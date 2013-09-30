##################################
# fichier la-grande-braderie-validation.py
# nom de l'exercice :  La Grande Braderie
# url : http://www.france-ioi.org/algo/task.php?idChapter=843&idTask=0&sTab=task&iOrder=9
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

positionDepart= int(input())
largeurEmplacement= int(input())
nbVendeurs= int(input())
b=1
print(positionDepart)
for loop in range(nbVendeurs):
   a= positionDepart +(largeurEmplacement*b)
   print(a)
   b=b+1
