##################################
# fichier maison-de-l-espion-entrainement.py
# nom de l'exercice :  Maison de l'espion
# url : http://www.france-ioi.org/algo/task.php?idChapter=648&idTask=0&sTab=task&iOrder=2
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

Xmin = int(input())
Xmax = int(input())
Ymin = int(input())
Ymax = int(input())
totalM = int(input())
nombre = 0
for loop in range (totalM):
   x =int(input())
   y =int(input())
   if (x <= Xmax) and (x>= Xmin) and (y <= Ymax) and (y>= Ymin):
      nombre = nombre +1
print (nombre)
