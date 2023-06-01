import streamlit as st
import cloudinary
import cloudinary.uploader

# Configuration de Cloudinary (remplacez YOUR_CLOUD_NAME, YOUR_API_KEY et YOUR_API_SECRET par vos informations)
cloudinary.config(
    cloud_name="dcxlyp0xn",
    api_key="989176184167239",
    api_secret="3fx0CfVXvoZwSwsXpCxMLNbb4Qw"
)

# Interface Streamlit
st.title("Téléchargement d'image")

uploaded_image = st.file_uploader("Sélectionnez une image", type=['jpg', 'jpeg', 'png'])

if uploaded_image is not None:
    response = cloudinary.uploader.upload(uploaded_image)
    image_url = response['secure_url']
    
    st.write("L'image a été téléchargée avec succès !")
    st.write("URL de l'image :", image_url)
