def FizzBuzz():
    numero = int(input("Digite um numero: "))
    if numero % 5 == 0 and numero % 3 == 0:
        print('fizz-buzz')
    elif numero % 3 == 0:
        print('fizz')
    elif numero % 5 == 0:
        print('buzz')
    else:
        return numero


FizzBuzz()
