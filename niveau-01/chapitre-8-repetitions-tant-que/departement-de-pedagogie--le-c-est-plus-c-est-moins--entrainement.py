##################################
# fichier departement-de-pedagogie--le-c-est-plus-c-est-moins--entrainement.py
# nom de l'exercice :  Département de pédagogie : le c'est plus, c'est moins !
# url : http://www.france-ioi.org/algo/task.php?idChapter=649&idTask=0&sTab=task&iOrder=5
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

nombre = int(input())
essais = 1
proposition = int(input())
while proposition != nombre:
   if proposition > nombre :
      print("c'est moins")
   else:
      print("c'est plus")
   essais = essais +1
   proposition=int(input())
print("Nombre d'essais nécessaires : ")
print(essais)
