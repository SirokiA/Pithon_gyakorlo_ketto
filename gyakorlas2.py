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

#szam= int(input("Adj meg egy számot: "))

#osszeg=0

#for i in str(abs(szam)):
#    osszeg += int(i)

#print(f"A(z) {szam} szám számjegyeinek összege: {osszeg}")


#Ötödik feladat

#lista=[1,2,3,4,5,6,7,8,9,]

#negyzet=[]

#for i in lista:
#    negyzet.append(i**2)

#print("Eredeti lista:", lista)
#print("Négyzetre emelt lista:",negyzet)


#Hatodik feladat

#szemelyek = {}

#for i in range(5):
#    nev=input(f"Add meg a {i+1}. személy nevét: ")
#    kor=int(input(f"Add meg {nev} életkorát:"))
#    szemelyek[nev]= kor

#legidosebb_nev = max(szemelyek, key=szemelyek.get)
#legidosebb_kor = szemelyek[legidosebb_nev]

#print(f"A legidősebb személy: {legidosebb_nev}, életkor: {legidosebb_kor}")


#Hetedik feladat

#class Auto:
#    def __init__(self, marka, tipus, evjarat):
#        self.marka = marka
#        self.tipus = tipus
#        self.evjarat = evjarat

#    def adat(self):
#        print(f"Márka: {self.marka}, tipus: {self.tipus}, évjárat {self.evjarat}")

#auto1 = Auto("Toyota", "Corolla", 2015)
#auto2 = Auto("Ford", "Focus", 2018)

#auto1.adat()
#auto2.adat()


#Nyolcadik feladat

#class BankAccount:
#    def __init__(self,nev,egyenleg=0):
#        self.nev = nev
#        self.egyenleg = egyenleg

#    def deposit(self, osszeg):
#        self.egyenleg += osszeg
#        print(f"{osszeg} befizetve. új egyenleg: {self.egyenleg}")

#    def withdraw(self, osszeg):
#        if osszeg > self.egyenleg:
#            print("Nincs elég pénz a számlásn!")

#    def get_balance(self):
#        return self.egyenleg
    

#szamla1 = BankAccount("Anna", 1000)
#szamla2 = BankAccount("Béla", 500)

#szamla1.deposit(200)   # Anna számlája: 1200
#szamla2.deposit(300)   # Béla számlája: 800

#print(f"Anna egyenlege: {szamla1.get_balance()}")
#print(f"Béla egyenlege: {szamla2.get_balance()}")



#Kilencedik feladat

#class Student:
#    def __init__(self, nev, eletkor, atlag):
#        self.nev = nev
#        self.eletkor = eletkor
#        self.atlag = atlag

#    def adat (self):
#        print(f"Név: {self.nev}, Életkor {self.eletkor}, Átlag {self.atlag}")

#tanulok = []

#for i in range(3):
#        nev = input(f"Add meg az {i+1}. tanuló nevét:")
#        eletkor = int(input(f"Add meg {nev} életkorát:"))
#        atlag = int(input(f"Add meg {nev} átlagát:"))
#        tanulok.append(Student(nev, eletkor, atlag))

#legjobb = max(tanulok, key=lambda x: x.atlag)

#print(f"A legjobb átlagú tanuló: {legjobb.nev}, Átlag: {legjobb.atlag}")



#Tizedik feladat

class Allat:
    def __init__(self, nev, eletkorr):
        self.nev = nev
        self.eletkor = eletkorr

    def adat(self):
        print(f"Név: {self.nev}, Életkor: {self.eletkor}")

class Kutya(Allat):
    def __init__(self, nev, eletkor, fajta):
        super().__init__(nev, eletkor)
        self.fajta = fajta
    
    def hang(self):
        print(f"{self.nev} mondja: Vau-Vau")

    def adat(self):
        super(). adat()
        print(f"Fajta: {self.fajta}")

class Macska(Allat):
    def __init__(self, nev, eletkor, szin):
        super().__init__(nev, eletkor)
        self.szin =szin

    def hang(self):
        print(f"{self.nev} mondja: Miau")

    def adat(self):
        super(). adat()
        print(f"Szín: {self.szin}")



#kutyus = Kutya("Bodri", 3, "Golden Retriever")
#macska = Macska("Cirmos", 2, "Szürke")

#kutyus.adat()
#kutyus.hang()

#print()  

#macska.adat()
#macska.hang()


kutya_nev=input(f"Kérem a kutya nevét:")
kutya_eletkor=int(input(f"Kérem {kutya_nev} életkorát:"))
kutya_fajta=input(f"Add meg {kutya_nev} fajtáját:")

macska_nev=input(f"Add meg a mcsaka nevét:")
macska_eletkor=int(input(f"add meg {macska_nev} életkorát: "))
macska_szin=input(f"Add meg {macska_nev} szinét: ")

kutyus = Kutya(kutya_nev, kutya_eletkor, kutya_fajta)
macska = Macska(macska_nev, macska_eletkor, macska_szin)

print("\n-- Kutya --")
kutyus.adat()
kutyus.hang()

print("\n-- Macska --")
macska.adat()
macska.hang()