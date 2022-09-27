n = int(input('zadaj cislo'))
vysledok = 0
a = int
for a in range(1,n+1):
    if a%4==0 and a%7==0:
        vysledok += 1
print(vysledok)