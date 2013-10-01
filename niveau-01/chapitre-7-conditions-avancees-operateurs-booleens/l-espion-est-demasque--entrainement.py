##################################
# fichier l-espion-est-demasque--entrainement.py
# nom de l'exercice :  L'espion est démasqué !
# url : http://www.france-ioi.org/algo/task.php?idChapter=648&idTask=0&sTab=task&iOrder=14
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

nbPersonnes = int(input())
nombre = 0
for loop in range (nbPersonnes):
   taille = int(input())
   age = int(input())
   poid = int(input())
   cheval = int(input())
   cheveux = int(input())
   if (taille>=178) and (taille<=182):
      nombre = nombre+1
   if age>=34:
      nombre = nombre+1
   if poid < 70:
      nombre = nombre+1
   if cheval == 0:
      nombre = nombre+1   
   if cheveux == 1:
      nombre = nombre+1
   if nombre == 5:
      print("Très probable")
   elif (nombre==4) or (nombre==3):
      print("Probable")
   elif  nombre==0:
      print("Impossible")
   elif (nombre==1) or (nombre==2):
      print("Peu probable")
