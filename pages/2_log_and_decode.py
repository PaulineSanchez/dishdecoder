from datetime import datetime
import numpy as np
import pandas as pd
from PIL import Image, UnidentifiedImageError
import io

import cloudinary
import cloudinary.uploader
from st_btn_select import st_btn_select
import streamlit as st
from streamlit_cropper import st_cropper
from streamlit_extras.switch_page_button import switch_page

import json
import requests
import sqlite3

#This is the second page of Dish Decoder, the user can only access it if he has logged in
#The user can see his history of translations and can also translate a new image
#These two tasks are available through two tabs
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

st.session_state["ocr_response"] = None if "ocr_response" not in st.session_state else st.session_state["ocr_response"]
st.session_state["username"] = None if "username" not in st.session_state else st.session_state["username"]
st.session_state["logged_in"] = False if "logged_in" not in st.session_state else st.session_state["logged_in"]
st.session_state["history"] = [] if "history" not in st.session_state else st.session_state["history"]

st.title("Dish Decoder 🍲")
st.header("_Welcome {} ! Decode Recipes, Translate Tastes - Dish Decoder!_".format(st.session_state["username"]))

st.markdown("###")
st.markdown("###")

# Connexion à la base de données SQLite
connection = sqlite3.connect("database.db")

def api_ocr(image: Image.Image, source_lang: str, target_lang: str):
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

def get_history():
    """
    Get the history of translations from the database.
    """
    with connection:
        cursor = connection.cursor()
        cursor.execute("SELECT link.url, link.description, link.timestamp FROM link JOIN user ON link.user_id = user.id WHERE user.username = ?", (st.session_state.username,))
        links = cursor.fetchall()

        # Liste des liens (dans l'ordre inverse)
        all_links = links[::-1]

        # Afficher les liens
        if all_links:
            st.session_state["history"] = []
            for link in all_links:
                url = link[0]
                description = link[1]
                timestamp = link[2]
                st.session_state["history"].append({'URL': url, 'Describe': description, 'Timestamp': timestamp})


cropped_img = None
user_image = None


tab_history, tab_decode = st.tabs(["History", "Decode"])

with tab_history:
    get_history()
    if st.button("Refresh :recycle:"):
        get_history()
    if st.session_state["history"]:   
        st.subheader("Saved recipes")
        st.dataframe(pd.DataFrame(st.session_state["history"]))
    else:
        st.info("Aucun lien sauvegardé")


with tab_decode:

    col_uploadimage, col_ocr, col_translation = st.columns(3)

    with col_uploadimage:
        uploaded_image= st.file_uploader("1. Select an image of the recipe of your choice...", type=["jpg", "png", "jpeg"])

        if uploaded_image is not None:
            user_image = Image.open((uploaded_image))
            st.image(user_image, caption='Here is the recipe you just uploaded', use_column_width=True)

    user_image = user_image

    with col_ocr:
        st.markdown("2. Let's crop that tasty recipe...")
        st.markdown(":warning: Our great application is only reading line by line")
        st.markdown("so please crop your recipe accordingly ! ")
        cropcheck = st.checkbox(label="Crop that recipe ! ", value=False)
        if cropcheck:

            if user_image is not None:

                img_file = user_image

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
                cropped_img = st_cropper(img_file, realtime_update=realtime_update, box_color=box_color,
                                                aspect_ratio=aspect_ratio)

                # Manipulate cropped image at will
                st.write("Preview")
                _ = cropped_img.thumbnail((800, 800))
                st.image(cropped_img)

            else :
                st.markdown(":warning: Please upload an image first !")

    cropped_img = cropped_img

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

            if cropped_img is not None:
                r = api_ocr(cropped_img, source_lang, target_lang)
                if r.status_code == 200:
                    st.session_state["ocr_response"] = r.content
                else:
                    st.error("An error occured during the OCR process")
            else:
                st.warning("Please crop the image before OCR and translation.")

        if st.session_state["ocr_response"] is not None:
            st.image(st.session_state["ocr_response"], caption='Here is the translated recipe', use_column_width=True)
            description = st.text_input("description", key="describe")
            send_to_cloud = st.button("Save this recipe to your history", key="send_to_cloud")

            if send_to_cloud:
                if description is not None and description != "":
                    r = api_img2cloud(st.session_state["ocr_response"])
                    received_url = r.text
                    with connection:
                        cursor = connection.cursor()
                        current_timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                        cursor.execute(
                            "INSERT INTO link (url, description, timestamp, user_id) VALUES (?, ?, ?, ?)",
                            (received_url, description, current_timestamp, st.session_state.user_id),
                        )
                        connection.commit()
                    st.success("Recipe saved to your history !")
                else:
                    st.error("Please enter a description")



if st.button("Go back to home page") or not st.session_state["logged_in"]:
    switch_page("dishdecoder_app")