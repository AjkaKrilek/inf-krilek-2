a=int(input('zadaj hodnotu a:'))
b=int(input('zadaj hodnotu b:'))
c=int(input('zadaj hodnotu c:'))
if a+b>c:
    print('hodnoty su stranami trojuholnika')
    if a==b==c:
        print('je rovnostranny')
    elif a==b:
        print('je rovnoramenny')
    elif a**2+b**2==c**2:
        print('je pravouhly')
    else:
        print('roznostranny')
else:
    print('nie je stranami trojuholnika')