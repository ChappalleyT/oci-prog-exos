##################################
# fichier departement-de-medecine--controle-d-une-epidemie-entrainement.py
# nom de l'exercice :  Département de médecine : contrôle d'une épidémie
# url : http://www.france-ioi.org/algo/task.php?idChapter=649&idTask=0&sTab=task&iOrder=1
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

popTot = int(input())
Nbmalades=1
jours=1
while Nbmalades < popTot:
   Nbmalades = Nbmalades + (Nbmalades*2)
   jours=jours+1
print(jours)
