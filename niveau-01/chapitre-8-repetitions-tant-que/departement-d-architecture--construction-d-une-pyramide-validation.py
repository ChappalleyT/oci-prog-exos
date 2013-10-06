##################################
# fichier departement-d-architecture--construction-d-une-pyramide-validation.py
# nom de l'exercice :  Département d'architecture : construction d'une pyramide
# url : http://www.france-ioi.org/algo/task.php?idChapter=649&idTask=0&sTab=task&iOrder=6
# type : validation
#
# Nom du chapitre : 
#
# Compétence développée : 
#
# auteur : 
##################################

# chargement des modules


# mettre votre code ici

NbmaxP = int(input())
hauteur = 0
tot = 0
while NbmaxP-tot>= (hauteur+1)**2:
   tot = tot +(hauteur+1)**2
   hauteur = hauteur +1
print(hauteur)
print(tot)
   
