nomes = ["João", "Maria", "Fulano", "Ciclano"]

def imprimir_nomes():
    print("1 -", nomes[0])
    print("2 -", nomes[1])
    print("3 -", nomes[2])
    print("4 -", nomes[3])

imprimir_nomes()


def imprime_primeiro_ultimo():
    print("Primeiro -", nomes[0])
    print("Último -", nomes[3])

imprime_primeiro_ultimo()


def imprime_segundo_terceiro():
    print("Segundo -", nomes[1])
    print("Terceiro -", nomes[2])

imprime_segundo_terceiro()

def substituir_alimentos():
    array_inicial = ["Macarrão", "Pepino", "Batata"]

    alimento1 = input("Digite o alimento 1: ")
    alimento2 = input("Digite o alimento 2: ")
    alimento3 = input("Digite o alimento 3: ")
    
    array_inicial[0] = alimento1
    array_inicial[1] = alimento2
    array_inicial[2] = alimento3

    print("1 -", array_inicial[0])
    print("2 -", array_inicial[1])
    print("3 -", array_inicial[2])

substituir_alimentos()
