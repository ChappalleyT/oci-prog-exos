##################################
# fichier course-avec-les-enfants-validation.py
# nom de l'exercice :  Course avec les enfants
# url : http://www.france-ioi.org/algo/task.php?idChapter=644&idTask=0&sTab=task&iOrder=18
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
a=0
for loop in range(10):
   a=a+1
   for loop in range(a):
       droite()
   ramasser()
   for loop in range (a):
       gauche()
   deposer()
       
     
