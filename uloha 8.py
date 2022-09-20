a=int(input('zadaj cislo:'))
if (a%10 + a%100 //10)%2==0:
    print('posledne dvojcifrie je parne')
else:
    print('posledne dvojcifrie je neparne')