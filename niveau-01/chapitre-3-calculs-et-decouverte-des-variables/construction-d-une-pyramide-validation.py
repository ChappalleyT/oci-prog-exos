##################################
# fichier construction-d-une-pyramide-validation.py
# nom de l'exercice :  Construction d'une pyramide
# url : http://www.france-ioi.org/algo/task.php?idChapter=644&idTask=0&sTab=task&iOrder=19
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
a=17
b=a*a*a
for loop in range(8):
   a=a-2
   b=b+a**3   
print(b)
