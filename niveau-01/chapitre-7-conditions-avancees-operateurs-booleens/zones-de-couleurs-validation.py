##################################
# fichier zones-de-couleurs-validation.py
# nom de l'exercice :  Zones de couleurs
# url : http://www.france-ioi.org/algo/task.php?idChapter=648&idTask=0&sTab=task&iOrder=15
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

N = int(input())
for loop in range (N):
   X = int(input())
   Y = int(input())
   if (X>15) and (X<45) and (Y>60) and (Y<70) or (X>60) and (X<85) and (Y>60) and (Y<70):
      print("Dans une zone rouge")
   if (X>10) and (X<25) and (Y>10) and (Y<55) or (X>25) and (X<50) and (Y>10) and (Y<20) or (X>25) and (X<50)and (Y>45) and (Y<55) or (X>50) and (X<85) and (Y>10) and (Y<55):
      print("Dans une zone bleue")
   if (X>0) and (X<90) and (Y>0) and (Y<10) or (X>0) and (X<10) and (Y>10) and (Y<55) or (X>0) and (X<15) and (Y>55) and (Y<70) or (X>85) and (X<90) and (Y>0) and (Y<70) or (X>15) and (X<85) and (Y>55) and (Y<60) or (X>45) and (X<60 and (Y>60) and (Y<70)or (X>25) and(X<50) and (Y>20) and (Y<45):
      print("Dans une zone jaune")
   else:
      print("En dehors de la feuille")

