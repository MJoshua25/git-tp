def factoriel(n):
    fact=1
    if n==0 or n==1:
        fact=1
    else:
        fact=n*factoriel(n-1)
    return fact

n=int(input("Entrez n : "))
fac=factoriel(n)
print(fac)
