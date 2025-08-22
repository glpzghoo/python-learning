homeNumber = int(input('Эхний тоогоо оруулна уу: '))
awayNumber = int(input('2 дох тоогоо оруулна уу: '))

if(homeNumber > awayNumber): 
    print(f'Эхний тоо их байна! {homeNumber}')

elif (homeNumber < awayNumber): 
    print(f'2 дох тоо их байна! {awayNumber}')

else:
    print(f"2 тоо тэнцүү байна!")
