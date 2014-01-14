##################################
# fichier 04f-ngms-sns-vlls-obligatoire.py
# nom de l'exercice : ngms sns vlls
# url : http://www.france-ioi.org/algo/task.php?idChapter=595&idTask=0&sTab=task&iOrder=23
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

for loop in range(2):
   ligne = input()
   for idLettre in range(len(ligne)):
      car = ligne[idLettre]
      if (car != " " and car != "A" and car != "E" and car != "I" and
          car != "O" and car != "U" and car != "Y"):
         print(car, end = "")
   print()
