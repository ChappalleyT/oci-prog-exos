##################################
# fichier le-juste-prix-validation.py
# nom de l'exercice :  Le juste prix
# url : http://www.france-ioi.org/algo/task.php?idChapter=647&idTask=0&sTab=task&iOrder=8
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

nbM = int(input())
position = 0
positionV=0
prixmin = 1000000
for loop in range(nbM):
   position = position + 1
   prix = int(input())
   if prix <= prixmin:
      prixmin = prix
      positionV = position
print(positionV)
