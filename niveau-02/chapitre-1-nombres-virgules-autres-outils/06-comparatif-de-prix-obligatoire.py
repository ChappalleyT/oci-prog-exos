##################################
# fichier 06-comparatif-de-prix-obligatoire.py
# nom de l'exercice : Comparatif de prix
# url : http://www.france-ioi.org/algo/task.php?idChapter=650&idTask=0&sTab=task&iOrder=7
# type : obligatoire
#
# Chapitre : chapitre-1-nombres-virgules-autres-outils
#
# Compétence développée : 
#
# auteur : 
##################################

# chargement des modules


# mettre votre code ici

nbL= int(input())
for loop in range (nbL):
   poid = float(input())
   jours = float(input())
   prix = float(input())
   print(prix/poid)

