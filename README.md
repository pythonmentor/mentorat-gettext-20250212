# Création des fichiers de traduction

## Dépendances à installer

Commencez par installer les outils nécessaires à la traduction. Que ce soit sur Windows, MacOS ou Linux, il s'agit d'installer GNU Gettext. 

- [Installation de Gettext sous Windows](https://mlocati.github.io/articles/gettext-iconv-windows.html)
- Installation de GNU Gettext sous MacOS : `$ brew install gettext`
- Installation de GNU Gettext sous Debian ou Ubuntu ou les linux basés sur apt : `$ sudo apt install gettext`
- Installation de GNU Gettext sous Fedora: `$ sudo dnf install gettext`

## Création des fichiers de traduction

Une fois que le programme est écrit en utilisant le module gettext de la bibliothèque standard, voici les opérations à effectuer pour que l'internalisation soit effective. 

- Pour extraire les chaines de caractères : `$ xgettext -o locales/monexemple.pot monscript.py`
- Pour générer un fichier de traduction au format .po : `$ msginit -l fr_FR -o locales/fr_FR/LC_MESSAGES/monexemple.po -i locales/monexemple.pot` ou `msginit -l fr_CH -o locales/fr_CH/LC_MESSAGES/monexemple.po -i locales/monexemple.pot`
- Pour compiler le fichier le traduction : `$ msgfmt -o locales/fr_FR/LC_MESSAGES/monexemple.mo locales/fr_FR/LC_MESSAGES/monexemple.po` ou `$ msgfmt -o locales/fr_CH/LC_MESSAGES/monexemple.mo locales/fr_CH/LC_MESSAGES/monexemple.po`