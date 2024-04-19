num = int(input("Validador de numero primo: "))
i = 1
x = 0

while i <= num:
    if num % i == 0:
        x += 1
    i += 1
    
if x == 2:
    print(f'{num} é um numero primo!!')
else:
    print(f'{num} não é um numero primo!!')
    

