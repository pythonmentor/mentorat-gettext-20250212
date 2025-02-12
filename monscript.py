import gettext
import argparse

# Configuration du parser d'arguments
parser = argparse.ArgumentParser(description="Programme multilingue")
parser.add_argument(
    "-l", "--lang", type=str, help="language (ex: fr_CH, fr_FR, us_US)", default="fr_CH"
)
parser.add_argument("n", type=int, help="number for the test of plural")
args = parser.parse_args()


# Configuration de l'internationalisation
lang = gettext.translation(
    "monexemple", localedir="locales", languages=[args.lang], fallback=False
)
_ = lang.gettext
ngettext = lang.ngettext

# Code applicatif
print(_("Hello, World!"))  # Affichera "Bonjour, le monde!"
print(ngettext("{n} means singular", "{n} means plural", args.n).format(n=args.n))
