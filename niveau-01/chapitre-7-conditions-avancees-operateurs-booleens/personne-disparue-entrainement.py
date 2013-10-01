##################################
# fichier personne-disparue-entrainement.py
# nom de l'exercice :  Personne disparue
# url : http://www.france-ioi.org/algo/task.php?idChapter=648&idTask=0&sTab=task&iOrder=9
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

numero = int(input())
taille = int(input())
for loop in range(taille):
   nombre = int(input())
   Sortidelaville = (nombre == numero)
if Sortidelaville:
   print("Sorti de la ville")
else:
   print("Encore dans la ville")
      
