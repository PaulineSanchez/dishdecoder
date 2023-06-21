import io
import re
import base64
import json
from pathlib import Path
from PIL import Image

from fastapi import FastAPI, File, Form, UploadFile, HTTPException
from fastapi.responses import Response

from service import Service
from sqlalchemy import func
from sqlmodel import Session
from sqlmodel import create_engine, SQLModel

from models import User, Link ,engine, Data
from alerting import send_discord_notification


app = FastAPI()

service = Service()


@app.get("/", tags=["status"])
def root():
    return {"message": "Hello World"}

@app.get("/healthcheck", status_code=200, tags=["status"])
def healthcheck():
    return {"message": "OK"}

@app.post("/inference", status_code=200, tags=["inference"])
def inference(
    source_lang: str = Form(...),
    target_lang: str = Form(...),
    file: UploadFile = File(...),
):
    """
    Inference lance le processus de traduction sur une image.

    Args:
        source_lang (str): Langue source (avant traduction)
        target_lang (str): Langue cible (après traduction)
        file (UploadFile): Fichier image à traiter
    """
    image = Image.open(io.BytesIO(file.file.read()))

    try: 
        result, concatenated_ocr_texts, corrected_sentences, translated_paragraph = service.inference(image, source_lang, target_lang)
      
        with io.BytesIO() as output:
            result.save(output, format="PNG")
            image_contents = output.getvalue() 

            concatenated_ocr_texts_json = json.dumps(concatenated_ocr_texts)
            corrected_sentences_json = json.dumps(corrected_sentences)
            translated_paragraph_json = json.dumps(translated_paragraph)

        return {
            "image": base64.b64encode(image_contents).decode("utf-8"),
            "concatenated_ocr_texts": concatenated_ocr_texts_json,
            "corrected_sentences": corrected_sentences_json,
            "translated_paragraph": translated_paragraph_json,
        }
    
    except Exception as e:
        print(e)
        raise HTTPException(status_code=404, detail="The OCR wasn't able to detect any text in the image.")
    
        

@app.post("/img2cloud", status_code=200, tags=["database"])
def img2cloud(
    file: UploadFile = File(...),
):
    """
    Img2cloud télécharge une image sur Cloudinary.

    Args:
        file (UploadFile): Fichier image à télécharger
    """
    image = Image.open(io.BytesIO(file.file.read()))
    result = service.image_to_cloud(image)

    return Response(result)

  
@app.post("/create_user", status_code=200, tags=["users"])
def create_user(
    username: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
):
    """
    Create_user crée un nouvel utilisateur.

    Args:
        username (str): Nom d'utilisateur
        email (str): Adresse email
        password (str): Mot de passe
    """
    with Session(engine) as session:
        user = User(username=username, email=email, password=password)
        session.add(user)
        session.commit()

        # Envoi de la notification Discord
        message = f"Un nouvel utilisateur a été créé : {username}"
        send_discord_notification(message)


        return user


@app.post("/check_user", status_code=200, tags=["users"])
def check_user(
    username: str = Form(...),
    password: str = Form(...),
):
    """
    Check_user vérifie les identifiants d'un utilisateur.

    Args:
        username (str): Nom d'utilisateur
        password (str): Mot de passe
    """
    with Session(engine) as session:
        user = session.query(User).filter(func.lower(User.username) == func.lower(username)).first()

        if user is None:
            return {"result": False}  # Utilisateur introuvable
        elif user.password == password:
            return {"result": True}  # Identifiants valides
        else:
            return {"result": False}  # Identifiants invalides
        


@app.post("/check_username", status_code=200, tags=["users"])
def check_username(
    username: str = Form(...),
):
    """
    Check_username vérifie si un nom d'utilisateur est déjà utilisé. Les noms d'utilisateurs doivent être uniques. Les majuscules et minuscules ne sont pas prises en compte.

    Args:
        username (str): Nom d'utilisateur
    """
    with Session(engine) as session:
        user = session.query(User).filter(func.lower(User.username) == func.lower(username)).first()

        if user is None:
            return {"result": True} # Nom d'utilisateur disponible
        else:
            return {"result": False} # Nom d'utilisateur indisponible
        

@app.post("/check_email", status_code=200, tags=["users"])
def check_email(
    email: str = Form(...),
):
    """
    Check_email vérifie si une adresse email est au bon format.
    """
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if re.match(email_pattern, email):
        return {"result": True} # Adresse email valide
    else:
        return {"result": False} # Adresse email invalide


@app.post("/check_password", status_code=200, tags=["users"])
def check_password(
    password: str = Form(...),
):
    """
    Check_password vérifie si un mot de passe est au bon format.
    """
    password_pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d\W]{8,}$" # Au moins 8 caractères, une majuscule, une minuscule et un chiffre
    if re.match(password_pattern, password):
        return {"result": True} # Mot de passe valide
    else:
        return {"result": False} # Mot de passe invalide


@app.post("/get_user_id", status_code=200, tags=["users"])
def get_user_id(
    username: str = Form(...),
    password: str = Form(...),
):
    """
    Get_user_id récupère l'ID d'un utilisateur.

    Args:
        username (str): Nom d'utilisateur
        password (str): Mot de passe
    """
    with Session(engine) as session:
        user = session.query(User).filter(func.lower(User.username) == func.lower(username), User.password == password).first()

        return user.id

      

@app.post("/add_to_links", status_code=200, tags=["database"])
def add_to_links(
    url: str = Form(...),
    description: str = Form(...),
    user_id: int = Form(...),
):
    """
    Add_to_links ajoute un lien à la liste des liens.

    Args:
        url (str): URL du lien
        description (str): Description du lien
        user_id (int): ID de l'utilisateur
    """
    with Session(engine) as session:
        link = Link(url=url, description=description, user_id=user_id)
        session.add(link)
        session.commit()

        return link
    
@app.post("/get_links", status_code=200, tags=["database"])
def get_links(
    user_id: int = Form(...),
):
    """
    Get_links récupère la liste des liens d'un utilisateur.

    Args:
        user_id (int): ID de l'utilisateur
    """
    with Session(engine) as session:
        links = session.query(Link).filter(Link.user_id == user_id).all()
        for link in links:
            link.timestamp = link.timestamp.strftime("%d-%m-%Y %H:%M")

        return links

@app.post("/add_rating", status_code=200, tags=["database"])
def add_rating(
    user_id: int = Form(...),
    user_rating: int = Form(...),
    ocr_entry: str = Form(...),
    corrected_ocr: str = Form(...),
    translation_output: str = Form(...),
): 
    """
    Add rating ajoute une note sur la qualité de la traduction à la base de données.
    Args:
        user_id (int): Id de l'utilisateur
        user_rating (int): Note de l'utilisateur
        ocr_entry (str): Texte original
        corrected_ocr (str): Texte corrigé
        translation_output (str): Texte traduit
    """

    with Session(engine) as session:
        rating = Data(user_id=user_id, user_rating=user_rating, ocr_entry=ocr_entry, corrected_ocr=corrected_ocr, translation_output=translation_output)
        session.add(rating)
        session.commit()

        return rating
        
@app.post("/get_data", status_code=200, tags=["database"])
def get_data():
     
     """
    Get_data récupère la liste des données de la base de données.
    """
     
     with Session(engine) as session:
        data = session.query(Data).all()
        return data
            


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=7680)

