##################################
# fichier 06-etude-de-marche-obligatoire.py
# nom de l'exercice : Étude de marché
# url : http://www.france-ioi.org/algo/task.php?idChapter=651&idTask=0&sTab=task&iOrder=9
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

nbProduits = int(input())
nbSouhaits = [0] * nbProduits
nbPersonnes = int(input())
for idPersonne in range(nbPersonnes):
   numeroProduit = int(input())
   nbSouhaits[numeroProduit] = nbSouhaits[numeroProduit] + 1
 
 
for numeroProduit in range(nbProduits):
   print(nbSouhaits[numeroProduit])
