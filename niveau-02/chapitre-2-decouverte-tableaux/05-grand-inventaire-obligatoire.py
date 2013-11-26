##################################
# fichier 05-grand-inventaire-obligatoire.py
# nom de l'exercice : Grand inventaire
# url : http://www.france-ioi.org/algo/task.php?idChapter=651&idTask=0&sTab=task&iOrder=7
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

quantite = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
nbOperations = int(input())
for loop in range(nbOperations ):
   numero = int(input())
   operation= int(input())
   quantite[numero] = quantite[numero] + operation
 
for numero in range(1, 11):
   print(quantite[numero])
