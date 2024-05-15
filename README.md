# Outils-traitement-corpus

## TD Cours n°1

### Tâche réalisée

J'ai choisi une tâche d'ASR (automatic speech recognition), c'est-à-dire une tâche dont les différents aspects peuvent être la transcription de mots écrits à partir d'extraits audio de parole, l'identification du locuteur, ou encore la caractérisation de ce dernier. La tâche sur laquelle je veux particulièrement me concentrer serait celle de la caractérisation d'un loctueur.

### Corpus qui répond à cette tâche

Pour le corpus, j'ai choisi le [**Mozilla Common Voice**](https://commonvoice.mozilla.org/fr), car il s'agit d'un projet de production participative dans le but de créer une base de données libre et open-source d'extraits audio pour l'ASR. Tous les enregistrements ont ainsi été recueillis par des volontaires aux profils variés, qui s'enregistrent et vérifient les enregistrements des autres. Tout cela est ensuite réuni dans une base de données du domaine public, sous la licence CC0.

Ce corpus se compose de 30k heures d'enregistrement, dont 19k ont été validées. 
Voici les langues qui composent le corpus :
```
Abkhaz, Arabic, Armenian, Assamese, Azerbaijani, Basaa, Bashkir, Basque, Belarusian, Breton, Bulgarian, Catalan, Central Kurdish, Chinese (China), Chinese (Hong Kong), Chinese (Taiwan), Chuvash, Czech, Danish, Dhivehi, Dutch, English, Erzya, Esperanto, Estonian, Finnish, French, Frisian, Galician, Georgian, German, Greek, Guarani, Hakha Chin, Hausa, Hindi, Hungarian, Igbo, Indonesian, Interlingua, Irish, Italian, Japanese, Kabyle, Kazakh, Kinyarwanda, Kurmanji Kurdish, Kyrgyz, Latvian, Lithuanian, Luganda, Macedonian, Malayalam, Maltese, Marathi, Moksha, Mongolian, Norwegian Nynorsk, Odia, Persian, Polish, Portuguese, Punjabi, Romanian, Romansh Sursilvan, Romansh Vallader, Russian, Sakha, Santali (Ol Chiki), Serbian, Slovak, Slovenian, Sorbian, Upper, Spanish, Swahili, Swedish, Tamil, Tatar, Thai, Turkish, Ukrainian, Urdu, Uyghur, Uzbek, Vietnamese, Votic, Welsh
```

Voici les metadonnees disponibles :
```py
{
  'client_id': 'd59478fbc1ee646a28a3c652a119379939123784d99131b865a89f8b21c81f69276c48bd574b81267d9d1a77b83b43e6d475a6cfc79c232ddbca946ae9c7afc5', 
  'path': 'et/clips/common_voice_et_18318995.mp3', 
  'audio': {
    'path': 'et/clips/common_voice_et_18318995.mp3', 
    'array': array([-0.00048828, -0.00018311, -0.00137329, ...,  0.00079346, 0.00091553,  0.00085449], dtype=float32), 
    'sampling_rate': 48000
  }, 
  'sentence': 'Tasub kokku saada inimestega, keda tunned juba ammust ajast saati.', 
  'up_votes': 2, 
  'down_votes': 0, 
  'age': 'twenties', 
  'gender': 'male', 
  'accent': '', 
  'locale': 'et', 
  'segment': ''
}
```

Les premières données ont été publiées en 2017 et le corpus continue de s'agrandir encore aujourd'hui.

### Type de prédiction

Ce corpus peut réaliser des tâches de classification (reconnaissance des mots, du locuteur etc.).

### A quel modèle il a servi

Ce corpus a déjà servi a quasiment 200 modèles répertoriés sur HuggingFace. Par exemple, plusieurs modèles Nvidia comme NeMo Canary, un modèle d'ASR en 4 langues (Anglais, Allemand, Français, Espagnol) et de traduction de l'Allemand/Français/Espagnol vers l'Anglais et de l'Anglais vers ces 3 langues. Un deuxième modèle Nvidia est Parakeet RNNT 1.1B, qui réalise des tâches de transcription automatique d'extraits audio vers de l'anglais écrit en minuscules.
Enfin, ce corpus a aussi beaucoup servi pour des modèles Wav2Vec.

### Constitution de mon propre corpus

Le Common Voice est constitué uniquement d'extraits de parole spontanée, j'ai donc pour projet de constituer mon corpus à partir de vidéos YouTube. Pour cela, il faudra que je récupère des URLS ainsi que quelques métadonnées sur les vidéos pour ensuite récupérer l'audio de ces vidéos. 

## TD Cours n°2

### Récupération automatique du corpus

Pour récupérer mon corpus, je travaille à partir de la librairie Python `pytube`, qui me permet à partir du lien d'une playlist youtube de récupérer automatiquement tous les urls de cette playlist.
J'ai choisi dans ma playlist de prendre des vidéos de Konbini pour plusieurs raisons :
- Le corpus est propre d'un point de vue de l'enregistrement
- Le locuteur change à chaque vidéo et son nom est présent dans le titre de la vidéo
- Le locuteur est généralement une personnalité célèbre, ce qui facilite grandement la recherche d'éventuelles métadonnées
- La prise de parole est spontanée
- Il y a assez peu de moment "parasites" (interlocuteur par exemple)
- Toutes ces vidéos sont sur la même chaîne youtube à l'origine

### Récupération des métadonnées

Concernant la structure finale de mon corpus, je ne peux pas espérer obtenir exactement les mêmes métadonnées que le Mozilla Common Voice, car ce corpus et le mien auront été constitué de manières complètement différentes. Mon corpus de référence étant un corpus participatif, les métadonnées sur les locuteurs ont été données par les volontaires au moment de s'enregister. Etant donné que nous devons quant à nous scrapper le web, je peux obtenir un certain nombre de métadonnées automatiquement, mais pas nécessairement les mêmes.

Voici donc les métadonnées que je peux collecter :
- Transcription de l'audio
- Titre de la vidéo
- Longueur de la vidéo
- Date de publication
- Auteur de publication
- Nombre de vues

Toutes ces données ont été enregistrées au format json.

### Transcription de l'audio

J'ai voulu dans un premier temps utiliser la librairie `pytube` pour récupérer la transcription de l'audio, mais avec cette librairie je ne pouvais pas récupérer une transcription automatique.

J'ai donc utilisé `whisper` et son model `utlarge-v2` pour obtenir une transcription. J'ai réalisé 2 fichiers de transcription : le premier qui conserve les timecodes, et le second avec les données brutes. Par la suite je peux envisager de générer une transcription au format `textgrid` qui est bien plus adapté pour travailler sur un corpus oral (potentiellement avec l'outil MFA).

### Ce dépôt

J'ai poussé sur ce dépôt un échantillon de 7 vidéos afin que vous puissiez voir la structure finale que crée mon script, ainsi que le script python qui génère le corpus. Comme vous pouvez le voir, ce script génère cela à partir d'un unique lien (celui vers la playlist youtube).

## TD Cours n°3

J'ai créé un csv avec les données qui réunit les métadonnées des fichiers json et les transcriptions. Le script qui réalise cette tâche est [`create_csv.py`](src/create_csv.py) et le csv obtenu est [ici](data/data.csv).

## TD Cours n°4

Pour ce TP, j'ai realisé 4 plots differents sur le corpus :
- le nombre de vues en fonction de la longueur de la video (courbe)
- le nombre de tokens par video (barplot)
- le nombre de tokens par plot en fonction de la longueur de l'enregistrement (courbe)
- la loi de Zipf


Tous les plots sont disponibles dans le dossier [`plots`](plots).

## TD Cours n°5

J'ai choisi de mesurer la corrélation entre la longueur de la vidéo et le nombre de tokens obtenus pour chaque transcription.

Le programme qui calcule cette corrélation est [`correlation.py`](src/correlation.py).

Le resultat est le suivant : 
```
PearsonRResult(statistic=0.9741186978556917, pvalue=9.920797062076906e-14)
```
On voit donc que ces deux variables sont corrélées positivement et que la p-value montre que cela est très significatif. Cela est cohérent par rapport à notre corpus et au fait qu'a priori, plus la vidéo sera longue, plus le nombre de phrases sera nombreux. Je n'ai donc pas de traitement supplémentaire à faire pour améliorer la p value.

La deuxième partie du TP est de split le corpus est test et train. Je n'ai pas enregistré le résultat sur le git pour ne pas avoir trop de corpus sur le dépôt, mais le script qui fait cela est [`split.py`](src/split.py).


