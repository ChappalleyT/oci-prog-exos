##################################
# fichier 03-deux-rectangles-obligatoire.py
# nom de l'exercice : Deux rectangles
# url : http://www.france-ioi.org/algo/task.php?idChapter=509&idTask=0&sTab=task&iOrder=5
# type : obligatoire
#
# Chapitre : chapitre-4-fonctions
#
# Compétence développée : 
#
# auteur : 
##################################

# chargement des modules


# mettre votre code ici

def rectangle(nbLignes,nbColonnes,caractereAffiche):
   for loop in range(nbLignes):
      for loop in range(nbColonnes):
         print(caractereAffiche,end="")
      print()
       
rectangle(4,10,'X')
rectangle(6,5,'O')
