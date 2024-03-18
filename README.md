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

Les premières données ont été publiées en 2017 et le corpus continue de s'agrandir encore aujourd'hui.

### Type de prédiction

Ce corpus peut réaliser des tâches de classification (reconnaissance des mots, du locuteur etc.).

### A quel modèle il a servi

Ce corpus a déjà servi a quasiment 200 modèles répertoriés sur HuggingFace. Par exemple, plusieurs modèles Nvidia comme NeMo Canary, un modèle d'ASR en 4 langues (Anglais, Allemand, Français, Espagnol) et de traduction de l'Allemand/Français/Espagnol vers l'Anglais et de l'Anglais vers ces 3 langues. Un deuxième modèle Nvidia est Parakeet RNNT 1.1B, qui réalise des tâches de transcription automatique d'extraits audio vers de l'anglais écrit en minuscules.
Enfin, ce corpus a aussi beaucoup servi pour des modèles Wav2Vec.
