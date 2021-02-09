def calculadora():
    op = input(''' 
escreva a operação matemática 
+ para adição 
- para subtração 
* para multiplicação 
/ para divisão 
''')

    n1 = int(input("Primeiro operador: "))
    n2 = int(input("Segundo operador: "))

    if op == '+':
        print('{} + {} = '.format(n1, n2))
        print(n1 + n2)

    elif op == '-':
        print('{} - {} = '.format(n1, n2))
        print(n1 - n2)

    elif op == '*':
        print('{} * {} = '.format(n1, n2))
        print(n1 * n2)

    elif op == '/':
        print('{} / {} = '.format(n1, n2))
        print(n1 / n2)

    else:
        print('Você não digitou um operador válido. Tente novamente')

    dnv()


def dnv():
    calc_dnv = input(''' 
    Deseja realizar outra operação? 
    digite 'S' para sim e 'N' para não 
    ''')

    if calc_dnv.upper() == 'S':
        calculadora()
    elif calc_dnv.upper() == 'N':
        print("Até mais! :)")
    else:
        dnv()


calculadora()