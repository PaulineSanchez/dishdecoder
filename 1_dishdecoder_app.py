import streamlit as st
from st_btn_select import st_btn_select
from streamlit_extras.switch_page_button import switch_page

import json
import requests

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

st.session_state["logged_in"] = False if "logged_in" not in st.session_state else st.session_state["logged_in"]

st.title("Dish Decoder 🍲")
st.header("_Decode Recipes, Translate Tastes - Dish Decoder!_")

st.markdown("###")
st.markdown("###")


def api_create_user(username: str, email: str, password: str):
    """
    Call the API to create a new user.
    """
    url="http://localhost:7680/create_user"
    data = {"username": username, "email": email, "password": password}
    response = requests.post(url, data=data)
    return response


def api_check_user(username: str, password: str):
    """
    Call the API to check the user credentials.
    """
    url = "http://localhost:7680/check_user"
    data = {"username": username, "password": password}
    response = requests.post(url, data=data)
    result = json.loads(response.content).get("result")
    return result


def api_get_user_id(username: str, password: str):
    """
    Call the API to get the user id.
    """
    url = "http://localhost:7680/get_user_id"
    data = {"username": username, "password": password}
    response = requests.post(url, data=data)
    result = json.loads(response.content)
    return result

def api_check_username(username: str):
    """
    Call the API to check if the username is already taken.
    """
    url = "http://localhost:7680/check_username"
    data = {"username": username}
    response = requests.post(url, data=data)
    result = json.loads(response.content).get("result")
    return result

def api_check_email(email: str):
    """
    Call the API to check if the email has the right form.
    """
    url = "http://localhost:7680/check_email"
    data = {"email": email}
    response = requests.post(url, data=data)
    result = json.loads(response.content).get("result")
    return result

def api_check_password(password: str):
    """
    Call the API to check if the password has the right form.
    """
    url = "http://localhost:7680/check_password"
    data = {"password": password}
    response = requests.post(url, data=data)
    result = json.loads(response.content).get("result")
    return result

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


with col_buttons:
  
    st.markdown("###")
    st.markdown("###")
    st.markdown("###")
    st.markdown("###")
    st.markdown("###")

    buttons = st_btn_select(("Join the cooks", "Create User", "Log in"))

    container = st.container()

    if buttons == "Join the cooks":
        with container:
            st.empty()

    if buttons == "Create User":
        with container:
            create_user_form = st.form("create_user")
            # Collecte des informations de l'utilisateur via un formulaire Streamlit
            username = create_user_form.text_input("Nom d'utilisateur", key="c")
            email = create_user_form.text_input("Email", key="d")
            password = create_user_form.text_input("Mot de passe", type="password", key="e")
            submitted_signup = create_user_form.form_submit_button("Créer un compte")

            # Vérification des champs du formulaire
            if submitted_signup:
                is_valid = True
                
                # Vérification du nom d'utilisateur
                check_username_result = api_check_username(username)
                if not check_username_result:
                    st.error("Ce nom d'utilisateur est déjà pris, veuillez en choisir un autre")
                    is_valid = False
                
                # Vérification du mot de passe
                check_password_result = api_check_password(password)
                if not check_password_result:
                    st.error("Le mot de passe doit contenir au moins 8 caractères, dont une majuscule, une minuscule et un chiffre")
                    is_valid = False
                
                # Vérification de l'adresse e-mail
                check_email_result = api_check_email(email)
                if not check_email_result:
                    st.error("Veuillez entrer une adresse email valide")
                    is_valid = False
                
                # Création du compte si tous les champs sont valides
                if is_valid:
                    reponse_api = api_create_user(username, email, password)
                    if reponse_api.status_code == 200:
                        st.success("Compte créé avec succès, connectez-vous depuis l'onglet 'Log in'")
                    else:
                        st.error("Une erreur s'est produite lors de la création du compte, veuillez réessayer et vous assurer de remplir tous les champs")

                    

    if buttons == "Log in":
        with container:
            login_form = st.form("login_form")
            # Collecte des informations de connexion de l'utilisateur via un formulaire Streamlit
            username = login_form.text_input("Nom d'utilisateur", key="nn")
            password = login_form.text_input("Mot de passe", type="password", key="b")
            submitted = login_form.form_submit_button("Connexion")
          
            # Vérification des champs
            if submitted:
                r = api_check_user(username, password)
                print(r)
                if r :
                    st.session_state["logged_in"] = True
                    st.session_state["username"] = username
                    r_user_id = api_get_user_id(username, password)
                    st.session_state["user_id"] = r_user_id
                    st.success("Connexion réussie")
                    switch_page("log_and_decode")
                elif r == False:
                    if username == "superadmin" and password == "superadmin":
                        st.session_state["logged_in"] = True
                        switch_page("admin")
                    else:
                        st.error("Nom d'utilisateur ou mot de passe incorrect")
                else:
                    st.error("Erreur lors du processus")

