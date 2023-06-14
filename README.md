# dishdecoder
🍽️

### RAPPORT SUR LE PROJET DISHDECODER

PLAN :

I. Introduction

    1.1 Contexte
    1.2 Objectifs
    1.3 Approche de la solution
    1.4 Technologies utilisées
    1.5 Schéma de l’application

II. ETAT DE L’ART

III. DISHDECODER

    3.1 Le modèle d'OCR
        3.1.1 Le choix du modèle
        3.1.2 Les données nécessaires à l’entraînement du modèle
        3.1.3 La création du dataset
        3.1.4 Le prétraitement des données
        3.1.5 Le stockage du dataset
        3.1.6 L’entraînement du modèle
        3.1.7 Configuration des hyperparamètres du modèle
        3.1.8 Comparaison des modèles et choix du meilleur
        3.1.9 Le stockage du modèle

    3.2 Les modèles de traduction
        3.2.1 Le choix des modèles
        3.2.2 Les données nécessaires à l’entraînement des modèles
        3.2.3 La création du dataset
        3.2.4 Le prétraitement des données
        3.2.5 Le stockage du dataset
        3.2.6 L’entraînement des modèles
        3.2.7 Configuration des hyperparamètres des modèles
        3.2.8 Comparaison des modèles et choix des meilleurs
        3.2.9 Le stockage des modèles

    3.3 L'utilisation d'Open AI
        3.3.1 Pourquoi le choix d'Open AI ?
        3.3.2 L'API d'Open AI
        3.3.3 Le modèle utilisé
        3.3.4 Le prompt

    3.4 Le back-end
        3.4.1 L’API
        3.4.2 La schématisation de l’API
        3.4.3 La base de données relationnelle
        3.4.4 Le stockage des images des utilisateurs

    3.5 Le front-end
        3.5.1 L'utilisation de Streamlit
        3.5.2 La schématisation du front-end
        3.5.3 Les fonctionnalités de l'application
        3.5.4 Le parcours utilisateur
        3.5.5 Le parcours administrateur
    
    3.6 L'organisation du projet
        3.6.1 Le Trello (GANT ?)
        3.6.2 Le Kanban
        3.6.2 Le GitHub

IV. CONCLUSION

    4.1 La réalisation du projet
    4.2 Les difficultés rencontrées
    4.3 Les améliorations possibles
    4.4 Les perspectives d'évolution
    

# I. Introduction

## 1.1. Contexte

Depuis plusieurs mois maintenant, l'Intelligence Artificielle est au coeur de l'actualité. Tantôt adulée, par certains qui voient en elle un moyen de résoudre les problèmes de l'humanité, tantôt décriée, par d'autres qui la voient comme une menace pour l'emploi et la survie de l'espèce, l'Intelligence Artificielle est un sujet qui fait débat. 
C'est dans ce contexte que je me suis mise en quête d'un projet à réaliser où je pourrais mêler à la fois mes connaissances en IA et un sujet qui est très terre à terre : la nourriture. Les premières idées qui me sont venues concernaient la lecture des ingrédients présents sur les emballages alimentaires et la détection de substances dangereuses dans certains plats préparés, cependant de nombreuses applications exitent déjà sur le marché et je ne voyais pas comment je pourrais apporter une plus-value à ce qui existe déjà.
C'est au détour d'une conversation avec mon père que l'idée de Dishdecoder m'est venue. En effet, celui-ci me demandait si je connaissais une application où lorsqu'on lui envoie une photo avec du texte celle-ci est capable de renvoyer une traduction de ce texte dans la langue souhaitée. Bien sur, il existe déjà des applications qui extraient du texte présent sur une image, des applications faisant de la traduction, et même des applications faisant les deux comme par exemple TextGrabber, mais je me suis dit que je pourrais essayer de faire quelque chose de similaire, spécialisé dans la cuisine et plus précisément dans la lecture et la traduction de recettes de cuisine. C'est ainsi que Dishdecoder est né.

## 1.2. Objectifs

L'objectif de Dishdecoder est d'être une application permettant à un utilisateur de prendre en photo une recette de cuisine et d'obtenir une traduction de celle-ci dans la langue de son choix. L'application doit être capable de détecter le texte présent sur l'image, de le reconnaitre et de le traduire. Dans un premier temps, l'application devra être capable de fournir des traductions de recettes de cuisine en anglais et en français. L'application devra également proposer à l'utilisateur de sauvegarder les recettes traduites dans un espace personnel. Enfin, l'application devra permettre à l'administrateur de voir les traductions réalisées afin de pouvoir récolter des données pour améliorer les modèles de traduction.

## 1.3 Approche de la solution

Pour réaliser ce projet, plusieurs composants allaient être nécessaires:
- Les modèles d'intelligence artificielle : celui d'extraction de texte à partir d'image et ceux de traduction
- Les bases de données : celles contenant les datasets pour entrainer les modèles et celle contenant les données de l'application
- La mise en place du back-end de l'application : là où les modèles communiqueront avec l'API
- La réalisation du front-end de l'application : là où l'utilisateur pourra interagir avec l'application qui elle même interéagira avec l'API

## 1.4 Technologies utilisées

Pour réaliser ce projet, j'ai utilisé les technologies suivantes :
- Python : comme langage de programmation
- Pytorch : pour la réalisation des modèles d'intelligence artificielle
- FastAPI : pour la réalisation de l'API
- SQLModel : pour la réalisation de la base de données relationnelle
- Streamlit : pour la réalisation du front-end de l'application
- HuggingFace Hub : pour le stockage des modèles d'intelligence artificielle et des datasets
- Cloudinary : pour le stockage d'images
- PadddleOCR : pour la réalisation du modèle d'extraction de texte à partir d'image
- HuggingFace : pour la réalisation du modèle de traduction
- OpenAI : pour l'utilisation de leur API 
- Playground AI : pour la réalisation de l'égérie de l'application


## 1.5 Schéma de l'application

INSERER ICI LE SCHÉMA DE L'APPLICATION

# II. ETAT DE L'ART

INSERER ICI L'ETAT DE L'ART

# III. DISHDECODER

## 3.1 Le modèle d'OCR

### 3.1.1 Le choix du modèle

Comme nous l'avons vu précédemment, il existe à l'heure actuelle de très nombreux modèles pour réaliser de l'OCR (Optical Character Recognition).

Lors de mon alternance j'ai été en charge de la réalisation d'un modèle d'OCR pour une application de lecture de documents. J'ai donc eu l'occasion de tester plusieurs modèles d'OCR et de voir leurs avantages et leurs inconvénients. Parmi les modèles que j'ai testé, il y avait Tesseract, EasyOCR, TROCR et PaddleOCR. 

Tesseract, qui est sans doute le plus connu, a été développé à l'origine par Hewlett-Packard Labs et désormais maintenu par Google. Tesseract est un modèle open source et est de base fait pour être utilisé en language C++ mais il existe des wrappers pour l'utiliser en Python, comme par exemple Pytesseract. Cependant, après test, Tesseract n'est pas le modèle le plus performant, notamment sur les images avec du bruit. De plus, il n'est pas toujours simple à configurer selon l'utilisation que l'on souhaite en faire et aussi son implémentation en Python peut se réveler très compliquée en raison d'incompatibilités avec d'autres librairies. C'est pourquoi, lors de mon alternance, j'ai décidé de ne pas utiliser Tesseract.

EasyOCR est quant à lui connu pour être une librairie open-source, dévelopée par JaidedAi, qui prend en charge plus de 70 langues et qui est compatible avec de nombreux langages de programmation dont Python, C#, Java. En plus de cela, EasyOCR est très rapide. Par ailleurs, comme son nom l’indique EasyOCR est facile à utiliser. Il suffit de trois lignes, dont l'importation, pour qu’il lise une image. Cependant, j'avais remarqué que les sorties de celui-ci n’étaient pas toujours exactes. Que ce soit pour la lecture des chiffres présents sur les documents ou la lecture des différentes zones de texte, de nombreuses erreurs étaient réalisées à chaque lecture : confusion entre deux caractères, oubli d’espace, ajout de caractères etc. Malgré divers réglages dans les paramètres, les résultats restaient toujours brouillons.

TROCR (Tokenization, Recognizing, and OCR) est également une librairie open-source, datant de 2017, développée par Microsoft et implémentée
dans Transformers, la librairie open-source d’Hugging Face. TROCR combine les étapes d’OCR pour extraire le texte des images, et de tokenisation pour convertir le texte en une séquence de tokens utilisable par des modèles de traitement du langage naturel. Contrairement à EasyOCR, le traitement des images via TROCR est beaucoup plus long. Malgré cela j'ai quand même testé TROCR, avec le modèle base-printed qui est censé être le modèle le plus adapté à la lecture de caractères d’imprimerie. En effet, le modèle base-printed a été fine-tuné sur le dataset SROIE qui est constitué d’un millier de tickets de caisse. Après de nombreux tests, les résultats obtenus avec TROCR étaient généralement meilleurs que ceux obtenus avec EasyOCR. Toutefois, TROCR donnait exclusivement des sorties en majuscules, la ponctuation était approximative, les espaces pas toujours respectés et surtout, le temps d’inférence du modèle était beaucoup trop important. TROCR doit être réservé à un usage sur GPU, ce qui n'était pas possible lors de mon altenance et qui ne l'est toujours pas aujourd'hui avec Dishdecoder.

PaddleOCR est, comme pour les trois OCR précédents, une librairie open-source. Celle-ci est développée par PaddlePaddle (PArallel Distributed Deep LEarning), une entreprise chinoise. Elle utilise des algorithmes de pointe pour détecter, localiser et reconnaître des caractères dans des images, et est disponible dans de
nombreuses langues. L’utilisation de PaddleOCR ressemble à celle d’EasyOCR par sa facilité. Là aussi, la librairie est compatible avec plusieurs langages de programmation tels que Python, C++ et Java, ce qui facilite son intégration dans différents projets.
L’architecture de deep-learning utilisée derrière PaddleOCR est un CRNN : Convolutional Recurrent Neural Network. Le CRNN est un réseau de neurones profonds qui combine à la fois un CNN (Convolutional Neural Network) et un RNN (Recurrent Neural Network). 
Dans un CRNN, la couche de convolution, CNN, est utilisée pour extraire des caractéristiques pertinentes des images. Ensuite, la couche RNN est utilisée pour analyser et traiter ces caractéristiques dans un contexte de séquence. Les sorties de la couche de convolution sont
transformées en séquences d'entrée pour le RNN, qui utilise sa mémoire interne pour prendre en compte les caractéristiques précédentes tout en analysant la séquence actuelle. Cela permet au CRNN de mieux comprendre la structure de l'image et d'extraire des informations textuelles
pertinentes.
Concernant PaddlePaddle, il s’agit de la première plateforme open-source indépendante de deep learning en Chine. Elle est développée par l’entreprise Baidu. PaddlePaddle est plus ou moins l’équivalent chinois de TensorFlow. La plateforme PaddlePaddle est réputée pour sa rapidité d’inférence, sa capacité à traiter des volumes de données massifs et son large écosystème de modules et d'outils intégrés. La plateforme est largement utilisée dans différents domaines, notamment l'industrie, le transport, l’agriculture et les services publics. 
Dès la première utilisation de PaddleOCR, avec le modèle de base en langue française et latine, j’ai  pu observer que les sorties données étaient bien meilleures que celles d’EasyOCR. Certains points étaient malgré tout perfectibles : les espaces entre les caractères n’étaient souvent pas retranscrits et il y avait parfois de la confusion entre certains caractères. Cependant, il était mis en avant sur le GitHub de PaddleOCR qu'avec du finetuning, les résultats pouvaient être nettement améliorés. 

Voici un exemple de test que j'ai réalisé lors de mon alternance sur EasyOCR, TROCR et PaddleOCR :

INSERER ICI LES IMAGES MR OU MME BERTIN


Comme nous pouvons l'observer, les résultats obtenus par TROCR et PaddleOCR sont bien concluants que ceux obtenus par EasyOCR. 

C'est donc pour ces diverses raisons que lors de mon alternance j'ai décidé de finetuner PaddleOCR. Les bons résultats obtenus font que mon modèle finetuné est désormais le modèle utilisé par mon entreprise d'alternance lorsqu'il s'agit de faire de l'OCR.

Ne pouvant réutiliser le modèle et le dataset d'entraînement de mon alternance pour Dishdecoder, j'ai choisi de reconstituer un nouveau dataset d'entraînement et de finetuner un modèle de PaddleOCR sur ce nouveau dataset.

### 3.1.2 Les données nécessaires à l'entraînement du modèle

Avant de savoir quelles données sont nécessaires pour finetuner un modèle de PaddleOCR, il est important de comprendre comment fonctionne PaddleOCR.
En effet, il n'existe pas qu'un seul modèle PaddleOCR qui sait gérer toutes les langues. Il existe un modèle par langue. Par exemple, il existe un modèle pour la langue française, un modèle pour la langue anglaise, un modèle pour la langue chinoise etc. Il y a également plusieurs versions, il y a par exemple les modèle PP-OCRv2 de l'ancienne génération et les PP-OCRv3 qui sont les plus récents et les plus performants. A vitesse égale, selon les langues, les modèles PP-OCRv3 sont entre 5% et 11% plus précis (accuracy) que les modèles PP-OCRv2.
Par ailleurs, PaddleOCR propose d’utiliser trois types de modèles différents qui peuvent être combinés lors de la lecture d’une image. Il y a un modèle de reconnaissance de caractères (recognition model aussi appelé rec), un modèle de détection de texte (detection model aussi appelé det) et un modèle de classification d’angle du texte (classification model aussi appelé cls). Dans mon cas d’usage, je n’avais pas besoin de finetuner mon modèle pour qu’il soit plus performant dans la détection de texte ou dans la reconnaissance de l’orientation du texte. Je souhaitais uniquement avoir un modèle plus performant sur la reconnaissance de caractères, c’était donc un recognition model que j’allais finetuner. Par ailleurs, plutôt que de finetuner le modèle de reconnaissance français, french_mobile_v2.0_rec, j’ai choisi de finetuner le modèle de reconnaissance latin appelé
latin_PP-OCRv3_rec. En effet, le modèle latin fait partie des modèles de 3ème génération, ce qui implique de meilleures performances.

Il est recommandé, sur le GitHub de PaddleOCR, d'utiliser plus de 5000 images lors du finetuning d'un modèle de reconnaissance. 

D'experience, je sais également que plus le dataset comprend des images diverses et variées et plus le modèle finetuné est performant. Il était donc nécessaires que je receuille des images avec différentes tailles, différentes polices de caractères, différents types de fonds, différentes couleurs, différentes longueur de texte, des majuscules, des minuscules, des chiffres, des caractères spéciaux etc.

Souhaitant également que mon OCR soit performant sur du français comme sur de l'anglais, j'ai décidé de récolter des images en français et en anglais.

Pour finetuner un modèle de reconnaissance PaddleOCR, le dataset doit être constitué de la manière suivante : il doit y avoit des images et un fichier texte. Le fichier texte doit contenir deux éléments pour chaque image: le chemin de sa localisation avec le nom donné à l'image et le texte présent sur l'image. Le chemin de l'image et le texte présent sur l'image doivent être séparés par une tabulation. 

### 3.1.3 La création du dataset

N'ayant trouvé aucun dataset pertinent répondant à mes besoins, j'ai décidé, comme lors de mon alternance, de créer mon propre dataset.
Pour cela, aucun outil de labellisation n'est nécessaire. 
En effet, le seul outil dont j'avais besoin était un outil de capture d'écran. J'ai donc utilisé l'outil de capture d'écran intégré à mon ordinateur, celui de Ubuntu.
Afin de constitué mon dataset, j'ai été sur de nombreux sites internet dont : 
- Amazon.com où j'ai recherché différents ouvrages en français et en anglais. J'y ai capturé des images de titres de livres, de quatrième de couverture, de table des matières...
- Brest.fr où j'ai pu trouver certains extraits de magazines, des infographies, des affiches, des publicités...
- Des sites internet d'archive où sont scannés d'anciens numéros de journaux actuels comme Le Monde ou Le Canard Enchaîné, où j'ai pu capturer des images de titres d'articles etc.
- Des sites internet spécialisés dans les journaux et annuaires anciens pour trouver des polices d'écriture plus rares.
- Des sites internet de restaurants dont Restaurantguru.com où j'ai pu capturer des images à partir des différents menus.

J'ai récolté en tout 1285 images. Pour chaque image, j'ai recensé son chemin avec son nom ainsi que le texte présent dans cette même image, le tout consigné dans un fichier texte.

### 3.1.4 Le prétraitement des données

Parmi les images récupérées, j'en ai sélectionné 565 pour l'entraînement et 720 pour la validation.
Afin de rendre mon dataset plus robuste, j'ai fait de la data augmentation sur mon dataset d'entrainement. 
Pour cela, j'ai adapté le code du projet Straug présent sur le GitHub de Roatenzia à ce dont j’avais besoin.
J’ai choisi d’appliquer à mes images les effets suivants : GaussianNoise, SpeckleNoise, ImpulseNoise, MotionBlur, DefocusBlur, Shadow, Rain. 

INSRER IMAGE EXEMPLE

Une fois les nouvelles images générées, 17 nouvelles images en sortie pour 1 image en entrée, soit 9605 nouvelles images, j’ai pu les labelliser dans mon fichier texte d’entraînement et les déplacer dans mon dossier comprenant toutes les images.
Ainsi le dataset final pour ce finetuning comprenait 10170 images pour l’entraînement et 720 images pour la validation.
L'ensemble du dataset a été mis dans un dossier train_data. Dans train_data il y a un dossier data où sont stockées toutes les images du dataset et deux fichiers .txt : dataset_IMG_train_REDO.txt et dataset_IMG_val_REDO.txt . Comme leurs noms le laisse supposer, le fichier dataset_IMG_train_REDO.txt contient les chemins ainsi que le texte contenu sur les images d'entraînement et le fichier dataset_IMG_val_REDO.txt contient les chemins ainsi que le texte contenu sur les images de validation.

### 3.1.5 Le stockage du dataset

J'aurais souhaité stocker mon dataset sur le Hub de Hugging Face, mais cela n'a pas pu être fait car un repository sur HuggingFace ne peut pas contenir plus de 10000 éléments. J'ai donc stocké mon dataset dans un dossier sur mon ordinateur. 

### 3.1.6 L'entrainement du modèle

La première étape avant de lancer l'entraînement, fut de cloner le repository GitHub de PaddleOCR sur mon ordinateur.
```$ git clone https://github.com/PaddlePaddle/PaddleOCR.git```
Une fois le projet cloné, il fallait, à l’intérieur du dossier principal, créer un dossier pretrain_models.
En effet, lorsque l’on finetune un modèle, il nous faut obligatoirement un modèle de base, modèle auquel on va apporter des modifications avec le finetuning. Pour les raisons expliquées plus haut, j’avais choisi le modèle latin_PP-OCRv3_rec. Il fallait alors télécharger ce modèle depuis le GitHub de PaddleOCR et l’extraire dans le dossier pretrain_models.
Après cela, à la racine du dossier principal PaddleOCR, au même niveau que pour le dossier pretrain_models, il fallait copier le dossier train_data comprenant le dataset.
L’étape suivante était de retourner dans le dossier principal PaddleOCR, puis d’aller dans le dossier configs, puis rec, puis PP-OCRv3, puis multi_language, puis de faire une copie du fichier latin_PPOCRv3_rec.yml en le renommant. C’est dans ce fichier de configuration qu’interviennent les
modifications de chemins afin de permettre à PaddleOCR d’utiliser le dataset contenu dans train_data lors de l’entraînement. Ce fichier de configuration permet également de spécifier bon nombre de paramètres : le chemin du dictionnaire à utiliser, la prise en compte des espaces, mais
également le chemin du modèle pré-entraîné à utiliser etc.
Une fois toutes ces étapes réalisées, j'ai décidé de créer un nouvel environnement conda dédié à l'entrainement de mon modèle. Pour cela, j'ai utilisé la commande suivante : 
```$ conda create --name paddle-training python=3.10```
J'ai ensuite activé cet environnement avec la commande suivante : 
```$ conda activate paddle-training```
Après cela, afin d'utiliser la version GPU pour l'entraînement du modèle, j'ai fait la commande suivante qui est recommandée sur le site de Paddlepaddle: 
```python -m pip install paddlepaddle-gpu==2.4.2.post117 -f https://www.paddlepaddle.org.cn/whl/linux/mkl/avx/stable.html```
Enfin j'ai installé, en prenant bien soin d'être à ce moment-là dans le dossier PaddleOCR, les dépendances nécessaires à l'entraînement du modèle avec la commande suivante : 
```$ pip install -r requirements.txt```
Une fois toutes ces étapes réalisées, tout en étant toujours bien à la racine du dossier PaddleOCR, j'ai pu lancer l'entraînement de mon modèle avec la commande suivante : 
```$ python3 -m paddle.distributed.launch --gpus '0'  tools/train.py -c configs/rec/PP-OCRv3/multi_language/latin_PP-OCRv3_rec_4_finetuning.yml```

L'entraînement, de 200 epochs, a été lancé à 12h49 et s'est terminé à 23h18, soit un peu plus de 10h d'entraînement.
Comme spécifié dans le fichier de configuration, les poids du modèle finetuné ayant la meilleure précision (accuracy) ainsi que ses différents fichiers (fichier de configuartaion, fichier qui repertorie tous les logs d'entraînement, poids du modèle actualisés à chaque epoch...) ont été stockés dans le dossier ./output/v3_latin_mobile_FINETUNING_1

Vis-à-vis de la méthode d'entraînement, Le finetuning est souvent considéré comme une forme d'entraînement supervisé car il nécessite des annotations étiquetées pour guider le processus d'apprentissage. Cependant, on peut également le considérer comme une approche semi-supervisée, car le modèle de base pré-entraîné apporte une connaissance préalable supervisée qui est ensuite améliorée et affinée grâce aux données supplémentaires annotées que nous lui fournissons. 

### 3.1.7 Configuration des hyperparamètres du modèle

Lors de ce premier finetuning, j'ai choisi de modifier les hyperparamètres suivants :
- le batch size, que j'ai mis à 16
- le nombre d'epochs, que j'ai mis à 200

Etant donné qu'après ce premier entraînement j'ai eu l'occasion d'avoir accès à un GPU plus puissant, j'ai décidé de refaire un finetuning avec cette fois-ci un batch size de 128 et un nombre d'epochs de 200.
Ensuite, j'ai décidé de faire un troisième finetuning avec un batch size de 64 et un nombre d'epochs de 200.
Puis, j'ai décidé de faire un quatrième finetuning avec un batch size de 64 et un nombre d'epochs de 750.
Enfin, j'ai décidé de faire un cinquième finetuning avec un batch size de 32 et un nombre d'epochs de 200.

### 3.1.8 Comparaison des modèles et choix du meilleur 

N'ayant pas utilisé d'outil de monitoring pour les entraînements de mon modèle, je n'ai pas pu avoir accès à des graphiques représentant l'évolution de l'accuracy au cours des entraînements. Cependant, j'ai pu avoir accès à ces informations dans le fichier de log de chaque entraînement. 
Par ailleurs, à la fin de chaque entraînement, PaddleOCR indique qu'elle fut l'epoch où a été calculée la meilleure accuracy sur le dataset de validation. Pour PaddleOCR l'accuracy est la métrique utilisée pour évaluer la performance du modèle.

Voici les résultats obtenus pour chaque entraînement :

INSERER ICI LES RESULTATS OBTENUS POUR CHAQUE ENTRAINEMENT

Comme nous pouvons le constater, le modèle ayant la meilleure accuracy est le premier à avoir été entraîné. C'est donc celui-ci que nous allons utiliser pour la suite de ce projet.

Cependant, le modèle obtenu après l'entraînement n'est pas utilisable en l'état. Après entraînement tous les modèles PaddleOCR sont composés de trois fichiers : un fichier en .pdopt, un fichier en .pdparams et un fichier en .states. Dans notre cas ces trois fichiers sont stockés dans le dossier ./output/v3_latin_mobile_FINETUNING_1/best_accuracy. Afin de pouvoir utiliser ce modèle, il a donc fallu le convertir en un modèle utilisable par PaddleOCR.

 Pour cela, j'ai éxecuté la commande suivante : 
```$ python3 tools/export_model.py -c configs/rec/PP-OCRv3/multi_language/latin_PP-OCRv3_rec_4_finetuning.yml -o Global.pretrained_model=./output/v3_latin_mobile_FINETUNING_1/best_accuracy Global.save_inference_dir=./inference```

Une fois cette commande exécutée, le modèle fut converti et stocké dans le dossier inference. 
Le modèle est alors composé de trois nouveaux fichiers : inference.pdiparams, qui est le fichier de paramètres du modèle, inference.pdiparams.info, qui est le fichier d'informations du modèle et inference.pdmodel, qui est le fichier de programme du modèle en lui-même.
Afin de facilité l'utilisation du nouveau modèle, je crée un dossier ocr_model et j'ai ajouté dans ce dossier les trois fichiers d'inférence convertis, le fichier de configuration du modèle en .yml ainsi que le dictionnaire utilisé en .txt.

INSERER ICI UNE IMAGE DU DOSSIER OCR_MODEL

### 3.1.9 Le stockage du modèle

Afin de pouvoir utiliser ce modèle dans ce projet et dans d'autres à venir, j'ai décidé de le stocker sur le Hub Hugging Face. Pour cela, j'ai créé un nouveau repository sur mon compte Hugging Face et j'ai ajouté les fichiers du modèle dans ce repository.
Le modèle est donc maintenant disponible à l'adresse suivante : https://huggingface.co/PaulineSanchez/PaddleOCR_ft

INSERER ICI UNE IMAGE DU HUB HUGGING FACE AVEC LE MODELE DANS LE REPOSITORY

# 3.2 Les modèles de traduction

### 3.2.1 Le choix des modèles

Comme pour l'OCR, une multitude de modèles de traduction existe. Depuis quelques années, les entreprises utilisent de plus en plus les modèles de traduction neuronaux. Ces modèles sont des modèles de traduction automatique qui utilisent des réseaux de neurones artificiels. Ils sont capables de traduire des textes d'une langue à une autre en s'appuyant d'avantage sur le contexte. Parmi ces architectures, on retrouve notamment les RNN et les LSTM.
Les réseaux de neurones récurrents (RNN) sont des modèles conçus pour traiter des séquences de texte en entrée et/ou générer des séquences de texte en sortie. Leur caractéristique principale est leur capacité à conserver une forme de mémoire grâce à des boucles récurrentes au sein de leurs couches cachées. Cela permet à l'information contextuelle de circuler à travers le réseau, de sorte que les sorties précédentes puissent influencer les calculs effectués à chaque étape temporelle.

Cette capacité à mémoriser les informations contextuelles est similaire à notre façon de lire. Lorsque nous lisons, nous retenons les éléments importants des mots et des phrases précédentes pour les utiliser comme référence et comprendre le sens des nouveaux mots et des nouvelles phrases.
Les LSTM (Long Short-Term Memory) sont une variante des RNN. En effet, bien que les RNN soient capables de conserver des informations sur de courtes périodes de temps, ils ont du mal à conserver des informations sur de longues périodes de temps. C'est ce que l'on appelle le problème de la disparition du gradient. Les LSTM peuvent donc être considérés comme des RNN améliorés. Les LSTM sont composés de trois portes : la porte d'oubli, la porte d'entrée et la porte de sortie. La porte d'oubli permet de décider quelles informations doivent être oubliées ou conservées. La porte d'entrée permet de décider quelles nouvelles informations doivent être stockées dans la cellule d'état. Enfin, la porte de sortie permet de décider quelles informations doivent être renvoyées en sortie. Ainsi, grâce à leur structure spécifique, les LSTM sont capables de capturer et de retenir des informations pertinentes sur une longue séquence, permettant ainsi de conserver la relation entre les mots à travers différentes parties de la séquence. Ils sont donc particulièrement adaptés à la traduction de textes longs. 

Cependant, une révolution majeure dans le domaine de la traduction automatique est survenue avec l'avènement des Transformers. Contrairement aux LSTM, qui sont basés sur des architectures récurrentes, les Transformers utilisent une approche basée sur l'attention pour capturer les relations entre les mots. Cette architecture révolutionnaire a permis de surmonter les limitations des LSTM en termes de gestion des dépendances à long terme et de parallélisme. Les Transformers se sont imposés comme une avancée majeure dans la traduction automatique en raison de leur capacité à traiter efficacement les séquences de texte et à capturer les dépendances contextuelles sur de plus longues distances. Grâce à leur mécanisme d'attention, les Transformers peuvent attribuer des poids différents aux mots en fonction de leur importance, ce qui leur permet de comprendre le contexte global de la phrase et d'effectuer des traductions plus précises et cohérentes.

C'est pourquoi, j'ai donc décidé d'utiliser des modèles de traduction neuronaux basés sur les Transformers. Afin de choisir quels modèles j'allais utiliser et finetuner, j'ai été lire le cours sur la traduction de Hugging Face. Plusieurs modèles étaient proposés, comme par exemple T5, MarianMT, Bart...
T5 (Text-To-Text Transfer Transformer) est un modèle de traitement du langage naturel développé par Google. Il s'agit d'un modèle basé sur les Transformers qui peut être utilisé pour diverses tâches, dont la traduction. 
Bart (Bidirectional and AutoRegressive Transformers") est un modèle développé par Facebook AI. Il est lui aussi basé sur les Transformers et a été spécifiquement conçu pour la génération de texte. 
MarianMT est un projet open-source qui se concentre sur la traduction automatique neuronale. Il s'agit d'une implémentation basées sur les Transformers. MarianMT utilise le même modèle de base que Bart avec quelques modifications.

Souhaitant utiliser des modèles spécialisés dans les tâches de traduction neuronaux basés sur les Transformers, j'ai donc décidé de finetuner des modèles basés sur MarianMT.

### 3.2.2 Les données nécessaires à l'entraînement des modèles

Souhait faire de la traduction de l'anglais vers le français et du français vers l'anglais, j'ai choisi de finetuner les deux modèles suivants :
