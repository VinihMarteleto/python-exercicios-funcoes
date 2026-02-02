faturamento = 1000
custo = 600

lucro = faturamento - custo

if lucro > 0:
    print("lucro de R$", lucro)
else:
    print("prejuizo de R$", lucro)

print("Fim do programa")

# Exemplo 
produtos = ["iphone", "ipad", "macbook", "imac"]
novo_produto = input("Digite o nome do produto :")

if novo_produto in produtos:
    print("Produto já existe na lista")
else:
    print(f"{novo_produto} adicionado com sucesso")
    produtos.append(novo_produto)

print(produtos)
print("Fim do programa")

# Exemplo 2
vendas = 20000

if vendas >= 15000:
    bonus = 500
elif vendas >= 5000:
    bonus = 100
else:
    bonus = 0

print("Bonus do funcionario: R$", bonus)

# Exemplo 3
vendas_empresa = 200_000
meta_empresa = 100_000
vendas_funcionario = 11000

if vendas_funcionario >= 15000 and vendas_empresa >= meta_empresa:
    bonus = 500
elif vendas_funcionario >= 5000 and vendas_empresa >= meta_empresa:
    bonus = 100
else:
    bonus = 0

print("Bonus do funcionario: R$", bonus)
