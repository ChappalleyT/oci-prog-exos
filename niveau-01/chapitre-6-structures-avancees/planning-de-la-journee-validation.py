##################################
# fichier planning-de-la-journee-validation.py
# nom de l'exercice :  Planning de la journée
# url : http://www.france-ioi.org/algo/task.php?idChapter=647&idTask=0&sTab=task&iOrder=2
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

position = int(input())
nbvillage = int(input())
nombre = 0
for lopp in range(nbvillage):
   positionV = int(input())
   if position-positionV >= -50:
      if position-positionV <=50:
         nombre=nombre+1
print(nombre)
