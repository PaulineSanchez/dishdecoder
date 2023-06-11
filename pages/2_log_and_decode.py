from datetime import datetime
import numpy as np
import pandas as pd
from PIL import Image, UnidentifiedImageError
import io
from typing import Union
import re

import cloudinary
import cloudinary.uploader
from st_btn_select import st_btn_select
import streamlit as st
from streamlit_cropper import st_cropper
from streamlit_extras.switch_page_button import switch_page

import json
import requests
import sqlite3

from io import BytesIO
import base64
from PIL import Image

import discord
from discord import SyncWebhook


#This is the second page of Dish Decoder, the user can only access it if he has logged in
#The user can see his history of translations and can also translate a new image
#These two tasks are available through two tabs
#After having translated an image, the user can give his opinion on the translation. This opinion is then sent to the API.
#The user can also logout from this page, it leads him back to the login page and clears the session state

st.set_option('deprecation.showfileUploaderEncoding', False)

st.set_page_config(
    initial_sidebar_state="collapsed",
    page_title="Dish Decoder",
    page_icon="🍲",
    layout='wide'
    )

st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)

st.session_state["ocr_and_translation_response"] = None if "ocr_and_translation_response" not in st.session_state else st.session_state["ocr_and_translation_response"]
st.session_state["username"] = None if "username" not in st.session_state else st.session_state["username"]
st.session_state["logged_in"] = False if "logged_in" not in st.session_state else st.session_state["logged_in"]
st.session_state["history"] = [] if "history" not in st.session_state else st.session_state["history"]
st.session_state["cropped_image"] = None if "cropped_image" not in st.session_state else st.session_state["cropped_image"]
st.session_state["user_image"] = None if "user_image" not in st.session_state else st.session_state["user_image"]
st.session_state["user_id"] = None if "user_id" not in st.session_state else st.session_state["user_id"]
st.session_state["concatened_ocr_texts"] = None if "concatened_ocr_texts" not in st.session_state else st.session_state["concatened_ocr_texts"]
st.session_state["corrected_sentences"] = None if "corrected_sentences" not in st.session_state else st.session_state["corrected_sentences"]
st.session_state["translated_paragraph"] = None if "translated_paragraph" not in st.session_state else st.session_state["translated_paragraph"]


st.title("Dish Decoder 🍲")

if st.session_state["username"] is not None:
    st.header("_Welcome {} ! Decode Recipes, Translate Tastes - Dish Decoder!_".format(st.session_state["username"].capitalize()))
else:
    st.header("_Welcome {} ! Decode Recipes, Translate Tastes - Dish Decoder!_".format(st.session_state["username"]))

st.markdown("###")
st.markdown("###")


def send_discord_notification(message):
    webhook = SyncWebhook.from_url("https://discord.com/api/webhooks/1117050342392217620/FJAU95KidaUPf5jZ53U3P5dxJYs_vn04FJ8PJJosvfsPKq449jHpNrKOJ1pLg27f5HEr")
    webhook.send(message)


def api_ocr_and_translation(image: Image.Image, source_lang: str, target_lang: str):
    """
    Call the OCR API to perform OCR on the image and translate it from the source language to the target language.
    """
    if isinstance(image, Image.Image):
        # convert as bytes
        img_byte_arr = io.BytesIO()
        image.save(img_byte_arr, format='PNG')
        img_byte_arr = img_byte_arr.getvalue()

    url = "http://localhost:7680/inference"
    files = {'file': img_byte_arr}
    data = {'source_lang': source_lang, 'target_lang': target_lang}
    response = requests.post(url, files=files, data=data)
    return response


def api_img2cloud(image: Image.Image):
    """
    Call the Img2cloud API to upload the image to Cloudinary.
    """
    if isinstance(image, Image.Image):
        # convert as bytes
        img_byte_arr2 = io.BytesIO()
        image.save(img_byte_arr2, format='PNG')
        img_byte_arr2 = img_byte_arr2.getvalue()

    else:
        img_byte_arr2 = image

    url = "http://localhost:7680/img2cloud"
    files = {'file': img_byte_arr2}
    response = requests.post(url, files=files)
    return response


def api_add_to_links(url_link: str, description: str, user_id: int):
    """
    Call the API to add a new link.
    """
    url="http://localhost:7680/add_to_links"
    data = {"url": url_link, "description": description, "user_id": user_id}
    response = requests.post(url, data=data)
    return response


def api_get_links(user_id: int):
    """
    Call the API to get the links of a user.
    """
    url="http://localhost:7680/get_links"
    data = {"user_id": user_id}
    response = requests.post(url, data=data)
    result = json.loads(response.content)
    print(user_id)
    print(result)
 
    if result is not None:
        if len(result) > 0:
            all_links = result

            # Afficher les liens
            st.session_state["history"] = []
            for link in all_links:
                if isinstance(link, dict):
                    url = link.get("url")
                    description = link.get("description")
                    timestamp = link.get("timestamp")
                    st.session_state["history"].append({'URL': url, 'Describe': description, 'Timestamp': timestamp})
        else:
            all_links = []
    else:
        all_links = []

    return all_links


def api_add_rating(user_id: int, user_rating: int, ocr_entry: str, corrected_ocr: str, translation_output: Union[list, str]):
    """
    Call the API to add a rating to a recipe. Many data are sent to the API, the user_id, the user_rating, the ocr entry, the corrected ocr and the translation output.
    """
    url="http://localhost:7680/add_rating"

    if isinstance(translation_output, list):
        translation_output = " ".join(translation_output)

    decoded_translation = translation_output.encode('latin-1').decode('unicode_escape')
    decoded_corrected_ocr = corrected_ocr.encode().decode('unicode-escape').strip("\n").strip("\n\n")
    new_ocr = re.sub('\n', '', decoded_corrected_ocr)

    data = {"user_id": user_id, "user_rating": user_rating, "ocr_entry": ocr_entry, "corrected_ocr": new_ocr, "translation_output": decoded_translation}
    print(data)
    response = requests.post(url, data=data)
    return response
    

tab_history, tab_decode = st.tabs(["History", "Decode"])


with tab_history:


    history = api_get_links(st.session_state["user_id"])
    if st.button("Refresh :recycle:"):
        history = api_get_links(st.session_state["user_id"])
    st.subheader("Saved recipes")
    if st.session_state["history"]:   
        
        df = pd.DataFrame(
            {
                "url": [st.session_state["history"][i]["URL"] for i in range(len(st.session_state["history"]))],
                "description": [st.session_state["history"][i]["Describe"] for i in range(len(st.session_state["history"]))],
                "timestamp" : [st.session_state["history"][i]["Timestamp"] for i in range(len(st.session_state["history"]))]
            }
        )
        st.dataframe(
                df,
                column_config={
                    "url": st.column_config.ImageColumn(
                        "🖼️ Saved images",
                        help="📢 Click twice on the image to make it bigger and click again once to make it full scren in another tab",
                        width="medium"
                    ),
                    # "url": st.column_config.LinkColumn(
                    #     "📡	URL",
                    #     width="medium"
                    # ),
                    "description": st.column_config.TextColumn(
                        "📋	Description",
                        width="medium",
                        help="📢 Here is the description of what you saved"
                    ),
                    "timestamp": st.column_config.DatetimeColumn(
                        "📅	Date",
                        format="D MMM YYYY, h:mm a",
                        width="medium",
                        help="📢 Here is the day you saved your masterpiece"
                    ),
                },
                hide_index=False,
            )
    else:
        st.info("No saved recipe")




with tab_decode:

    col_uploadimage, col_ocr, col_translation = st.columns([2, 3, 3])

    with col_uploadimage:
        uploaded_image= st.file_uploader("1. Select an image of the recipe of your choice...", type=["jpg", "png", "jpeg"])

        if uploaded_image is not None:
            st.session_state["user_image"] = Image.open((uploaded_image))
            st.image(st.session_state["user_image"], caption='Here is the recipe you just uploaded', use_column_width=True)

    with col_ocr:
        st.markdown("2. Let's crop that tasty recipe...")
        st.markdown(":warning: Our great application is only reading line by line")
        st.markdown("so please crop your recipe accordingly ! ")
        cropcheck = st.checkbox(label="Crop that recipe ! ", value=False)
        if cropcheck:

            if st.session_state["user_image"] is not None:

                img_file = st.session_state["user_image"]

                col_realtime, col_boxcolor, col_aspect = st.columns(3)
                with col_realtime:
                    realtime_update = st.checkbox(label="Update in Real Time", value=True)
                with col_boxcolor:    
                    box_color = st.color_picker(label="Box Color", value='#0000FF')
                with col_aspect:
                    aspect_choice = st.radio(label="Aspect Ratio", options=["1:1", "16:9", "4:3", "2:3", "Free"])
                    aspect_dict = {
                        "1:1": (1, 1),
                        "16:9": (16, 9),
                        "4:3": (4, 3),
                        "2:3": (2, 3),
                        "Free": None
                    }
                    aspect_ratio = aspect_dict[aspect_choice]
                # Get a cropped image from the frontend
                st.session_state["cropped_image"] = st_cropper(img_file, realtime_update=realtime_update, box_color=box_color,
                                                aspect_ratio=aspect_ratio)

                # Manipulate cropped image at will
                st.write("Preview")
                _ =  st.session_state["cropped_image"].thumbnail((800, 800))
                st.image(st.session_state["cropped_image"])

            else :
                st.markdown(":warning: Please upload an image first !")


    with col_translation:
        st.markdown("3. Let's ocr and translate that fabulous recipe...")
        option = st.radio("Translation Option:", ["🇫🇷 ➡️ 🇬🇧 (French to English)", "🇬🇧 ➡️ 🇫🇷 (English to French)"])
        translatecheck = st.button("OCR and translate that recipe!", key="translatecheck")   

        if translatecheck:
            if option == "🇫🇷 ➡️ 🇬🇧 (French to English)":
                source_lang = "fr"
                target_lang = "en"
            elif option == "🇬🇧 ➡️ 🇫🇷 (English to French)":
                source_lang = "en"
                target_lang = "fr"

            if st.session_state["cropped_image"] is not None:
                r = api_ocr_and_translation(st.session_state["cropped_image"], source_lang, target_lang)
                if r.status_code == 200:
                    response = r.json()
                    base64_image = response["image"]
                    image_data = base64.b64decode(base64_image)

                    image_stream = BytesIO(image_data)
                    image = Image.open(image_stream)

                    st.session_state["ocr_and_translation_response"] = image
                    st.session_state["concatenated_ocr_texts"] = response["concatenated_ocr_texts"]
                    st.session_state["corrected_sentences"] = response["corrected_sentences"]
                    st.session_state["translated_paragraph"] = response["translated_paragraph"]

                elif r.status_code == 404:
                    st.error("No text was found in the image")
                    message = f"Aucun texte n'a été trouvé dans l'image pour l'utilisateur : {st.session_state['username']}"
                    send_discord_notification(message)   

                else:
                    st.error("An error occured during the OCR and translation process")
                    message = f"Une erreur est survenue lors de la phase d'ocr et de traduction pour l'utilisateur : {st.session_state['username']}"
                    send_discord_notification(message)
            else:
                st.warning("Please crop the image before OCR and translation.")

        if st.session_state["ocr_and_translation_response"] is not None:
            st.image(st.session_state["ocr_and_translation_response"], caption='Here is the translated recipe', use_column_width=True)
            description = st.text_input("description", key="describe")
            send_to_cloud = st.button("Save this recipe to your history", key="send_to_cloud")

            if send_to_cloud:
                if description is not None and description != "":
                    try :
                        r = api_img2cloud(st.session_state["ocr_and_translation_response"])
                        received_url = r.text
                        add_bdd = api_add_to_links(received_url, description, st.session_state["user_id"])
                        if add_bdd.status_code == 200:
                            st.success("Recipe saved !")
                        else:
                            st.error("An error occured during the saving process")
                    except Exception as e:
                        message = f"Une erreur est survenue lors de la sauvegarde de la recette pour l'utilisateur : {st.session_state['username']}, voici l'erreur : {e}"
                        send_discord_notification(message)                 
                else:
                    st.error("Please enter a description")

            st.markdown("Rate this translation")
            rating = st.slider("Rate this translation, 0 means awful, 5 is ok and 10 is perfect", min_value=0, max_value=10, value=5, step=1, key="rating")
            st.write(f"You rated this translation {rating}/10")
            send_rating = st.button("Send your rating", key="send_rating")
            if send_rating:
                try :
                    print(st.session_state["user_id"], rating, st.session_state["concatenated_ocr_texts"], st.session_state["corrected_sentences"], st.session_state["translated_paragraph"])
                    r = api_add_rating(st.session_state["user_id"], rating, st.session_state["concatenated_ocr_texts"], st.session_state["corrected_sentences"], st.session_state["translated_paragraph"])
                    if r.status_code == 200:
                        st.success("Rating saved !")
                    else:
                        st.error("An error occured during the saving process")
                except Exception as e:
                    message = f"Une erreur est survenue lors de la sauvegarde de la note pour l'utilisateur : {st.session_state['username']}, voici l'erreur : {e}"
                    send_discord_notification(message)



if st.button("Go back to home page") or not st.session_state["logged_in"]:
    st.session_state["user_id"] = None
    st.session_state["history"] = []
    switch_page("dishdecoder_app")



