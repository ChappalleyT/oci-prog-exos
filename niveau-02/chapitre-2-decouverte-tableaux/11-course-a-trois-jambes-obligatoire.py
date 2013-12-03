##################################
# fichier 11-course-a-trois-jambes-obligatoire.py
# nom de l'exercice : Course à trois jambes
# url : http://www.france-ioi.org/algo/task.php?idChapter=651&idTask=0&sTab=task&iOrder=16
# type : obligatoire
#
# Chapitre : chapitre-2-decouverte-tableaux
#
# Compétence développée : 
#
# auteur : 
##################################

# chargement des modules


# mettre votre code ici

nbParticipants = int(input())
num = [0] * nbParticipants
for loop in range(nbParticipants):
    num[loop] = int(input())

num.sort()

for premier in range(nbParticipants // 2):
    deuxieme = nbParticipants - 1 - premier
    print("{} {}".format (num[premier], num[deuxieme]) )
    
