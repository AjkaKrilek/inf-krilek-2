m = 0
p = 0
while m != 'koniec':
    m = input('zadaj meno:')
    if m != 'koniec':
        p = len(m)
        print(m, ',pocet pismen:',p)