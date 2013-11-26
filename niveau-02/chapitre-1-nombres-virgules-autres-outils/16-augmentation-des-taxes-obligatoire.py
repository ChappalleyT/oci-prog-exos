##################################
# fichier 16-augmentation-des-taxes-obligatoire.py
# nom de l'exercice : Augmentation des taxes
# url : http://www.france-ioi.org/algo/task.php?idChapter=650&idTask=0&sTab=task&iOrder=20
# type : obligatoire
#
# Chapitre : chapitre-1-nombres-virgules-autres-outils
#
# Compétence développée : 
#
# auteur : 
##################################

# chargement des modules


# mettre votre code ici

from math import *

taxe1 = float(input())
taxe2 = float(input())
prix = float(input())

nouveauprix = prix / (1+taxe1/100) * ( 1+taxe2/100)
nouveauprix = round(nouveauprix *100) / 100
print(nouveauprix)
