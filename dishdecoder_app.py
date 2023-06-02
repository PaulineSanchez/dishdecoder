import numpy as np
from PIL import Image, UnidentifiedImageError
import io

import streamlit as st
from streamlit_cropper import st_cropper
from streamlit_extras.switch_page_button import switch_page

import json
import requests
import sqlite3

#Dish Decoder is an application where you can perform OCR on a recipe and translate it.
#The OCR and translation parts are powered by an API made with FastAPI. 
#This is the welcome page of the application.
#On that welcome page you will find an explication about what the application does and how to use it, an image to illustrate the explication and two buttons : one to log in (when authentified it will take you to the next page) and ont to sign up.

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

st.markdown('#')

st.title("Dish Decoder 🍲")
st.header("_Decode Recipes, Translate Tastes - Dish Decoder!_")

st.markdown("###")
st.markdown("###")


col_describe, col_imageexemple, col_buttons = st.columns([1, 1, 1])


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


with col_imageexemple:
    st.image("dishexplorer.png", use_column_width=True, caption="It would have been easier with Dish Decoder...")

# Connexion à la base de données SQLite
connection = sqlite3.connect("database.db")

# Création de la table user si elle n'existe pas déjà
with connection:
    cursor = connection.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL
        )
        """
    )

    # Création de la table link si elle n'existe pas déjà
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS link (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT NOT NULL,
            description TEXT NOT NULL,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            user_id INTEGER NOT NULL,
            FOREIGN KEY (user_id) REFERENCES user (id)
        )
        """
    )

with col_buttons:

    st.markdown("###")
    st.markdown("###")

    # Création d'un bouton pour créer un compte utilisateur
    if "show_create_user_button" not in st.session_state:
        st.session_state.show_create_user_button = True

    if st.session_state.show_create_user_button:
        if st.button("Create User"):
            st.session_state.show_create_user_button = False

    if not st.session_state.show_create_user_button:
        with st.form("create_user"):
            # Collecte des informations de l'utilisateur via un formulaire Streamlit
            username = st.text_input("Nom d'utilisateur", key="c")
            email = st.text_input("Email", key="d")
            password = st.text_input("Mot de passe", type="password", key="e")
            submitted_signup = st.form_submit_button("Créer un compte")

            # Vérification des champs vides
            if submitted_signup:
                if not username or not email or not password:
                    st.error("Veuillez remplir tous les champs d'entrée")
                else:
                    # Ajout de l'utilisateur à la base de données
                    with connection:
                        cursor = connection.cursor()
                        cursor.execute(
                            "INSERT INTO user (username, email, password) VALUES (?, ?, ?)",
                            (username, email, password),
                        )
                        connection.commit()
                        st.success("Utilisateur créé avec succès")
                        st.session_state.show_create_user_button = True


    st.markdown("###")
    st.markdown("###")

    # Création d'un bouton pour se connecter
    if "show_login_button" not in st.session_state:
        st.session_state.show_login_button = True

    if st.session_state.show_login_button:
        if st.button("Log in"):
            st.session_state.show_login_button = False

    if not st.session_state.show_login_button:

        with st.form("login_form"):
            # Collecte des informations de connexion de l'utilisateur via un formulaire Streamlit
            username = st.text_input("Nom d'utilisateur", key="nn")
            password = st.text_input("Mot de passe", type="password", key="b")
            submitted = st.form_submit_button("Connexion")

            # Vérification des champs 
            if submitted:
                if not username or not password:
                    st.error("Veuillez remplir tous les champs d'entrée")
                else:
                    # Vérification des informations de connexion dans la base de données
                    with connection:
                        cursor = connection.cursor()
                        cursor.execute("SELECT * FROM user WHERE username = ?", (username,))
                        user = cursor.fetchone()
                        if user and user[3] == password:
                            st.session_state.logged_in = True
                            # st.success("Connecté en tant que {}".format(user[1]))
                            st.session_state.username = user[1]
                            st.session_state.user_id = user[0]
                            switch_page("Next page")
                        else:
                            st.error("Nom d'utilisateur ou mot de passe incorrect")

