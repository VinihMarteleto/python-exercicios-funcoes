lista_precos = [1500, 1000, 800, 2000]


def definir_taxa(preco):
    if preco > 2000:
        taxa = 0.2
    else:            
        taxa = 0.1
    return taxa

def calcular_imposto(lista_valores):
    imposto_total = 0
    for preco in lista_valores:
        taxa = definir_taxa(preco)
        imposto = preco * taxa
        imposto_total = imposto_total + imposto
    return imposto_total

imposto_lista1 = calcular_imposto(lista_precos)
print(f"O imposto total da lista 1 é R$ {imposto_lista1}")
 
lista2_precos = [500, 4000, 3200, 2600, 1000]
imposto_lista2 = calcular_imposto(lista2_precos)
print(f"O imposto total da lista 2 é R$ {imposto_lista2}")
calcular_imposto(lista2_precos)


def se_escreve_no_canal():
    print("Se escreve no canal Aula de Python")
    print("de um like e se inscreve no canal")
se_escreve_no_canal()
