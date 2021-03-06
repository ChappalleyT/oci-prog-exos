##################################
# fichier 05-distance-obligatoire.py
# nom de l'exercice : Distance
# url : http://www.france-ioi.org/algo/task.php?idChapter=509&idTask=0&sTab=task&iOrder=9
# type : obligatoire
#
# Chapitre : chapitre-4-fonctions
#
# Compétence développée : 
#
# auteur : 
##################################

# chargement des modules


# mettre votre code ici

from math import *
 
def distanceEuclidienne(x1, y1, x2, y2):
   return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
 
def main():
   x1 = float(input())
   y1 = float(input())
   x2 = float(input())
   y2 = float(input())
   print(distanceEuclidienne(x1, y1, x2, y2))
