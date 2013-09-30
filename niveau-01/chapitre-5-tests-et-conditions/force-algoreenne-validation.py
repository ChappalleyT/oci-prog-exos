##################################
# fichier force-algoreenne-validation.py
# nom de l'exercice :  Force algoréenne
# url : http://www.france-ioi.org/algo/task.php?idChapter=646&idTask=0&sTab=task&iOrder=1
# type : validation
#
# Nom du chapitre : 
#
# Compétence développée : 
#
# auteur : 
##################################

# chargement des modules


# mettre votre code 

nbPersonnes = int(input())
somme1=0
somme2=0
for loop in range (nbPersonnes):
   poid1 = int(input())
   poid2 = int(input())
   somme1 = somme1+ poid1
   somme2 = somme2+ poid2
if somme1 > somme2:
   print("L'équipe 1 a un avantage")
else:
   print("L'équipe 2 a un avantage")
print("Poids total pour l'équipe 1 : ", end = "")
print(somme1)
print("Poids total pour l'équipe 2 : ", end = "")
print(somme2)

