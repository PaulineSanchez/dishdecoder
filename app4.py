import pandas as pd
import streamlit as st
import sqlite3

from datetime import datetime

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

def create_user():
    st.subheader("Créer un utilisateur")

    # Collecte des informations de l'utilisateur via un formulaire Streamlit
    username = st.text_input("Nom d'utilisateur", key="c")
    email = st.text_input("Email", key="d")
    password = st.text_input("Mot de passe", type="password", key="e")

    if st.button("Créer"):
        # Vérification des champs vides
        if not username or not email or not password:
            st.error("Veuillez remplir tous les champs d'entrée")
            return

        # Ajout de l'utilisateur à la base de données
        with connection:
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO user (username, email, password) VALUES (?, ?, ?)",
                (username, email, password),
            )
            connection.commit()

        st.success("Utilisateur créé avec succès")

# Ajouter verificateur d'email > qu'il y ait bien un @
# Ajouter que le nom d'utilisateur n'existe pas déjà


def login():
    
    link_data = []
    updated_link_data= []

    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:
        st.subheader("Connexion")

        # Collecte des informations de connexion de l'utilisateur via un formulaire Streamlit
        username = st.text_input("Nom d'utilisateur", key="nn")
        password = st.text_input("Mot de passe", type="password", key="b")

        if st.button("Se connecter"):
            # Vérification des informations de connexion dans la base de données
            with connection:
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM user WHERE username = ?", (username,))
                user = cursor.fetchone()
                if user and user[3] == password:
                    st.session_state.logged_in = True
                    st.success("Connecté en tant que {}".format(user[1]))
                    st.session_state.username = user[1]
                    st.session_state.user_id = user[0]
                else:
                    st.error("Nom d'utilisateur ou mot de passe incorrect")
                    return

    if st.session_state.logged_in:
        st.subheader("Bienvenue, {}".format(st.session_state.username))

        # Récupérer les liens associés à l'utilisateur depuis la base de données
        with connection:
            cursor = connection.cursor()
            cursor.execute("SELECT link.url, link.description, link.timestamp FROM link JOIN user ON link.user_id = user.id WHERE user.username = ?", (st.session_state.username,))
            links = cursor.fetchall()

        # Liste des liens (dans l'ordre inverse)
        all_links = links[::-1]

        # Afficher les liens
        if all_links:
            st.subheader("Liens sauvegardés")
            for link in all_links:
                url = link[0]
                description = link[1]
                timestamp = link[2]
                link_data.append({'URL': url, 'Description': description, 'Timestamp': timestamp})
                
            df = pd.DataFrame(link_data)
            st.subheader("Liens dans un DataFrame")
            st.dataframe(df)

        else:
            st.info("Aucun lien sauvegardé")

        # Formulaire pour ajouter un lien
        st.subheader("Ajouter un lien")
        url = st.text_input("URL", key="aa")
        description = st.text_input("description", key="describe")
        if st.button("Ajouter le lien"):
            # Ajout du lien à la base de données associée à l'utilisateur
            with connection:
                cursor = connection.cursor()
                current_timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                cursor.execute(
                    "INSERT INTO link (url, description, timestamp, user_id) VALUES (?, ?, ?, ?)",
                    (url, description, current_timestamp, st.session_state.user_id),
                )
                connection.commit()

            # Récupérer les liens mis à jour depuis la base de données
            with connection:
                cursor = connection.cursor()
                cursor.execute("SELECT link.url, link.description, link.timestamp FROM link JOIN user ON link.user_id = user.id WHERE user.username = ?", (st.session_state.username,))
                links = cursor.fetchall()

            # Liste des liens (dans l'ordre inverse)
            all_links = links[::-1]

            # Afficher les liens mis à jour
            if all_links:
                st.subheader("Liens sauvegardés mis à jour")
                for link in all_links:
                    url = link[0]
                    description = link[1]
                    timestamp = link[2]
                    updated_link_data.append({"URL": url, "Description": description, "Timestamp": timestamp})
                    
                df_updated = pd.DataFrame(updated_link_data)
                st.dataframe(df_updated)
                
            else:
                st.info("Aucun lien sauvegardé")


# Titre de l'application
st.title("Application de gestion d'utilisateurs")

# Appel des fonctions de création d'utilisateur et de connexion
login()
create_user()
