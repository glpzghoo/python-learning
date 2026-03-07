def is_prime(number):
    if number < 2:
        return False
    
    for i in range(2, number):
        if number % i == 0:
            return False
        
    return True

user_input = int(input('Тоо оруулна уу~ '))

print(is_prime(user_input))