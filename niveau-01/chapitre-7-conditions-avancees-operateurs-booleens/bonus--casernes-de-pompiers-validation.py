##################################
# fichier bonus--casernes-de-pompiers-validation.py
# nom de l'exercice :  Bonus : Casernes de pompiers
# url : http://www.france-ioi.org/algo/task.php?idChapter=648&idTask=0&sTab=task&iOrder=7
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

nbpair = int(input())
for loop in range(nbpair):
   xminA = int(input())
   xmaxA = int(input())
   yminA = int(input())
   ymaxA = int(input())
   xminB = int(input())
   xmaxB = int(input())
   yminB = int(input())
   ymaxB = int(input())
if (xmaxA>xminB) and (ymaxA>yminB)or (xmaxB>xminA)and (ymaxB>yminA):
   print("OUI")
else:
   print("NON")
