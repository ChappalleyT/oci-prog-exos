##################################
# fichier nombre-de-jours-dans-le-mois-entrainement.py
# nom de l'exercice :  Nombre de jours dans le mois
# url : http://www.france-ioi.org/algo/task.php?idChapter=648&idTask=0&sTab=task&iOrder=4
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

mois = int(input())
if (mois < 4) or (mois>= 7) and (mois <=9):
   print("30")
if mois == 11:
   print ("29")
if (mois>=4) and (mois<=6) or (mois == 10):
   print("31")
