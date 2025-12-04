#Első feladat
#szam = int(input("Adj meg egy számot: "))

#fakt = 1
#i = 1

#while i <= szam:
#    fakt *= i
#    i += 1

#print("A(z)", szam, "faktoriálisa:", fakt)

#Második feladat
#n = int(input("Adj meg egy N számot: "))

#szorzat = 1

#for i in range(1, n + 1):
#    szorzat *= i

#print(f"Az 1-től {n}-ig terjedő számok szorzata: {szorzat}")

#Harmadik feladat

#szam = int(input("Adj meg egy számot: "))

#if szam <= 1:
#    print("Ez a szám nem prímszám.")
#else:
#    prim = True
#    for i in range(2, szam):
#        if szam % i == 0:
#            prim = False
#            break

#    if prim:
#        print("A szám prímszám.")
#    else:
#        print("A szám nem prímszám.")


#Negyedik feladat

szam= int(input("Adj meg egy számot: "))

osszeg=0

for i in str(abs(szam)):
    osszeg += int(i)

print(f"A(z) {szam} szám számjegyeinek összege: {osszeg}")