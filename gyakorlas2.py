#Első feladat
#szam = int(input("Adj meg egy számot: "))

#fakt = 1
#i = 1

#while i <= szam:
#    fakt *= i
#    i += 1

#print("A(z)", szam, "faktoriálisa:", fakt)

#Második feladat
n = int(input("Adj meg egy N számot: "))

szorzat = 1

for i in range(1, n + 1):
    szorzat *= i

print(f"Az 1-től {n}-ig terjedő számok szorzata: {szorzat}")