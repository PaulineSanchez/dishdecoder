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
    Introduction
    1. Contexte historique
    2. Les fondamentaux des Transformers
    3. Architecture des Transformers
    4. Domaines d'applications des Transformers
    5. Avancées récentes et défis
    Conclusion

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
        3.5.4 L'interaction avec le back-end
    
    3.6 L'organisation du projet
        3.6.1 Le Trello (GANT ?)
        3.6.2 Le Kanban
        3.6.2 Le GitHub

IV. CONCLUSION

    4.1 La réalisation du projet
    4.2 Les difficultés rencontrées
    4.3 Les améliorations et les perspectives d'évolution
    

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

Introduction :

Au cours des dernières années, les transformers ont révolutionné le domaine de l'apprentissage automatique et du traitement du langage naturel. Ces architectures neurales puissantes ont ouvert de nouvelles perspectives en matière de modélisation des séquences, avec des performances impressionnantes dans des tâches de NLP telles que la traduction automatique, la génération de texte ou encore la compréhension du langage.

Les transformers ont émergé en 2017 avec la publication de l'article "Attention is All You Need" par Vaswani et al. Dès lors, ils ont gagné en popularité et sont devenus la référence en matière de modélisation de séquences. Ils se sont avérés particulièrement efficaces pour traiter des tâches impliquant des relations à longue distance entre deux séquences et une compréhension contextuelle approfondie.

Contrairement aux approches précédentes basées sur les réseaux de neurones récurrents (RNN) ou les réseaux de neurones convolutifs (CNN), les transformers se distinguent par l'utilisation d'un mécanisme d'attention. Ce mécanisme permet aux transformers de prendre en compte les dépendances contextuelles à travers toute la séquence d'entrée, sans la nécessité d'une propagation séquentielle de l'information.

Dans les transformers, l'attention permet de calculer des pondérations sur les différentes parties de la séquence d'entrée, en mettant l'accent sur les éléments les plus pertinents pour la tâche en cours. Cela permet aux transformers de capturer les relations à long terme et de modéliser des dépendances complexes, ce qui en fait des modèles très adaptés aux tâches de compréhension et de génération de séquences.

Dans cet état de l'art, nous explorerons en détail les principes fondamentaux des transformers, leur architecture, ainsi que les avancées récentes dans ce domaine. Nous mettrons en évidence les performances remarquables des transformers dans des tâches clés telles que la traduction automatique et la génération de texte. Nous examinerons également les différentes variantes de transformers qui ont été proposées pour améliorer les performances et répondre à des défis spécifiques. Nous explorerons également l'évolution des transformers et mettrons en évidence leur impact significatif sur le traitement du langage naturel et d'autres tâches de modélisation de séquences.

1. Contexte historique :

Depuis quelques années, les entreprises utilisent de plus en plus les modèles de traduction neuronaux. Ces modèles sont des modèles de traduction automatique qui utilisent des réseaux de neurones artificiels. Ils sont capables de traduire des textes d'une langue à une autre en s'appuyant d'avantage sur le contexte. Parmi ces architectures, on retrouve notamment les RNN et les LSTM.

Les réseaux de neurones récurrents (RNN) sont des modèles conçus pour traiter des séquences de texte en entrée et/ou générer des séquences de texte en sortie. Leur caractéristique principale est leur capacité à conserver une forme de mémoire grâce à des boucles récurrentes au sein de leurs couches cachées. Cela permet à l'information contextuelle de circuler à travers le réseau, de sorte que les sorties précédentes puissent influencer les calculs effectués à chaque étape temporelle.
Cette capacité à mémoriser les informations contextuelles est similaire à notre façon de lire. Lorsque nous lisons, nous retenons les éléments importants des mots et des phrases précédentes pour les utiliser comme référence et comprendre le sens des nouveaux mots et des nouvelles phrases.

Les LSTM (Long Short-Term Memory) sont une variante des RNN. En effet, bien que les RNN soient capables de conserver des informations sur de courtes périodes de temps, ils ont du mal à conserver des informations sur de longues périodes de temps. C'est ce que l'on appelle le problème de la disparition du gradient. Les LSTM peuvent donc être considérés comme des RNN améliorés. Les LSTM sont composés de trois portes : la porte d'oubli, la porte d'entrée et la porte de sortie. La porte d'oubli permet de décider quelles informations doivent être oubliées ou conservées. La porte d'entrée permet de décider quelles nouvelles informations doivent être stockées dans la cellule d'état. Enfin, la porte de sortie permet de décider quelles informations doivent être renvoyées en sortie. Ainsi, grâce à leur structure spécifique, les LSTM sont capables de capturer et de retenir des informations pertinentes sur une longue séquence, permettant ainsi de conserver la relation entre les mots à travers différentes parties de la séquence. Ils sont donc particulièrement adaptés à la traduction de textes longs. 

Cependant, une révolution majeure dans le domaine de la traduction automatique est survenue en 2017 avec l'avènement des Transformers. Contrairement aux LSTM, qui sont basés sur des architectures récurrentes, les Transformers utilisent une approche basée sur l'attention pour capturer les relations entre les mots. Cette architecture révolutionnaire a permis de surmonter les limitations des LSTM en termes de gestion des dépendances à long terme et de parallélisme. Les Transformers se sont imposés comme une avancée majeure dans la traduction automatique en raison de leur capacité à traiter efficacement les séquences de texte et à capturer les dépendances contextuelles sur de plus longues distances. Grâce à leur mécanisme d'attention, les Transformers peuvent attribuer des poids différents aux mots en fonction de leur importance, ce qui leur permet de comprendre le contexte global de la phrase et d'effectuer des traductions plus précises et cohérentes. Ce mécanisme a été une avancée majeure dans le domaine du traitement du langage naturel et a permis d'obtenir des performances significativement meilleures dans des tâches telles que la traduction automatique.

Depuis la publication de l'article fondateur, de nombreuses variantes et améliorations des transformers ont été proposées, telles que les transformers à plusieurs têtes, les transformers récurrents, les transformers pré-entraînés et les transformers axés sur la vision. Ces avancées ont élargi le champ d'application des transformers à différents domaines et ont contribué à leur popularité croissante.

Dans la prochaine section, nous examinerons en détail les fondements des transformers, en explorant leur architecture et leur fonctionnement. Nous mettrons également en évidence les applications les plus courantes des transformers dans le domaine du traitement du langage naturel et au-delà.

2. Les fondements des Transformers :

Les transformers reposent sur deux principaux concepts fondamentaux : le mécanisme d'attention et les couches d'encodeur-décodeur. Ces éléments clés sont à la base de l'architecture des transformers et contribuent à leur puissance et à leur efficacité dans la modélisation des séquences.

Comme nous l'avons vu précédemment, le méchanisme d'attention est l'élément novateur central pour les transformers. En effet, cela permet aux transformers de calculer des pondérations pour chaque élément de la séquence, en mettant l'accent sur les parties les plus pertinentes pour la tâche en cours. Cela diffère des approches séquentielles traditionnelles où l'information est propagée de manière linéaire à travers la séquence.

Le mécanisme d'attention des transformers se compose de trois éléments clés : les requêtes (queries), les clés (keys) et les valeurs (values). Les requêtes représentent les éléments que le modèle souhaite encoder ou prédire, les clés représentent les éléments de la séquence d'entrée et les valeurs représentent les informations associées à chaque élément de la séquence. Les poids d'attention sont calculés en comparant les similarités entre les requêtes et les clés, puis en utilisant ces poids pour pondérer les valeurs.

Une caractéristique importante des transformers est qu'ils peuvent calculer les poids d'attention pour tous les éléments de la séquence en parallèle. Cela permet des calculs plus rapides et efficaces par rapport aux approches séquentielles. De plus, les transformers utilisent des mécanismes d'attention multiples, appelés "têtes d'attention", qui permettent de capturer différents types de relations et d'informations contextuelles.

Les transformers ont également introduit l'idée de l'apprentissage par transfert, où les modèles pré-entraînés sur de grandes quantités de données peuvent être adaptés à des tâches spécifiques après avoir subi un léger ajustement (finetuning). Cela a permis de tirer profit des modèles pré-entraînés sur de vastes corpus de texte et a grandement contribué aux excellentes performances des transformers dans diverses tâches de NLP.

L'architecture des transformers est basée sur des couches d'encodeur-décodeur. L'encodeur est responsable de la compréhension de la séquence d'entrée, tandis que le décodeur génère la séquence de sortie. Chaque couche d'encodeur et de décodeur est composée de plusieurs sous-modules, tels que les couches d'attention et les réseaux de neurones entièrement connectés. Cette architecture d'encodeur-décodeur permet une compréhension complète des séquences d'entrée et une génération précise des séquences de sortie.

Dans la prochaine section, nous allons explorer en détail l'architecture des transformers.

3. Architecture des Transformers :

L'architecture des transformers est caractérisée par une structure en couches qui permet de capturer les dépendances à longue distance dans les séquences. Chaque couche du transformer est composée de deux principaux modules : l'encodeur et le décodeur.

L'encodeur est responsable de la représentation initiale des données d'entrée, tandis que le décodeur génère les prédictions à partir de cette représentation encodée. Les transformers sont généralement utilisés dans des tâches de génération de séquences, telles que la traduction automatique ou la génération de texte, où l'entrée et la sortie sont des séquences de symboles.

Chaque module d'encodeur et de décodeur est lui-même composé de plusieurs couches d'attention, de couches de transformation positionnelle et de couches de feed-forward. La combinaison de ces différentes couches permet aux transformers de modéliser les relations contextuelles complexes et de générer des prédictions précises.

Chaque couche de l'encodeur et du décodeur contient des sous-couches résiduelles et des couches de normalisation. Les sous-couches résiduelles permettent de conserver les informations non altérées à travers les différentes transformations, facilitant ainsi la propagation du gradient lors de l'entraînement du modèle. Les couches de normalisation garantissent une stabilité dans l'apprentissage en normalisant les activations à chaque étape.

Les couches d'attention sont le cœur de l'architecture des transformers. Elles permettent aux modèles de calculer des pondérations sur les différentes parties de la séquence d'entrée, en mettant l'accent sur les éléments les plus pertinents. Les couches d'attention fonctionnent en calculant des scores d'attention entre chaque paire d'éléments dans la séquence, puis en les pondérant pour obtenir une représentation pondérée. Cette représentation pondérée est ensuite utilisée pour calculer les sorties de chaque couche.

Les couches de transformation positionnelle sont utilisées pour encoder l'information sur l'ordre séquentiel des éléments. Elles ajoutent des informations sur la position relative des éléments, permettant ainsi aux transformers de prendre en compte l'ordre séquentiel lors de la génération des prédictions. Cela est particulièrement important dans les tâches de génération de séquences où l'ordre des symboles est essentiel.

Les couches de feed-forward sont des couches entièrement connectées qui introduisent de la non-linéarité dans le modèle. Elles permettent de transformer les représentations des éléments en utilisant des opérations linéaires suivies d'une fonction d'activation. Ces transformations non linéaires aident à capturer des relations complexes et à améliorer la capacité de modélisation des transformers.

Les transformers utilisent également des mécanismes de "masking" pour s'assurer que les prédictions ne dépendent que des éléments précédents de la séquence de sortie lors de la génération de chaque élément. Cela permet d'éviter toute dépendance vis-à-vis des éléments futurs, ce qui est essentiel pour les tâches de prédiction et de génération séquentielles.

Dans les architectures des transformers, l'information se propage de manière parallèle plutôt que séquentielle. Chaque couche traite l'ensemble de la séquence en parallèle, ce qui permet d'exploiter efficacement les capacités de calcul parallèle des processeurs modernes et d'accélérer l'entraînement et l'inférence.

L'architecture des transformers peut être étendue pour inclure des variantes telles que les transformers à plusieurs têtes. Les transformers à plusieurs têtes permettent de calculer différentes pondérations d'attention pour différentes parties de l'entrée, ce qui permet au modèle de mettre l'accent sur différentes relations et caractéristiques. Cela améliore la capacité du modèle à capturer des informations spécifiques et à modéliser des tâches complexes.

Dans la section suivante, nous allons mettre en lumière les utilisations de transformers les plus populaires.

4. Domaines d'application des Transformers :

Les transformers ont été largement utilisés dans divers domaines pour des tâches de modélisation de séquences. Leur capacité à capturer les dépendances à longue distance et à générer des prédictions précises en fait une architecture polyvalente et performante. Voici quelques-unes des applications les plus courantes des transformers :

1. La traduction automatique : Les transformers ont révolutionné le domaine de la traduction automatique en offrant des performances significativement meilleures par rapport aux approches précédentes. Grâce à leur capacité à modéliser les relations contextuelles à travers toute la séquence, les transformers sont capables de capturer les subtilités du langage et de produire des traductions plus précises et naturelles.

2. Résumé automatique : Les transformers sont également utilisés pour générer des résumés automatiques de textes. En modélisant les relations entre les phrases et en identifiant les informations clés, les transformers sont capables de condenser de longs textes en résumés concis et clairs.

3. Recherche d'informations : Les transformers sont employés dans les moteurs de recherche pour améliorer la pertinence des résultats. En analysant les requêtes des utilisateurs et en évaluant la similarité avec les documents, les transformers peuvent effectuer une recherche plus précise et fournir des résultats mieux adaptés.

4. Chatbots et assistants virtuels : Les transformers sont utilisés pour créer des chatbots et des assistants virtuels capables d'interagir avec les utilisateurs de manière naturelle et fluide. Grâce à leur capacité à comprendre et à générer du langage, les transformers permettent des conversations plus naturelles et plus efficaces.

5. Reconnaissance automatique de la parole : Les transformers ont également été appliqués avec succès dans la reconnaissance automatique de la parole. En modélisant les séquences audio et en capturant les relations temporelles, les transformers peuvent convertir des enregistrements audio en texte avec une grande précision.

6. Traitement du langage naturel : Les transformers sont utilisés pour diverses tâches de traitement du langage naturel telles que la classification de texte, la génération de texte, la réponse aux questions, la détection d'entités nommées, etc. Leur capacité à capturer les dépendances contextuelles leur permet de comprendre et de générer du langage de manière plus précise. Actuellement, les transformers sont la méthode la plus performante pour la plupart des tâches de traitement du langage naturel.

7. Vision par ordinateur : Les transformers ont également été adaptés au domaine de la vision par ordinateur, où ils ont montré des résultats prometteurs. En utilisant des architectures basées sur les transformers, il est possible de capturer les relations spatiales entre les éléments d'une image ou d'une vidéo, permettant ainsi des tâches telles que la classification d'images, la détection d'objets et la segmentation sémantique.

On remarque à travers ces exemples que les transformers ont été utilisés avec succès dans de nombreux domaines pour des tâches de modélisation de séquences. Leur capacité à capturer les dépendances à longue distance et à générer des prédictions précises en fait une architecture puissante et polyvalente. Les transformers continuent d'ouvrir de nouvelles perspectives et d'améliorer les performances dans diverses applications.

5. Avancées récentes et défis

Récemment, les transformers ont connu de nombreuses avancées qui ont contribué à améliorer leurs performances et à étendre leur utilisation. Voici quelques-unes des avancées les plus caractéristiques :

- Améliorations de l'attention : Les mécanismes d'attention ont été améliorés pour prendre en compte des aspects tels que l'attention contextuelle et l'attention multi-modale. Ces améliorations permettent aux transformers de mieux modéliser les relations complexes entre les éléments de séquence et d'intégrer des informations provenant de différents domaines, comme le langage et la vision.

- Adaptation aux domaines spécifiques : Les transformers ont été adaptés à des domaines spécifiques en utilisant des techniques telles que le finetuning. Cela permet d'ajuster un modèle pré-entraîné sur des données étiquetées spécifiques à une tâche donnée. Cette approche a permis d'obtenir de bonnes performances même avec des ensembles de données plus petits et spécifiques à un domaine. Cela a également permis de rendre les transformers plus accessibles aux utilisateurs non experts.

Parmi les défis actuels des transformers, on peut citer :

- Gestion de la complexité computationnelle : A l'ère du réchauffement climatique, il est de plus en plus mal vu d'utiliser des technologies qui demandent autant de ressources. Les transformers, en particulier les modèles de grande échelle, nécessitent d'importantes ressources computationnelles pour l'entraînement et l'inférence. Réduire la complexité et améliorer l'efficacité des modèles sans compromettre les performances reste un défi à relever.

- Interprétabilité : Les transformers sont souvent considérés comme des "boîtes noires" en raison de leur complexité. Comprendre et interpréter les décisions prises par les transformers reste un défi important. Comprendre comment les modèles prennent leurs décisions et quelles sont les informations prises en compte est crucial, en particulier pour les applications critiques telles que la santé et la sécurité. Les chercheurs travaillent sur des méthodes d'interprétabilité pour mieux comprendre comment les informations sont traitées et utilisées dans les différentes couches des transformers.

6. Conclusion

En conclusion, les transformers ont révolutionné le domaine de l'intelligence artificielle, du domaine de la NLP, et ont ouvert de nouvelles perspectives dans le traitement de séquences. Leur architecture basée sur l'attention leur confère une capacité unique à capturer les dépendances à longue distance, ce qui les rend particulièrement adaptés pour modéliser des données séquentielles complexes. Les transformers ont été largement utilsés dans des domaines tels que la traduction automatique, le résumé de texte, la vision par ordinateur et bien d'autres.

Au fil des années, les transformers ont connu des améliorations significatives, avec des modèles de plus en plus grands et des avancées dans l'efficacité de l'attention. Cependant, des défis subsistent, notamment en termes d'explicabilité et d'interprétabilité des prédictions, ainsi que de gestion des ressources nécessaires pour entraîner et déployer des modèles de grande échelle.

Malgré ces défis, les transformers continuent de repousser les limites de l'intelligence artificielle et d'améliorer les performances dans de nombreux domaines. Leur capacité à modéliser les dépendances complexes des séquences en fait une architecture puissante et désormais incontournable. 

# III. DISHDECODER

## 3.1 Le modèle d'OCR

### 3.1.1 Le choix du modèle

Il existe à l'heure actuelle de très nombreux modèles pour réaliser de l'OCR (Optical Character Recognition).

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

Afin de vérifier les performances du nouveau modèle, j'ai écrit un script Python permettant de comparer, EasyOCR, PaddleOCR avant le finetuning, et mon modèle PaddleOCR après le finetuning.

Pour mesurer les performances des OCR, j’ai choisi de calculer les distances de Levenshtein et d’Indel.
La distance de Levenshtein est une mesure de similitude entre deux chaînes de caractères, définie comme le nombre minimum d'éditions de caractères simples (insertions, suppressions ou substitutions) nécessaires pour transformer une chaîne en l'autre. Plus la distance est proche de 0,
plus les deux textes sont similaires.
La distance Indel est une variation de la distance de Levenshtein qui prend en compte uniquement les insertions et les suppressions, et pas les substitutions. C'est également une mesure de la dissimilarité entre deux chaînes de caractères. Pour Indel, plus la distance est proche de 100, plus
les deux textes sont similaires.

Pour pouvoir comparer les OCR, j’ai constitué un nouveau jeu de données de 10 images.


INSERER IMAGES DU DATASET DE TEST

Les résultats de la comparaison furent les suivants :
- pour la distance d’Indel (meilleur résultat = proche de 100) : EasyOCR: 89.53, PaddleOCR_base : 91.76, PaddleOCR_finetuné : 93.28 .
- pour la distance de Levenshtein (meilleur résultat = proche de 0) : EasyOCR: 3.7, PaddleOCR_base: 3.0, PaddleOCR_finetuné : 2.2 .

INSERER IMAGE AVEC LES RESULTATS    

On peut donc en conclure que peu importe la méthode de calcul le classement est le suivant :
 1ère place PaddleOCR nouveau modèle finetuné
 2nde place PaddleOCR modèle de base
 3ème place EasyOCR 

Grâce à cela, on peut en déduire que le finetuning a permis d’améliorer la précision du modèle. Le nouveau modèle finetuné est donc l’OCR le plus performant parmi ceux testés.


### 3.1.9 Le stockage du modèle

Afin de pouvoir utiliser ce modèle dans ce projet et dans d'autres à venir, j'ai décidé de le stocker sur le Hub Hugging Face. Pour cela, j'ai créé un nouveau repository sur mon compte Hugging Face et j'ai ajouté les fichiers du modèle dans ce repository.
Le modèle est donc maintenant disponible à l'adresse suivante : https://huggingface.co/PaulineSanchez/PaddleOCR_ft

INSERER ICI UNE IMAGE DU HUB HUGGING FACE AVEC LE MODELE DANS LE REPOSITORY

# 3.2 Les modèles de traduction

### 3.2.1 Le choix des modèles

C'est en raison des résultats évoqués dans l'état de l'art de ce projet que j'ai décidé d'utiliser des modèles de traduction neuronaux basés sur les Transformers. Afin de choisir quels modèles j'allais utiliser et finetuner, j'ai été lire le cours sur la traduction de Hugging Face. Plusieurs modèles étaient proposés, comme par exemple T5, MarianMT, Bart...

T5 (Text-To-Text Transfer Transformer) est un modèle de traitement du langage naturel développé par Google. Il s'agit d'un modèle basé sur les Transformers qui peut être utilisé pour diverses tâches, dont la traduction. 
Bart (Bidirectional and AutoRegressive Transformers") est un modèle développé par Facebook AI. Il est lui aussi basé sur les Transformers et a été spécifiquement conçu pour la génération de texte. 
MarianMT est un projet open-source qui se concentre sur la traduction automatique neuronale. Il s'agit d'une implémentation basées sur les Transformers. MarianMT utilise le même modèle de base que Bart avec quelques modifications.

Souhaitant utiliser des modèles spécialisés dans les tâches de traduction neuronaux basés sur les Transformers, j'ai donc décidé de finetuner des modèles basés sur MarianMT.

### 3.2.2 Les données nécessaires à l'entraînement des modèles

Souhait faire de la traduction de l'anglais vers le français et du français vers l'anglais, j'ai choisi de finetuner les deux modèles suivants :
`Helsinki-NLP/opus-mt-fr-en` pour la traduction du français vers l'anglais, et `Helsinki-NLP/opus-mt-en-fr` pour la traduction de l'anglais vers le français.
Pour finetuner ces modèles, j'allais avoir besoin d'un dataset contenant des phrases en anglais et leur traduction en français. Afin d'obtenir de bonnes performances, il fallait que ce dataset soit composé de phrases plus ou moins longues et de phrases plus ou moins complexes. De plus, le but de ce finetuning était pour moi d'obtenir des modèles spécialisés dans la thématique de la cuisine. Il fallait donc que le dataset contienne des phrases en lien avec la cuisine. Ces phrases devaient contenir des verbes d'action propres à la cuisine et à la réalisation de recettes, des noms d'ingrédients, des noms de plats, des noms d'ustensiles... Par ailleurs, plus le dataset allait être volumineux, plus les performances des modèles allaient être bonnes.


### 3.2.3 La création du dataset

De nombreux datasets de traduction sont disponibles sur les sites de Kaggle ou même d'Hugging Face. Cependant, aucun ne correspondait à mon thème, qui était la cuisine, dans les deux langues choisies, le français et l'anglais. Comme pour le finetuning d'OCR, j'ai donc décidé de créer mon propre dataset. Pour cela, j'ai utilisé plusieurs sites de cuisine : marmiton.org, allrecipes.com, simplyrecipes.com, mercotte.fr et quelques autres. 
A chaque fois, je selectionnais une ou plusieurs phrases qui me semblaient intéressantes, je les copiais, les collais dans la zone de texte du site deepl.com et je les traduisais dans la langue cible. Ayant des connaissances dans la traduction en anglais, je pouvais dans un second temps faire les modifictions nécessaires afin d'obtenir une traduction de qualité. Il ne me restait plus qu'à copier les phrases en anglais et leur traduction en français, et inversement, dans mon fichier CSV.
J'ai utilisé deepl.com car il s'agit d'un site de traduction qui utilise des modèles neuronaux et qui est donc plus performant que Google Traduction par exemple. 

Afin de pouvoir finetuner mes modèles, le moyen le plus efficace était de créer des datasets avec la librairie Datasets de Hugging Face. Cette librairie permet de créer des datasets à partir de fichiers JSON, CSV, TXT, XML, etc. 
Il fallait donc dans un premier temps que je crée un fichier CSV avec les données sur lesquelles je souhaitais finetuner mon modèle.
Le CSV devait avoir une colonne `id` qui s'incrémente à chaque nouvelle entrée et une colonne `translation` qui contient la phrase en anglais et sa traduction en français.
J'ai donc crée un CSV avec ces caractéristiques et il ne me restait plus qu'à le remplir avec les données que je souhaitais. 
Au final, mon fichier CSV était constitué de 399 entrées. 

### 3.2.4 Le prétraitement des données

Avant de transformer mon fichier CSV en Dataset Hugging Face, je n'ai pas fait de data augmentation. J'ai estimé que les données que j'avais sélectionnées étaient suffisantes pour finetuner mes modèles. 
J'ai donc utilisé la librairie Datasets de Hugging Face pour transformer mon fichier CSV en Dataset Hugging Face. Lors de l'exécution du script, j'ai pris soin de préciser que la colonne `translation` était une colonne de type `Translation` afin que le Dataset Hugging Face soit bien un dataset de traduction.

INSERER ICI LE CODE POUR TRANSFORMER LE CSV EN DATASET HUGGING FACE

J'ai ensuite envoyé mon dataset sur le Hub de Hugging Face où il a été stocké à l'adresse suivante `https://huggingface.co/datasets/PaulineSanchez/recipes_translation_4_helsinki_4.0`.

Après cela, et après avoir vérifié que mon dataset était correct et bien disponible sur le Hub de Hugging Face, je l'ai téléchargé, et toujours avec la librairie Datasets de Hugging Face, j'ai divisé mon dataset en deux datasets : un dataset d'entraînement et un dataset de validation. J'ai choisi de diviser mon dataset de la manière suivante, 80% des données pour l'entraînement et 20% pour la validation. Cela donnait un dataset d'entraînement de 319 entrées et un dataset de validation de 80 entrées.

INSERER ICI LE CODE POUR DIVISER LE DATASET EN DATASET D'ENTRAINEMENT ET DATASET DE VALIDATION

### 3.2.5 Le stockage du dataset

Comme pour le dataset avant la séparation en jeu d'entraînement et en jeu de validation, j'ai envoyé mon dataset sur le Hub de Hugging Face grâce à la fonction `push_to_hub` de Hugging Face. Mon dataset a été stocké à l'adresse suivante `https://huggingface.co/datasets/PaulineSanchez/recipes_translation_400`. Ce dataset en affiché en mode public afin que tout le monde puisse y avoir accès et l'utiliser.

INSERER ICI LE CODE POUR ENVOYER LE DATASET SUR LE HUB DE HUGGING FACE + FLOUTER LE TOKEN
INSERER ICI UNE CAPTURE D'ECRAN DU DATASET SUR LE HUB DE HUGGING FACE

### 3.2.6 L'entraînement des modèles

Pour entraîner mes modèles, j'ai utilisé un script que j'ai trouvé sur le Github de Hugging Face, dans le repository `transformers/examples/pytorch/translation`. Ce script permet d'entraîner un modèle de traduction, selon si son architecure est basée sur les transformers, à partir d'un dataset Hugging Face ou de fichiers json/CSV. J'ai donc utilisé ce script pour entraîner mes deux modèles de traduction.
Afin de pouvoir utilisé ce script, j'ai dû cloner le repository `transformers` de Hugging Face sur mon ordinateur. 
Après cela, après m'être déplacé dans le dossier, j'ai lancé la commande suivante :

```$ python examples/pytorch/translation/run_translation.py     --model_name_or_path Helsinki-NLP/opus-mt-en-fr     --do_train     --do_eval     --source_lang en     --target_lang fr     --dataset_name PaulineSanchez/recipes_translation_400  --output_dir /home/pauline/Documents/PCO/Modele_Traduction/train_hf_new_batch_4_epoch_6     --per_device_train_batch_size=6     --per_device_eval_batch_size=6     --predict_with_generate --report_to wandb --num_train_epochs 6 ```

Cette commande permet de lancer l'entraînement du modèle de traduction. Elle prend en paramètre le nom du modèle à utiliser, le code de la langue source, le code de la langue cible, le nom du dataset à utiliser, le chemin vers le dossier où stocker les résultats de l'entraînement, la taille du batch d'entraînement, la taille du batch de validation, le nom de l'outil utilisé pour faire du monitoring et le nombre d'epochs à effectuer. 

J'ai donc lancé cette commande plusieurs fois, en inversant les langues source et cible et en précisant le nom du modèle à utiliser. J'ai également changé le nom du dossier où stocker les résultats de l'entraînement afin de pouvoir les différencier.

### 3.2.7 Configuration des hyperparamètres des modèles

Lors des différents entraînements que j'ai lancé, les hyperparamètres que j'ai modifiés sont les suivants :
- le batch size : j'ai fait des tests avec des batch allant de 2 à 16
- le nombre d'epochs : j'ai fait des tests avec des epochs allant de 3 à 75

En fonction des résultats que j'obtenais et des courbes dessinées sur Weight and Biases, j'ai pu ajuster les hyperparamètres au fur et à mesure afin d'obtenir les meilleurs modèles possibles.

AJOUTER CAPTURE D'ECRAN DES COURBES DE W&B

### 3.2.8 Comparaison des modèles et choix des meilleurs

La métrique utilisée par Hugging Face pour comparer les modèles de traduction est le score BLEU (bilingual evaluation understudy). Le BLEU score est une métrique qui permet de comparer la qualité d'une traduction automatique à une ou plusieurs traductions de référence. Il évalue la similarité entre les n-grammes (séquences de n mots consécutifs) présents dans la sortie générée et ceux présents dans les références. Le score est compris entre 0 et 1. Plus le score est proche de 1, plus la traduction est de bonne qualité. Cependant, le score BLEU présente également certaines limites. Par exemple, il ne tient pas compte de la sémantique ou de la cohérence globale du texte, ce qui signifie qu'un score élevé ne garantit pas nécessairement une traduction ou un résumé de haute qualité sur tous les aspects.

Ainsi, afin de pouvoir comparer les différents modèles entraînés, j'ai là aussi utilisé Weight and Biases. 
J'ai classé mes modèles selon leur score BLEU et j'ai pu ainsi déterminer les meilleurs modèles.

INSERER ICI CAPTURE D'ECRAN DES MODELES ET DE LEUR SCORE BLEU

Ainsi, pour le modèle de traduction anglais-français, le meilleur modèle est celui entraîné avec un batch size de 8 et 3 epochs. Pour le modèle de traduction français-anglais, le meilleur modèle est celui entraîné avec un batch size de 12 et 4 epochs.

### 3.2.9 Le stockage des modèles

Une fois que j'ai déterminé les meilleurs modèles, je les ai envoyé sur le Hub de Hugging Face afin de pouvoir les utiliser par la suite. J'ai utilisé la fonction `push_to_hub` de Hugging Face pour envoyer mes modèles sur le Hub. Il est a noté que la fonction `push_to_hub` utilise Git et Git LFS pour envoyer les modèles sur le Hub. Ainsi, peu importe la taille du modèle, il sera envoyé sur le Hub.
Mes modèles ont été stockés aux adresses suivantes `https://huggingface.co/PaulineSanchez/translation_for_recipes_en_fr` pour le modèle anglais vers français et `https://huggingface.co/PaulineSanchez/translation_for_recipes_fr_en` pour le modèle français vers anglais.
Ces modèles sont en mode public afin que tout le monde puisse y avoir accès et les utiliser.

INSERER ICI LE CODE POUR ENVOYER LES MODELES SUR LE HUB DE HUGGING FACE + FLOUTER LE TOKEN

INSERER ICI UNE CAPTURE D'ECRAN DES MODELES SUR LE HUB DE HUGGING FACE

## 3.3 L'utilisation d'Open AI

### 3.3.1 Pouquoi le choix d'OPEN AI ?

Maintenant que mes modèles d'OCR et de traduction étaient finetunés, j'ai souhaité ajouté un bloc entre les deux qui me permettrait de corriger la grammaire et l'orthographe de la sortie de l'OCR afin que le modèle de traduction puisse fonctionner sur un texte correct et ne pas être perturbé par des erreurs. En effet, la moindre confusion entre deux caractères plutôt proches ou même l'ajout de caractère peut entraîner une erreur de traduction. Ainsi, j'ai souhaité utiliser un modèle de correction orthographique et grammaticale afin de corriger les potentielles erreurs de l'OCR.

Après de nombreuses recherches, je n'ai pas réussi à trouver un package Python qui me permettrait de faire cela de la manière dont je l'entends. J'ai pu tester Pygrammalecte qui est un wrapper Python autour de Grammelecte. Grammelecte est un correcteur grammatical et typographique open-source pour le français. Il a différent modules pour être ajouté sur Google Chrome, Firefox, Libre Office, Open Office ... Cependant, sa version Python n'était pas adaptée à ce que je souhaitais faire. En effet, Pygrammalecte ne permet pas de corriger un texte mais seulement de donner des suggestions de correction pour un mot donné. Par ailleurs, de nombreux mots corrects étaient signalés comme n'existant pas. Cela signifait donc que les dictionnaires utilisés en arrière plan n'étaient pas à jour voir erronnés. Je n'ai rien trouvé d'autre qui pouurrait fonctionner pour la correction en français. Il y a des projets qui existent mais soit ils ne fonctionnent pas, soit ils sont inachevés, soit ils ne sont pas utilisables en Python.

Du côté des outils similaires à chatGPT et Open AI, là aussi j'ai trouvé des alternatives mais aucune qui puisse fonctionner aussi bien et toutes avaient un coût plus élevé.

### 3.3.2 L'API d'Open AI

Afin de pouvoir utiliser l'API d'Open AI, j'ai eu besoin de créer un compte sur leur site. Une fois le compte crée, j'ai lié ma carte bancaire à mon compte et défini un seuil au delà duquel mes requêtes sont automatiquement rejetée et donc je ne paye pas plus. Sur Open AI, la facturation ne se fait pas à l'appel (de l'API) mais au nombre de tokens. Une fois tout cela mis en place, j'ai pu générer et récupérer ma clé API. 
J'ai également dû installer le package `openai` en utilisant la commande `pip install openai`.
L'API d'Open AI permet d'utiliser de nombreux modèles dont par exemple gpt-3.5-turbo ou encore text-davinci-003.

### 3.3.3 Le modèle utilisé

Pour répondre à mes besoins, j'ai décidé d'utiliser le modèle de completions `text-davinci-003`. Ce modèle est censé être le plus performant parmi ceux disponibles pour les tâches de linguistique. En effet, il doit pouvoir effectuer n'importe quelle tâche de linguistique comme la traduction ou la correction orthographique en apportant une qualité supérieure et un bon suivi des instructions. 
`text-davinci-003` a une limite maximale de 4 097 tokens. Les tokens sont des fragments de texte qui peuvent être aussi courts qu'un seul caractère ou aussi longs qu'un mot. La limite de tokens est importante car les modèles ont une contrainte sur le nombre maximum de tokens qu'ils peuvent traiter dans une seule entrée ou sortie.

### 3.3.4 Le prompt

Comme pour chatGPT, j'ai dû créer un prompt pour mon modèle. Le prompt est une phrase qui va permettre au modèle de comprendre ce que l'on attend de lui. Ainsi, j'ai créé un prompt qui permettra à mon modèle de corriger les erreurs orthographiques et grammaticales de l'OCR. Etant donné que certaines sorties seront en anglais et d'autres en français, j'ai crée un prompt pour chaque langue. Voici les prompt que j'ai utilisé : 
- Pour le français : ```"Corrige seulement la grammaire et l'orthographe du texte suivant :\n\n {sentence}"```
- Pour l'anglais : ```"Correct only the grammar and the orthograph of the following text:\n\n {sentence}"```


## 3.4 Le back-end

### 3.4.1 L'API

Afin de pouvoir faire communiquer ensemble les différents composants de mon application j'ai décidé de créer une API. Pour réaliser cette API j'ai utilisé le framework `fastapi`. Ce package permet de créer une API en Python. J'ai également utilisé le package `uvicorn` qui permet de lancer l'API. J'ai utilisé la commande `pip install fastapi` pour installer `fastapi` et la commande `pip install uvicorn` pour installer `uvicorn`.

L'API en elle même est constituée d'un fichier main.py et d'un fichier service.py. 
Les fichiers models.py, config.py, database.db et alerting.py sont des fichiers qui permettent de faire fonctionner l'API et qui appartiennt au back-end mais qui ne sont pas des composants directs de l'API.
L'API communique également avec le dossier models qui contient le modèle d'OCR. En effet, bien que le modèle ait été stocké sur le hub de Hugging Face, il n'est pas possible de l'utiliser directement depuis le hub. Il faut donc le télécharger et le stocker dans un dossier.

Le fichier main.py est le point d'entrée principal de l'API. Il contient les routes principales de l'API, telles que la racine ("/"), la vérification de l'état de santé de l'API ("/healthcheck"), l'inférence ("/inference"), le stockage des images sur Cloudinary ("/img2cloud"), etc. Chaque route est associée à une fonction qui définit son comportement.

Le fichier service.py contient la classe Service, qui fournit les fonctionnalités principales de l'API. Cette classe utilise divers modules et modèles pour effectuer des opérations telles que l'OCR sur une image, la correction de texte via Open AI, la traduction, etc. On y retrouve également les fonctions permettant de réaliser l'inférence telles que : do_ocr, do_correct_text, do_translation, etc.

Les fichiers models.py, config.py et database.db sont utilisés pour définir et gérer les modèles de données et la base de données utilisés par l'API. 

Le fichier config.py contient une classe Settings qui stocke les configurations du projet. Les attributs de cette classe incluent des clés d'API, les informations de connexion sur Cloudinary, une URL de webhook Discord, les chemins des modèles de traduction sur le hub d'Hugging Face, ainsi que d'autres paramètres. Les valeurs de configuration sont chargées à partir d'un fichier .env en utilisant la bibliothèque dotenv. Les valeurs peuvent être accédées via l'instance settings de la classe Settings.

Le fichier models.py définit les modèles de données utilisés dans le projet. Trois classes sont définies : User, Link et Data. Ces classes correspondent aux tables de la base de données. Chaque classe utilise la bibliothèque SQLmodel pour définir les attributs et les relations entre les tables. Par exemple, la classe Link contient des attributs tels que id, url, description, timestamp et user_id. Le fichier crée également une instance de moteur de base de données engine qui utilise SQLite comme backend.

Le fichier database.db est la base de données SQLite utilisée par l'API. 

Le fichier alerting.pycontient une fonction send_discord_notification qui est utilisée pour envoyer des notifications sur serveur Discord dédié à Dishdecoder. La fonction utilise la bibliothèque discord et utilise l'URL d'un webhook Discord défini dans le fichier config.py. Lorsqu'elle est appelée, la fonction envoie un message à travers le webhook. La fonction est utilisée pour envoyer des notifications pour des événements importants, tels que la création d'un nouvel utilisateur ou l'échec d'une requête.

### 3.4.2 La schématisation de l'API

INSERER ICI UN SCHEMA DE L'API

### 3.4.3 La base de données relationnelle

La base de données utilisée dans ce projet est une base de données relationnelle, qui stocke les informations relatives aux utilisateurs et à ce qu'ils créent sur l'application. La base de données est mise en œuvre à l'aide du système de gestion de base de données SQLite.

La structure de la base de données est définie à l'aide de la bibliothèque SQLmodel, qui permet de créer des modèles de données Python qui sont ensuite mappés aux tables de la base de données. Dans ce projet, nous utilisons trois tables principales : User, Link et Data.

La table User contient les informations relatives aux utilisateurs de l'application. Chaque utilisateur est représenté par un enregistrement dans cette table, avec des attributs tels que id, username, email et password. L'attribut id est une clé primaire qui permet d'identifier de manière unique chaque utilisateur.

La table Link stocke les liens URL des images générées par l'utilisateur et stockées sur Cloudinary. Chaque enregistrement dans cette table est lié à un utilisateur spécifique à l'aide de la clé étrangère user_id. Les autres attributs de cette table comprennent id, url, description et timestamp, qui enregistre la date et l'heure de création de chaque enregistrement.

La table Data est utilisée pour stocker les données générées par les utilisateurs dans un souci d'amélioration de l'application. Chaque enregistrement dans cette table est associé à un utilisateur et contient des attributs tels que id, ocr_entry, corrected_ocr, translation_output et user_rating. L'attribut user_id établit la relation avec la table User via une clé étrangère.

L'utilisation d'une base de données relationnelle permet de stocker de manière organisée et structurée les informations nécessaires au bon fonctionnement de l'application. Les relations entre les tables garantissent l'intégrité des données et permettent de récupérer facilement les informations liées à un utilisateur spécifique.

La création et la gestion de la base de données sont gérées par l'instance du moteur de base de données engine créée à l'aide de SQLmodel. Lorsque l'application démarre, les tables sont créées automatiquement si elles n'existent pas déjà.

L'API contient plusieurs endpoints qui permettent d'agir sur la base de données soit en insérant des données, soit en récupérant des données.
Tous les endpoints liés à la base de données se situent dans le fichier main.py. Les endpoints sont les suivants :

- /create_user : Crée un nouvel utilisateur en enregistrant les informations fournies (nom d'utilisateur, adresse e-mail, mot de passe) dans la table "User" de la base de données.

- /check_user : Vérifie les identifiants d'un utilisateur en comparant le nom d'utilisateur et le mot de passe fournis avec ceux enregistrés dans la base de données.

- /check_username : Vérifie si un nom d'utilisateur est déjà utilisé en comparant le nom d'utilisateur fourni avec ceux enregistrés dans la base de données. Les noms d'utilisateurs doivent être uniques, sans tenir compte de la casse.

- /check_email : Vérifie si une adresse e-mail est au bon format en utilisant une expression régulière.

- /check_password : Vérifie si un mot de passe est au bon format en utilisant une expression régulière.

- /get_user_id : Récupère l'ID d'un utilisateur en vérifiant les identifiants (nom d'utilisateur et mot de passe) fournis.

- /add_to_links : Ajoute un lien à la liste des liens en enregistrant l'URL, la description et l'ID de l'utilisateur dans la table "Link" de la base de données.

- /get_links : Récupère la liste des liens d'un utilisateur spécifique en utilisant son ID.

- /add_rating : Ajoute une note sur la qualité de la traduction à la base de données en enregistrant l'ID de l'utilisateur, la note donnée par l'utilisateur, le texte original, le texte corrigé et le texte traduit dans la table "Data".

- /get_data : Récupère la liste de toutes les données enregistrées dans table "Data".

A propos des requêtes utilisées pour interagir avec la base de données, La méthode query est utilisée pour effectuer des requêtes de recherche, la méthode add pour ajouter de nouveaux enregistrements, et la méthode commit pour valider les changements effectués dans la session et les sauvegarder dans la base de données. 

INSERER ICI UN SCHEMA DE LA BASE DE DONNEES

### 3.4.5 Le stockage des images des utilisateurs

Afin de pouvoir stocker les images générées par les utilisateurs, j'ai choisi d'utiliser Cloudinary. Cloudinary est un service de stockage d'images basé sur le cloud. La version gratuite de Cloudinary permet de stocker jusqu'à 25 Go de données. Cloudinary s'intègre très bien dans Dishdecoder, car il existe une bibliothèque Python qui permet d'interagir avec l'API de Cloudinary. Cela permet d'envoyer une image sur Cloudinary, de l'y stocker et de récupérer son URL en quelques lignes de code.
Ainsi, lorsqu'un utilisateur génère une image de recette traduite, il a la possibilité de lui donner une description et de la sauvegarder dans son espace personnel. Cela va en réalité envoyer l'image sur Cloudinary et enregistrer l'URL de l'image et la description donnée par l'utilisateur dans la base de données. Par la suite lorsque l'utilisateur ira dans son espace personnel, il y retrouvera l'image, la description de celle-ci, ainsi que la date et l'heure à laquelle elle a été enregistrée. Autrement dit, l'image n'est pas stockée dans la base de données, mais sur Cloudinary. Cela permet de ne pas surcharger la base de données avec des images, et de ne pas avoir à gérer le stockage de ces images.


## 3.5 Le front-end

### 3.5.1 L'utilisation de Streamlit

Pour le front-end de l'application, j'ai choisi d'utiliser Streamlit. Streamlit est un framework open-source qui permet de créer des applications web en Python. Streamlit possède de très nombreuses fonctionnalités qui permettent de créer des applications web interactives et personnalisées. Il est notamment possible d'ajouter des formulaires, des zones de texte, des boutons, de créer plusieurs pages, d'afficher des tableaux etc. La communauté de Streamlit étant très active de nouvelles fonctionnalités sont ajoutés régulièrement et il est également possible de trouver des modules créés par des utilisateurs qui permettent d'ajouter davantage de fonctionnalités supplémentaires. 

Streamlit ne doit cependant pas être utilisé pour le déploiement d'applications ou de site web. Streamlit est avant tout un démonstrateur. Streamlit est donc bien adapté dans le cadre de ce projet.

### 3.5.2 La schématisation du front-end

INSERER ICI LE SCHEMA DU FRONT-END

### 3.5.3 Les fonctionnalités de l'application

L'application est composée de 3 pages: la page d'accueil, la page de traduction et d'espace personnel, et la page de l'administrateur.

La page d'acceuil comprend une courte description de l'application, une image de l'égérie de l'application, ainsi que des boutons pour créer un compte utilisateur ou se connecter à un compte existant.

La seconde page comprend deux onglets. Le premier onglet affiche l'historique des enregistrements de l'utilisateur, ceux-ci sont consignés dans un tableau. Chaque entrée comprend, un id, l'image générée par l'utilisateur, la description que l'utilisateur a donné à son image, et la date et l'heure où l'image a été enregistrée. Il y a également un bouton qui permet de rafaîchir le tableau. Dans l'autre onglet, il est possible de télécharger une image, de la recadrer de façon à n'avoir qu'un seul paragraphe, et enfin de choisir si on veut effectuer une traduction de l'anglais vers le français ou du français vers l'anglais. Une fois que la traduction est effectuée, une nouvelle image va apparaître avec le texte traduit. L'utilisateur a alors la possibilité de donner une description à l'image et de l'enregistrer dans son espace personnel. L'utilisateur peut également choisir de donner une note à la traduction. Enfin, en bas de la page, il y a un bouton qui permet de retourner à la page d'accueil.

La troisième page, qui n'est accessible qu'à l'administrateur après avoir rentré son nom d'utilisateur et son mot de passe dans l'espace de connexion, contient un tableau où sont consignées les traductions que l'utilisateur a choisi de noter. Chaque entrée comprend, un id, le texte extrait par l'OCR, le texte corrigé par OpenAI, la traduction de ce texte et la note donnée par l'utilisateur. Il y a également un code couleur à l'intérieur du tableau en fonction de la note donnée par l'utilisateur afin que cela attire l'attention de l'administrateur. Enfin, en bas de la page, il y a un bouton qui permet à l'administrateur de télécharger le tableau en CSV et un autre qui permet de retourner à la page d'accueil.

D'autre part, des messages d'erreurs sont affichés lorsque l'utilisateur ne remplit pas correctement les champs des formulaires ou lorsqu'il y a un problème de connexion à l'API ou encore losrque l'API renvoie une erreur.

Lorsque l'API renvoie un message d'erreur ou lorsqu'un nouveau utilisateur est crée, un message est envoyé à l'administrateur sur le serveur Discord de Dishdecoder en lui spécifiant le type d'erreur ou le nom du nouvel utilisateur. Cela permet à l'administrateur de pouvoir réagir rapidement en cas de problème.

Enfin, l'intérêt d'afficher un tableau avec les notes des utilisateurs à propos des traductions est de pouvoir améliorer les modèles d'intelligence artificielle. En effet, l'administrateur peut voir quelles sont les traductions qui ont été mal notées et en tenir compte lorsqu'il constituera un nouveau jeu de données pour ré-entraîner les modèles. Cela permettra d'améliorer les modèles et donc d'améliorer la qualité des traductions. 

### 3.5.4 L'interaction avec le back-end

L'interaction avec la base de données relationnelle et avec les modèles d'intelligence artificelle se fait grâce à des appels API. Pour cela, j'ai utilisé la bibliothèque Python requests. Cette bibliothèque permet d'envoyer des requêtes HTTP. Ainsi, pour envoyer une requête à l'API, il suffit de préciser l'URL de l'API, le type de requête (GET, POST, PUT, DELETE) et les paramètres de la requête. Afin d'intégrer ces appels à l'API convenablement dans l'application, j'ai créé une fonction pour chaque requête. Ainsi, lorsque l'utilisateur clique sur un bouton, la fonction correspondante est appelée et la requête est envoyée à l'API.
Cela permet également de bien séparer le front-end du back-end. En effet, le front-end sert uniquement à l'affichage et ne fait que des appels à l'API, il n'interagit pas directement avec la base de données ou avec les modèles d'intelligence artificielle. Cela permet de rendre l'application plus robuste et plus facile à maintenir. En effet, si l'on souhaite modifier la base de données ou les modèles d'intelligence artificielle, il suffit de modifier l'API, sans avoir à modifier le front-end.

## 3.6 L'organisation du projet

### 3.6.1 Le GANTT

### 3.6.2 Le Kanban

### 3.6.3 Le GitHub

Dès le début du projet, j'ai créé un dépôt GitHub pour pouvoir versionner mon code. Ainsi, à chaque ajout de fonctionnalité, je faisais un commit depuis mon IDE, VSCode. Cela était rassurant car je gardaus la possibilité de revenir à une version antérieure de mon code en cas de problème. Aussi, Cela m'a été utile pour pouvoir travailler sur différents ordinateurs sans avoir à transférer les fichiers. En effet, il suffisait de cloner le dépôt sur l'ordinateur sur lequel je souhaitais travailler. 

# IV. CONCLUSION

## 4.1 La réalisation du projet

Réaliser Dishdecoder fut une expérience enrichissante pour de nombreuses raisons. 
Tout d'abord, en raison de la partie sur la traduction. Venant d'une formation spécialisée dans les langues étrangères, j'ai toujours été intéressée et passionée par la traduction. Cependant, je n'avais pas encore eu l'occasion de mêler mes nouvelles connaissances en intelligence artificielle à ma passion pour la traduction. C'est donc avec beaucoup d'enthousiasme et d'intérêt que j'ai réalisé ce projet et découvert cette branche de la NLP. 
Ensuite, je n'avais pas encore eu l'opportunité de travailler sur un projet qui utilise plusieurs modèles d'intelligence artificielle à la suite. J'ai donc apprécié pouvoir combiner ici un modèle d'OCR, un modèle de correction de texte et un modèle de traduction. 
Par ailleurs, ce projet m'a prouvé une fois encore que ce qui me plaît le plus est la constitution de jeux de données. En effet, j'ai passé beaucoup de temps à réunir les données que je souhaitais pour le modèle d'OCR et les modèles de traduction, mais cela n'a jamsi été un fardeau car j'ai pu obtenir exactement ce que je voulais et en plus de cela, les résultats ont été très satisfaisants.
Enfin, avoir un projet que j'ai crée de toute pièce et qui fonctionne est très gratifiant. Cela m'a permis de voir que j'étais capable de réaliser un projet de A à Z et de le mener à bien.

## 4.2 Les difficultés rencontrées

Je pense que la difficulté majeure dans ce genre de projet est de réussir à s'arrêter. Que ce soit lors de la constitution de jeux de données, lors de l'entraîenment de modèle ou lors de la réalisation de l'interface graphique et de l'intégration des différentes fonctionnalités, il m'a toujours été très compliqué de savoir quand m'arrêter. En effet, il y a toujours quelque chose à améliorer, à modifier ou à ajouter. Cependant, il faut savoir s'arrêter à un moment donné pour pouvoir passer à autre chose.
Une autre difficulté fut dans le choix de la technologie à utiliser pour l'interface graphique. En effet, lors de ma formation et de mon alternance nous avons très souvent utilisé Streamlit. J'apprécie beaucoup Streamlit car je trouve leur documentation très claire et en plus il y a toujours des nouveautés qui apportent de réels changements. Cependant, j'avais envie de changer et d'utiliser une autre technologie. J'ai donc commencé à utiliser Pynecone. La prise en main fut un peu plus compliquée car la documentation est moins claire et surtout il y a beaucoup moins de ressources sur internet étant donné que Pynecone est relativement récent. Toutefois, j'avais réussi à créer ma première page. Les problèmes vinrent lorsque j'ai eu besoin d'utiliser un wrapper React afin d'utiliser un widget me permettant de recadrer les images. Malgré tous mes efforts cela n'a jamais fonctionné comme je l'espèrais et lorsque j'ai voulu intégrer FastAPI à Pynecone j'ai compris que cela n'allait pas être possible non plus. J'ai donc décidé de revenir à Streamlit. Cela m'a permis de me rendre compte que Streamlit est vraiment une technologie que j'apprécie et que je maîtrise bien.

## 4.3 Les améliorations et les perspectives d'évolution

J'ai déjà de nombreuses idées pour améliorer Dishdecoder. 
Parmi les choses simples à faire, il y a :
- le fait d'intégrer un bouton qui permet à l'utilisateur de télécharger sur son ordinateur l'image qu'il a générée.
- le fait d'intégrer à l'interface administateur des statistiques sur les notes données aux traductions par les utilisateurs.

Parmi les choses qui prennent un peu plus de temps, il y a :
- le fait d'intégrer de nouvelles langues de traduction, notamment l'espagnol et l'italien.
- le fait de finetuner un modèle me permettant de faire de la correction orthographique.
- le fait d'augmenter le nombre d'entrées dans le jeu de données pour les modèles de traduction.
- trouver un moyen pour me passer du recadrage des images
- trouver un moyen de convertir les unités de mesures dans les recettes

Je pense que Dishdecoder est une application qui peut avoir de l'avenir et qui saurait sans doute trouver son public. Certes TextGrabber et Deepl existent mais il paraît que l'humain préfère de plus en plus aller à la simplicité. Alors quoi de plus simple que de prendre une photo de son livre de recettes et de se faire traduire la recette en un clic ? 