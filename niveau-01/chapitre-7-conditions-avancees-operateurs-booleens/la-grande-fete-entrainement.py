##################################
# fichier la-grande-fete-entrainement.py
# nom de l'exercice :  La grande fête
# url : http://www.france-ioi.org/algo/task.php?idChapter=648&idTask=0&sTab=task&iOrder=11
# type : entrainement
#
# Nom du chapitre : 
#
# Compétence développée : 
#
# auteur : 
##################################

# chargement des modules


# mettre votre code ici

DebutP = int(input())
FinP = int(input())
invites = int(input())
suspect = 0
for loop in range(invites):
   Debut = int(input())
   Fin = int(input())
   passuspect = (Fin < DebutP) or (FinP < Debut)
   if passuspect:
      suspect = suspect + 0
   if ( not (passuspect)):
      suspect = suspect + 1
print(suspect)
