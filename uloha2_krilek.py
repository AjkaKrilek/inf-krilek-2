s = 0
p = 0
c = int(input('zadaj cislo:'))
while (s + c)<=100:
    p += 1
    print(c)
    s += c
    c = int(input('zadaj ine cislo:'))
    print('pocet je', p+1, "a sucet je",s)