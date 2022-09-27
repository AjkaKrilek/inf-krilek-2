c = 0
u = int(input('zadaj mi cislo:'))
counter = 1
scitovac = u
priemer = scitovac/(counter)
sucetp = 0
while u!=0:
  u = int(input('zadaj cislo:'))
  scitovac = scitovac + u
  counter = counter - 1
  if u%2 == 0:
    sucetp += u
print(priemer)
