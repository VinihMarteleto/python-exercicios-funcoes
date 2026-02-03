#for e repetições em Python
for i in range(10):
    print("python é legal")

lista_precos = [5000, 7000, 12000, 15000]
taxa_imposto = 0.1 #10% de imposto

#for preco in lista_precos:
#    imposto = preco * taxa_imposto #calculando 10% de imposto
#    print(f"Preço: R$ {preco} - Imposto: R$ {imposto}")

#exemplos

for preco in lista_precos:
    if preco > 5000:
        taxa =0.15
    else:
        taxa =0.1
    imposto = preco * taxa
    print(f"Preço: R$ {preco} - Imposto: R$ {imposto}")

    #exemplo 2
    total_imposto = 0

    for preco in lista_precos:
        if preco > 10000:
           taxa = 0.15
        else:
              taxa = 0.1
        imposto = preco * taxa

        total_imposto = total_imposto + imposto

    print(f"Total de imposto: R$ {total_imposto}")
print(f"Preço: R$ {preco} - Imposto: R$ {imposto}")

#exempo 3 - usando dicionario
vendas_25 = {"janeiro": 15000, "fevereiro": 18000, "março": 12000, "abril": 15000}
vendas_26 = {"janeiro": 16000, "fevereiro": 29000, "março": 51100, "abril": 18000}

#calcular o total de crescimento de vendas de 2025 para 2026
#15000 / 16000 -1 = -> mostrar o crescimento em porcentagem

for mes in vendas_25:
    valor_25 = vendas_25[mes]
    valor_26 = vendas_26[mes]
    crescimento = (valor_26 / valor_25) - 1
    print(f"Mês: {mes} - Crescimento: {crescimento:.1%}")

#exercicio
print("Lista de produtos e preços:")

produtos = {"meia": 20, "camiseta": 35, "calça": 80, "tênis": 120, "boné": 25, "jaqueta": 150, "mochila": 90, "óculos": 60, "relógio": 200, "carteira": 45, "cinto": 30, "luvas": 25, "cachecol": 40, "chapéu": 70, "blusa": 55, "bermuda": 50, "sandália": 80, "meias": 15, "pijama": 65, "roupão": 100}
for produto, preco in produtos.items():
    if preco > 50:
        print(f"{produto.capitalize()}: R$ {preco}")
    else:
        print(f"{produto.capitalize()}: R$ {preco} - Produto em promoção!")

#calcular o total do estoque
total_estoque = 0
for preco in produtos.values():
    total_estoque += preco 
print(f"Total do estoque: R$ {total_estoque}")

#calcular o preço médio dos produtos
preco_medio = total_estoque / len(produtos)
print(f"Preço médio dos produtos: R$ {preco_medio:.2f}")

#listar produtos com preço acima da média
print("Produtos com preço acima da média:")
for produto, preco in produtos.items():
    if preco > preco_medio:
        print(f"{produto.capitalize()}: R$ {preco}")
#listar produtos com preço abaixo da média
print("Produtos com preço abaixo da média:")
for produto, preco in produtos.items():
    if preco < preco_medio:
        print(f"{produto.capitalize()}: R$ {preco}")

#calcular o imposto total sobre os produtos (imposto de 8%)

imposto_total = 0
for preco in produtos.values():
    imposto = preco * 0.08
    imposto_total += imposto

print(f"Total de imposto: R$ {imposto_total:.2f}")

