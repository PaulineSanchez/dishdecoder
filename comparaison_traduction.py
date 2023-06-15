from transformers import pipeline

## TRADUCTION ANGLAIS VERS FRANCAIS

# model_checkpoint_base_en_fr = "Helsinki-NLP/opus-mt-en-fr"
# model_checkpoint_new_en_fr = "PaulineSanchez/translation_for_recipes_en_fr"

# translator_base_en_fr = pipeline("translation", model=model_checkpoint_base_en_fr)
# translator_new_en_fr = pipeline("translation", model=model_checkpoint_new_en_fr)

## TRADUCTION FRANCAIS VERS ANGLAIS

model_checkpoint_base_fr_en = "Helsinki-NLP/opus-mt-fr-en"
model_checkpoint_new_fr_en = "PaulineSanchez/translation_for_recipes_fr_en"

translator_base_fr_en = pipeline("translation", model=model_checkpoint_base_fr_en)
translator_new_fr_en = pipeline("translation", model=model_checkpoint_new_fr_en)


to_be_translated = "Insérer ici le texte que vous souhaitez traduire"


print("xxxxxx")
print("Phrase à traduire :", to_be_translated)
# print("xxxxxx")
# print("Avec le modèle de base en vers fr :", translator_base_en_fr(to_be_translated))
# print("xxxxxx")
# print("Avec le modèle finetuné fr vers en :", translator_new_en_fr(to_be_translated))
# print("xxxxxx")
print("xxxxxx")
print("Avec le modèle de base fr vers en:", translator_base_fr_en(to_be_translated))
print("xxxxxx")
print("Avec le modèle finetuné fr vers en:", translator_new_fr_en(to_be_translated))
