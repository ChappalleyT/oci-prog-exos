##################################
# fichier espion-etranger-entrainement.py
# nom de l'exercice :  Espion étranger
# url : http://www.france-ioi.org/algo/task.php?idChapter=648&idTask=0&sTab=task&iOrder=1
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

date1 = int(input())
date2 = int (input())
entrees = int(input())
nombre = 0
for loop in range (entrees):
   valeur = int(input())
   if (valeur <= date2) and (valeur >= date1):
      nombre = nombre +1
print(nombre)
