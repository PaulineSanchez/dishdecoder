import streamlit as st
import pandas as pd
import requests

from streamlit_extras.switch_page_button import switch_page


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

st.session_state["logged_in"] = False if "logged_in" not in st.session_state else st.session_state["logged_in"]


st.title("Dish Decoder 🍲")

st.header("Admin Page")

st.subheader("Data from API")

response = requests.post("http://localhost:7680/get_data")

#Appliquer de la couleur seulement sur la colonne user_rating
def color_col(val):
    if val >=8:
        color = 'RGB(144, 198, 149)'
    elif val < 5:
        color = 'RGB(196, 77, 86)'
    else:
        color = 'RGB(255, 255, 159)'
    
    return f'background-color: {color}'


if response.status_code == 200:
    data = response.json()  # Convertir la réponse en format JSON

    # Créer une liste de dictionnaires contenant les données
    table_data = []
    for item in data:      
        table_data.append({
            "id": item["id"],
            "ocr_entry": item["ocr_entry"],
            "corrected_ocr": item["corrected_ocr"],
            "translation_output": item["translation_output"],
            "user_rating": item["user_rating"]
        })

    # Afficher les données dans un tableau
    df = pd.DataFrame(table_data)
    st.table(df.style.applymap(color_col, subset=['user_rating']))

else:
    st.error("Erreur lors de la récupération des données.")


st.subheader("Download Data into CSV")


def convert_df(df):
    return df.to_csv().encode('utf-8')

csv = convert_df(df)

st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='large_df.csv',
    mime='text/csv',
)

if st.button("Go back to home page") or not st.session_state["logged_in"]:
    st.session_state["user_id"] = None
    st.session_state["history"] = []
    switch_page("dishdecoder_app")