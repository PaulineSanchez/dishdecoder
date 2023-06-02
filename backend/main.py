import io
from pathlib import Path
from PIL import Image

from fastapi import FastAPI, File, Form, UploadFile
from fastapi.responses import Response

from service import Service

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

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=7680)
