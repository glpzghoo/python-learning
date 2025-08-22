number = int(input('Тоо оруулна уу: '))

if number == 0:
    print('Тоо тэг ба эерэг байна!')
elif number % 2 == 0:
    if number < 0: 
        print('Тоо тэгш ба сөрөг байна!')
    else:
        print('Тоо тэгш ба эерэг байна!')
else: 
    if number < 0:
        print('Тоо сондгой ба сөрөг байна!')
    else: 
        print('Тоо сондгой ба эерэг байна!')