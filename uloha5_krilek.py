s = input('zadaj slovo:')
pz = 0
while s[0] != "x":
    d = len(s)
    pz += d
    slovo = input('zadaj dalsie slovo:')
    print('pocet je',pz)