##################################
# fichier socles-pour-statues-validation.py
# nom de l'exercice :  Socles pour statues
# url : http://www.france-ioi.org/algo/task.php?idChapter=843&idTask=0&sTab=task&iOrder=14
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

a=int(input())
b=int(input())
c=a*a
for loop in range(a-b):
   c=c+(a-1)*(a-1)
   a=a-1
print(c)
