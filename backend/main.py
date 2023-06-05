import io
from pathlib import Path
from PIL import Image

from fastapi import FastAPI, File, Form, UploadFile
from fastapi.responses import Response

from service import Service
from sqlmodel import Session
from sqlmodel import create_engine, SQLModel

from models import User, Link ,engine


app = FastAPI()

service = Service()

@app.get("/")
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
    result = service.inference(image, source_lang, target_lang)

    with io.BytesIO() as output:
        result.save(output, format="PNG")
        contents = output.getvalue() 

    return Response(contents, media_type="image/png")

@app.post("/img2cloud", status_code=200, tags=["img2cloud"])
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

@app.post("/get_users", status_code=200, tags=["get_users"])
def get_users():
    """
    Get_users récupère la liste des utilisateurs.
    """
    with Session(engine) as session:
        users = session.query(User).all()

        return users

@app.post("/create_user", status_code=200, tags=["create_user"])
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

        return user

@app.post("/check_user", status_code=200, tags=["check_user"])
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
        user = session.query(User).filter(User.username == username).first()

        if user is None:
            return {"result": False}  # Utilisateur introuvable
        elif user.password == password:
            return {"result": True}  # Identifiants valides
        else:
            return {"result": False}  # Identifiants invalides
        


@app.post("/get_user_id", status_code=200, tags=["get_user_id"])
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
        user = session.query(User).filter(User.username == username, User.password == password).first()

        return user.id

      

@app.post("/add_to_links", status_code=200, tags=["add_to_links"])
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
    
@app.post("/get_links", status_code=200, tags=["get_links"])
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






if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=7680)

