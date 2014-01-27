##################################
# fichier 04g-la-bataille-obligatoire.py
# nom de l'exercice : La bataille
# url : http://www.france-ioi.org/algo/task.php?idChapter=595&idTask=0&sTab=task&iOrder=24
# type : obligatoire
#
# Chapitre : chapitre-3-chaines-de-caracteres
#
# Compétence développée : 
#
# auteur : 
##################################

# chargement des modules


# mettre votre code ici
paquet1 = input()
paquet2 = input()
gagnantTrouve = False
nbEgales = 0
indice = 0
while not gagnantTrouve and indice < min(len(paquet1), len(paquet2)):
   if paquet1[indice] != paquet2[indice]:
      gagnantTrouve = True
      if paquet1[indice] < paquet2[indice]:
         print(1)
      elif paquet1[indice] > paquet2[indice]:
         print(2)
   else:
      nbEgales = nbEgales + 1
   indice = indice + 1  
    
if not gagnantTrouve:
   if len(paquet1) > len(paquet2):
      print(1)
   elif len(paquet1) < len(paquet2):
      print(2)
   else:
      print("=")
 
print(nbEgales)

