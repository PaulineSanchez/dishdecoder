import streamlit as st
import numpy as np
from PIL import Image, UnidentifiedImageError
import io
from streamlit_cropper import st_cropper
import requests
import json

#Dish Decoder is an application where you can perform OCR on a recipe and translate it.
#The OCR and translation parts are powered by an API made with FastAPI. 


st.set_option('deprecation.showfileUploaderEncoding', False)

st.set_page_config(
    page_title="Dish Decoder",
    page_icon="🍲",
    layout='wide')

st.title("Dish Decoder 🍲")
st.header("_Decode Recipes, Translate Tastes - Dish Decoder!_")

st.markdown("###")
st.markdown("###")

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




cropped_img = None
user_image = None

col_describe, col_uploadimage, col_ocr, col_translation = st.columns(4)

with col_describe:
    tab1, tab2 = st.tabs(["English", "Français"])

    with tab1:
        st.markdown("**Welcome to Dish Decoder!**")
        st.markdown("Dish Decoder is an application")
        st.markdown("where you can perform OCR on a recipe") 
        st.markdown("and translate it.") 
        st.markdown("Not sure what it means ?") 
        st.markdown("Just try it!")

    with tab2:
        st.markdown("Bienvenue sur Dish Decoder !") 
        st.markdown("Dish Decoder est une application") 
        st.markdown("où vous pouvez effectuer de l'OCR sur une recette et la traduire.") 
        st.markdown("Vous ne savez pas ce que cela signifie ?") 
        st.markdown("Essayez-le tout simplement!")

    _, col_btn, _ = st.columns([5, 2, 5])

    with col_btn:
        st.markdown("**:red[Try it out!]**" " " ":arrow_upper_right:")
           
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
    translatecheck = st.checkbox("OCR and translate that recipe!", value=False, key="translatecheck")   

    if translatecheck:
        if option == "🇫🇷 ➡️ 🇬🇧 (French to English)":

            if cropped_img is not None:
                response = api_ocr(cropped_img, "fr", "en")

                if response.status_code == 200:
                    image_data = response.content
                    st.image(image_data, caption='Here is the translated recipe', use_column_width=True)
                else:
                    st.warning("OCR and translation failed. Please try again.")
            else:
                st.warning("Please crop the image before OCR and translation.")
    
    if translatecheck:
        if option == "🇬🇧 ➡️ 🇫🇷 (English to French)":
            
            if cropped_img is not None:
                response = api_ocr(cropped_img, "en", "fr")
    
                if response.status_code == 200:
                    image_data = response.content
                    st.image(image_data, caption='Here is the translated recipe', use_column_width=True)
                else:
                    st.warning("OCR and translation failed. Please try again.")
            else:
                st.warning("Please crop the image before OCR and translation.")

   




            
            




# with col_ocr:
#     st.markdown("2. Let's extract the text of that fabulous recipe...")
#     st.button("OCR that recipe!")