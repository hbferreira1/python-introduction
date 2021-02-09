def exponenciacao():
    n1 = int(input("número: "))
    n2 = int(input("elevado a: "))

    for i in range(20):
        print(n1 **n2)
        n2 = n2 + 1
        print(n1 ** n2)
        if (n1 ** n2) >= 1000:
            break
    print("O número já é maior que 1000")


exponenciacao()
