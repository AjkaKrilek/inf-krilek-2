z = int(input('zadaj zaciatok:'))
k = int(input('zadaj koniec:'))
v = 0
for a in range(z,k):
    if a%8==0:
        v += 1
print(v)