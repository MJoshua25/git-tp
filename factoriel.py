import os
#Début du programme
n=int(input("Entrez n : "))
#initialisation de la boucle
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)
os.system("pause")
