import math
from typing import List, Tuple, Union

import numpy as np
from paddleocr import PaddleOCR
from PIL import Image, ImageDraw, ImageFont
from transformers import pipeline

from config import settings

class Service:
    def __init__(self) -> None:
        self.ocr_model = PaddleOCR(
            rec_model_dir=settings.ocr_model_path,
            config=f"{settings.ocr_model_path}/config.yml",
            rec_char_dict_path=f"{settings.ocr_model_path}/latin_dict.txt",
            use_angle_cls=True,
            use_space_char=True,
            lang="latin",
        )
        self.en_to_fr = pipeline(
            model=settings.en_to_fr_model_path, 
            tokenizer=settings.en_to_fr_model_path, 
            task="translation",
            device=settings.device,
        )
        self.fr_to_en = pipeline(
            model=settings.fr_to_en_model_path, 
            tokenizer=settings.fr_to_en_model_path, 
            task="translation",
            device=settings.device,
        )

    def inference(self, image:Image.Image, source_lang: str, target_lang: str) -> Image.Image:
        """
        Inference lance le processus de traduction du texte sur une image.

        Args:
            image (Image.Image): Image à traiter
            source_lang (str): Langue source (avant traduction)
            target_lang (str): Langue cible (après traduction)
        
        Returns:
            Image.Image: Image de base avec le texte traduit
        """
        ocr_results = self.do_ocr(image)
        ocr_texts = [line[1][0] for line in ocr_results]
        # ocr_confidence = [line[1][1] for line in ocr_results]
        ocr_bbox = [line[0] for line in ocr_results]
        translated_texts = self.do_translation(ocr_texts, source_lang, target_lang)
        post_processed_image = self.do_post_processing(image, ocr_bbox, translated_texts)
        return post_processed_image
        
    def do_ocr(self, image:Image.Image) -> List[List[Union[List[List[float]], Tuple[str, float]]]]:
        """
        Do OCR lance le modèle d'OCR sur une image.

        Args: 
            image (Image.Image): Image à traiter

        Returns:
            List[List[Union[List[List[float]], Tuple[str, float]]]]: Liste de liste de listes ([bbox], (texte, confiance))
        """
        pix = np.array(image.convert('RGB'))
        result_base = self.ocr_model.ocr(pix)
        
        return result_base[0]

    def do_translation(self, ocr_texts: List[str], source_lang: str, target_lang: str) -> List[str]:
        """
        Do translation lance le modèle de traduction sur la liste de textes sortie par l'OCR.

        Args:
            ocr_texts (List(str)): Liste de textes à traduire
            source_lang (str): Langue source (avant traduction)
            target_lang (str): Langue cible (après traduction)
        
        Returns:
            List(str): Liste de textes traduits

        Raises:
            ValueError: Si la langue source n'est pas 'en' ou 'fr'
        """

        if source_lang == "en":
            translated_texts = self.en_to_fr(ocr_texts)
        elif source_lang == "fr":
            translated_texts = self.fr_to_en(ocr_texts)
        else:
            raise ValueError("Source language must be either 'en' or 'fr'")
        
        return [line["translation_text"] for line in translated_texts]
    


    def do_post_processing(self, image: Image.Image, bboxes: List[List[float]], translated_texts: List[str]) -> Image.Image:
        """
        Do post processing applique des rectangles opaques sur les coordonnées des bbox et les textes traduits sur l'image de base.

        Args:
            image (Image.Image): Image de base
            bboxes (List[List[float]]): Liste de listes de coordonnées des bbox
            translated_texts (List[str]): Liste de textes traduits

        Returns:
            Image.Image: Image de base avec les rectangles et les textes traduits
        """
        
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype(settings.font_path, 14)

        for bbox, text in zip(bboxes, translated_texts):
            x, y = bbox[0][0], bbox[0][1]

            bbox = [tuple(point) for point in bbox]
            draw.polygon(bbox, fill="white")
            
            dx = bbox[1][0] - bbox[0][0]
            dy = bbox[1][1] - bbox[0][1]
            angle = math.degrees(math.atan2(dy, dx))

            center_point = ((x + bbox[2][0]) // 2, (y + bbox[2][1]) // 2)

            rotated_img = image.rotate(angle, center=center_point, resample=Image.BICUBIC, expand=True)

            text_img = Image.new("RGBA", rotated_img.size, (0, 0, 0, 0))
            text_draw = ImageDraw.Draw(text_img)

            rotated_position = (center_point[0] - font.getsize(text)[0] // 2, center_point[1] - font.getsize(text)[1] // 2)
            text_draw.text(rotated_position, text, font=font, fill="black")

            text_img = text_img.rotate(-angle, center=center_point, resample=Image.BICUBIC)


            image.paste(text_img, mask=text_img)

            
        return image
    
 