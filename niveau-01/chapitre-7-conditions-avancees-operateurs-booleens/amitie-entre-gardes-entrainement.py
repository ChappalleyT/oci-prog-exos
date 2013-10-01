##################################
# fichier amitie-entre-gardes-entrainement.py
# nom de l'exercice :  Amitié entre gardes
# url : http://www.france-ioi.org/algo/task.php?idChapter=648&idTask=0&sTab=task&iOrder=5
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
date2 = int(input())
date3 = int(input())
date4 = int(input())
if (date3>=date1) and (date4<=date2)or (date1>=date3) and (date2<=date4)or  (date3>=date1) and (date3<=date2) and (date4>=date2)or (date1>=date3) and (date1<=date4) and (date2>=date4):
   print("Amis")
else:
   print("Pas amis")
   
   
   
