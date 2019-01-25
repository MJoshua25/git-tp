import os
n=int(input("Entrez n : "))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)
os.system("pause")
