def contar_ate_vinte():
    #for i in range(21):
    #    print(i)

    #for i in range(0,21,1):
    #    print(i)

    contador = 0
    while(contador <= 20):
        print(contador)
        contador = contador +1

contar_ate_vinte()


def contar_ate_numero():
    numero = int(input("Digite um número inteiro: "))
    for i in range(numero + 1):
        print(i)

contar_ate_numero()


def imprime_tabuada_dois():
    for i in range(11):
        print(f"2 + {i} = {2 + i}")

imprime_tabuada_dois()


def tabuada_user():
    numero = int(input("Qual a tabuada desejada?"))
    for i in range(0,11):
        print(f"{numero} x {i} = {numero * i}")

tabuada_user()
