##################################
# fichier 07-convertisseur-d-unites-obligatoire.py
# nom de l'exercice : Convertisseur d'unités
# url : http://www.france-ioi.org/algo/task.php?idChapter=509&idTask=0&sTab=task&iOrder=14
# type : obligatoire
#
# Chapitre : chapitre-4-fonctions
#
# Compétence développée : 
#
# auteur : 
##################################

# chargement des modules


# mettre votre code ici

def pied(metre):
   return metre / 0.3048
    
def livre(gramme):
   return gramme * 0.002205
    
def farenheit(celcius):
   return 32 + celcius * 1.8
 
def afficher(valeur,unite):
   print("{} {}".format(valeur,unite))
 
nbValeurs = int(input())
for loop in range(nbValeurs):
   valeur,unite = input().split()
   valeur = float(valeur)
   if unite == 'm':
      afficher(pied(valeur),'p')
   elif unite == 'g':
      afficher(livre(valeur),'l')
   elif unite == 'c':
      afficher(farenheit(valeur),'f')
