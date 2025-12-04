szam = int(input("Adj meg egy számot: "))

fakt = 1
i = 1

while i <= szam:
    fakt *= i
    i += 1

print("A(z)", szam, "faktoriálisa:", fakt)