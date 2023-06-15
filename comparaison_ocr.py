import os
import numpy as np
from PIL import Image
import easyocr
from paddleocr import PaddleOCR
from rapidfuzz import fuzz
from rapidfuzz.distance import Levenshtein

easyocr_base = easyocr.Reader(['en', 'fr'])
paddleocr_base = PaddleOCR(use_angle_cls=True, use_space_char=True, lang='latin')
paddleocr_finetuned = PaddleOCR(rec_model_dir='models/ocr_model', config="models/ocr_model/config.yml", rec_char_dict_path='models/ocr_model/latin_dict.txt', use_angle_cls=True, use_space_char=True, lang='latin')

liste_easyocr_base = []
liste_paddleocr_base = []
liste_paddleocr_finetuned = []

liste_score_easyocr_base_indel = []
liste_score_paddleocr_base_indel = []
liste_score_paddleocr_finetuned_indel = []

liste_score_easyocr_base_levenshtein = []
liste_score_paddleocr_base_levenshtein = []
liste_score_paddleocr_finetuned_levenshtein = []

def average(liste):
    return sum(liste) / len(liste)

def ocerisation(dossier_image):
    for fichier_image in sorted(os.listdir(dossier_image)):
        chemin_image = os.path.join(dossier_image, fichier_image)
        pix = np.array(Image.open(chemin_image).convert('RGB'))

        result_easyocr_base = easyocr_base.readtext(pix, paragraph=True, detail=0)
        txts_easyocr_base = ' '.join(result_easyocr_base)

        result_paddleocr_base = paddleocr_base.ocr(pix)
        txts_paddleocr_base = result_paddleocr_base

        result_paddleocr_finetuned = paddleocr_finetuned.ocr(pix)
        txts_paddleocr_finetuned = result_paddleocr_finetuned

        liste_easyocr_base.append(txts_easyocr_base)
        liste_paddleocr_base.append(txts_paddleocr_base[0][0][1][0])
        liste_paddleocr_finetuned.append(txts_paddleocr_finetuned[0][0][1][0])

        fichier_verite_terrain = open("fichier_verite_terrain.txt", "r")
        lignes = fichier_verite_terrain.readlines()

        liste_lignes_avec_deux_elements_par_ligne = []

        for chaque_ligne in lignes:
            deux_elements_par_ligne = chaque_ligne.strip().split("\t")
            liste_lignes_avec_deux_elements_par_ligne.append(deux_elements_par_ligne)


        verite_terrain = ""  
        for element in liste_lignes_avec_deux_elements_par_ligne:
            if element[0] == fichier_image:
                verite_terrain = element[1].strip("\n")
                break  

        liste_score_easyocr_base_indel.append(fuzz.ratio(txts_easyocr_base, verite_terrain))
        liste_score_paddleocr_base_indel.append(fuzz.ratio(txts_paddleocr_base[0][0][1][0], verite_terrain))
        liste_score_paddleocr_finetuned_indel.append(fuzz.ratio(txts_paddleocr_finetuned[0][0][1][0], verite_terrain))


        liste_score_easyocr_base_levenshtein.append(Levenshtein.distance(txts_easyocr_base, verite_terrain))
        liste_score_paddleocr_base_levenshtein.append(Levenshtein.distance(txts_paddleocr_base[0][0][1][0], verite_terrain))
        liste_score_paddleocr_finetuned_levenshtein.append(Levenshtein.distance(txts_paddleocr_finetuned[0][0][1][0], verite_terrain))

    print("***************")
    print("Distance d'Indel")
    print(f""" easy_ocr_base: {liste_score_easyocr_base_indel}, paddle_ocr_base: {liste_score_paddleocr_base_indel}, paddle_ocr_finetuned: {liste_score_paddleocr_finetuned_indel}""")
    print("***************")
    print(f""" avg_easy_ocr_base: {round(average(liste_score_easyocr_base_indel), 2)}, avg_paddle_ocr_base: {round(average(liste_score_paddleocr_base_indel), 2)}, avg_paddle_ocr_finetuned: {round(average(liste_score_paddleocr_finetuned_indel), 2)}""")
    print("***************")
    print("Distance de Levenshtein")
    print(f""" easy_ocr_base: {liste_score_easyocr_base_levenshtein}, paddle_ocr_base: {liste_score_paddleocr_base_levenshtein}, paddle_ocr_finetuned: {liste_score_paddleocr_finetuned_levenshtein}""")
    print("***************")
    print(f""" avg_easy_ocr_base: {round(average(liste_score_easyocr_base_levenshtein), 2)}, avg_paddle_ocr_base: {round(average(liste_score_paddleocr_base_levenshtein), 2)}, avg_paddle_ocr_finetuned: {round(average(liste_score_paddleocr_finetuned_levenshtein), 2)}""")
    print("***************")

ocerisation("images_test_ocr")
