##################################
# fichier 08-visite-de-la-mine-obligatoire.py
# nom de l'exercice : Visite de la mine
# url : http://www.france-ioi.org/algo/task.php?idChapter=651&idTask=0&sTab=task&iOrder=11
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

deplacInverse = [0, 2, 1, 3, 5, 4]
 
nbDeplac = int(input())
chemin = [0] * nbDeplac
 
for num in range(nbDeplac):
   chemin[num] = int(input())
 
for num in range(nbDeplac-1, -1, -1):
   deplac = chemin[num]
   print(deplacInverse[deplac])
