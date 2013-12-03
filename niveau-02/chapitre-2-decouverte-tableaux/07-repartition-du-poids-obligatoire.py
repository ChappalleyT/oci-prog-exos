##################################
# fichier 07-repartition-du-poids-obligatoire.py
# nom de l'exercice : Répartition du poids
# url : http://www.france-ioi.org/algo/task.php?idChapter=651&idTask=0&sTab=task&iOrder=10
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

nbCharrettes = int(input())
poids = [0.0] * nbCharrettes
 
poidsTotal = 0.0
for numero in range(nbCharrettes):
   poids[numero] = float(input())
   poidsTotal = poidsTotal + poids[numero]
 
poidsMoyen = poidsTotal / nbCharrettes
 
for numero in range(nbCharrettes):
   print(poidsMoyen - poids[numero])
