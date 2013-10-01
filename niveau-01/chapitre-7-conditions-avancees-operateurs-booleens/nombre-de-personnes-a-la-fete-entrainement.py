##################################
# fichier nombre-de-personnes-a-la-fete-entrainement.py
# nom de l'exercice :  Nombre de personnes à la fête
# url : http://www.france-ioi.org/algo/task.php?idChapter=648&idTask=0&sTab=task&iOrder=6
# type : entrainement
#
# Nom du chapitre : 
#
# Compétence développée : 
#
# auteur : 
##################################

# chargement des modules


# mettre votre code ici

nbP = int(input())
nombre=0
nbmax = 0
for loop in range (nbP*2):
   EetS = int(input())
   if EetS > 0:
      nombre = nombre + 1
   else:
      nombre = nombre - 1
   if nombre > nbmax:
      nbmax= nombre
print(nbmax)
   
