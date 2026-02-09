lista_vendas = [1000, 2000, 1500, 3000, 2500]
tupla_vendas = (1000, 2000, 1500, 3000, 2500)
print(lista_vendas[0])  #acesso por índice
print(tupla_vendas[0])  #acesso por índice
#tuplas são imutáveis, ou seja, não podem ser alteradas depois de criadas
#tuplas são mais rápidas que listas, pois são imutáveis

#bonus 1 : Reais por venda feita
# bonus 2: 1% do valor das vendas 

def calcular_bonus(lista_vendas):
    bonus1 = 2 * len(lista_vendas)  #bonus 1: R$ 2 por venda feita
    bonus2 = sum(lista_vendas) * 0.01  #bonus 2: 1% do valor das vendas
    return bonus1, bonus2

vendas = [100, 250, 400, 1000]
bonus1, bonus2 = calcular_bonus(vendas)  #recebendo os valores retornados pela função
# unpacking da tupla
print(f"Bonus 1: R$ {bonus1}")
print(f"Bonus 2: R$ {bonus2}")

lista_telas = [(1090, 1080), (2140, 1080)]
for altura, largura in lista_telas:
    print(altura, largura)      

# bonus 1: R$2 por venda feita
# bonus 2: 1% do valor de vendas

def calcular_bonus(lista_vendas):
    bonus1 = 2 * len(lista_vendas)
    bonus2 = 0.01 * sum(lista_vendas)
    return bonus1, bonus2

vendas = {
    "André": [1000, 500, 300, 5000, 1500, 80, 3000],
    "Andressa": [1500, 9000, 300, 150, 1500, 120, 130, 55, 500, 8500],
    "Alan": [800, 100],
    "Ana": [800, 900, 950, 1200, 1600, 130, 50, 50, 50, 50, 65, 60, 70, 70, 70, 200, 180, 100, 120, 110, 130, 140]
}

# bonus de cada funcionario
# total de bonus 1 pago aos funcionários
# total de bonus 2 pago aos funcionários


total_bonus1 = 0
total_bonus2 = 0
for vendedor in vendas:
    bonus1, bonus2 = calcular_bonus(vendas[vendedor])
    print(f"Bonus do {vendedor}: R$ {bonus1} + R$ {bonus2}")
    total_bonus1 = total_bonus1 + bonus1
    total_bonus2 = total_bonus2 + bonus2
print(f"Total de bonus 1 pago aos funcionários: R$ {total_bonus1}")
print(f"Total de bonus 2 pago aos funcionários: R$ {total_bonus2}") 