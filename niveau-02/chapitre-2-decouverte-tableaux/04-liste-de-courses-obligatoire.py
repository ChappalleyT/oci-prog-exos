##################################
# fichier 04-liste-de-courses-obligatoire.py
# nom de l'exercice : Liste de courses
# url : http://www.france-ioi.org/algo/task.php?idChapter=651&idTask=0&sTab=task&iOrder=5
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

total = 0
n=0
poids = [9, 5, 12, 15, 7, 42, 13, 10, 1, 20]
for loop in range(10):
   prix = int(input())
   total = total + prix * poids[n]
   n = n + 1
print(total)
