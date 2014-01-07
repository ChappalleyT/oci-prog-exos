##################################
# fichier 03d-analyse-de-frequence-obligatoire.py
# nom de l'exercice : Analyse de fréquence
# url : http://www.france-ioi.org/algo/task.php?idChapter=595&idTask=0&sTab=task&iOrder=16
# type : obligatoire
#
# Chapitre : chapitre-3-chaines-de-caracteres
#
# Compétence développée : 
#
# auteur : 
##################################

# chargement des modules


# mettre votre code ici

nbLignes, nbMots = map(int, input().split(" "))
histogramme = [0] * 101
for loop in range(nbLignes):
   mots = input().split(" ")
   for idMot in range(nbMots):
      longueur = len(mots[idMot])
      histogramme[longueur] = histogramme[longueur] + 1
for longueur in range(101):
   if histogramme[longueur] > 0:
      print("{} : {}".format(longueur, histogramme[longueur]))
