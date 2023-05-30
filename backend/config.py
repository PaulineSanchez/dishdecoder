from os import getenv
from dotenv import load_dotenv
from pydantic.dataclasses import dataclass


@dataclass
class Settings:
    api_key: str
    ocr_model_path: str
    en_to_fr_model_path: str
    fr_to_en_model_path: str
    device: int
    font_path: str

load_dotenv()

settings = Settings(
    api_key=getenv('API_KEY', None),
    ocr_model_path=getenv('OCR_MODEL_PATH', None),
    en_to_fr_model_path=getenv('EN_TO_FR_MODEL_PATH', None),
    fr_to_en_model_path=getenv('FR_TO_EN_MODEL_PATH', None),
    device=int(getenv('DEVICE', 0)),
    font_path=getenv('FONT_PATH'),
)
