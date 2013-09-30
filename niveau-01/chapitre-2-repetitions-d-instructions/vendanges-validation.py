##################################
# fichier vendanges-validation.py
# nom de l'exercice :  Vendanges
# url : http://www.france-ioi.org/algo/task.php?idChapter=643&idTask=0&sTab=task&iOrder=20
# type : validation
#
# Nom du chapitre : 
#
# Compétence développée : 
#
# auteur : 
##################################

# chargement des modules


# mettre votre code ici

from robot import *
for loop in range(20):
   ramasser()
   for loop in range(15):
      droite()
   deposer()
   for loop in range(15):
      gauche()
