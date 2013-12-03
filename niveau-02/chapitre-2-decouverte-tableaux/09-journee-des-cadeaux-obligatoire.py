##################################
# fichier 09-journee-des-cadeaux-obligatoire.py
# nom de l'exercice : Journée des cadeaux
# url : http://www.france-ioi.org/algo/task.php?idChapter=651&idTask=0&sTab=task&iOrder=14
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
fortune = [0] * nbPersonnes
 
for loop in range(nbPersonnes):
   fortune[loop] = int(input())
 
fortune.sort()
 
if nbPersonnes % 2 == 1:
   milieu = (nbPersonnes - 1) // 2
   print( fortune[milieu] )
else:
   milieu = nbPersonnes // 2
   print( ( fortune[milieu - 1] + fortune[milieu] ) / 2 )
