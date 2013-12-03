##################################
# fichier 12-banquet-municipal-obligatoire.py
# nom de l'exercice : Banquet municipal
# url : http://www.france-ioi.org/algo/task.php?idChapter=651&idTask=0&sTab=task&iOrder=17
# type : obligatoire
#
# Chapitre : chapitre-2-decouverte-tableaux
#
# Compétence développée : 
#
# auteur : 
##################################

# chargement des modules


# mettre votre code ici

nbPersonnes = int(input())
nbChangements = int(input())
num= [0] * nbPersonnes
 
for Personne in range(nbPersonnes):
   num[Personne] = int(input())
 
for loop in range(nbChangements):
   premier = int(input())
   second = int(input())
   temp = num[premier]
   num[premier] = num[second]
   num[second] = temp
 
for Personne in range(nbPersonnes):
   print(num[Personne])
    
