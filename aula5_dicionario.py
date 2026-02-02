# Aula 5 - Dicionários em Python
lista_produtos = ["iphone", "ipad", "macbook", "imac"]
lista_precos = [7000, 5000, 12000, 15000]

dic_produtos = {"ipad": 5000, "iphone": 7000, "macbook": 12000, "imac": 15000}

#pegar um item do dicionario
produto ="iphone"
posicao = lista_produtos.index(produto)
preco = lista_precos[posicao]
print(f"O preço do {produto} é R$ {preco}")

#com uso do dicionario
print(dic_produtos["iphone"])

#adicionar um item no dicionario
dic_produtos["airpods"] = 2000
print(dic_produtos)
#editar um item no dicionario
dic_produtos["iphone"] = dic_produtos["iphone"] * 0.9  #aplicando desconto de 10%
print(dic_produtos["iphone"])
print(dic_produtos)

#remover um item no dicionario
item_removido = dic_produtos.pop("macbook")
print(dic_produtos)
print(f"Item removido: {item_removido}")

#verificar se um item existe no dicionario
print("ipad" in dic_produtos)  #retorna True ou False
print("iphone" in dic_produtos.keys())
print("imac" in dic_produtos.values())  #retorna True ou False

produtos = list(dic_produtos.keys())
print(produtos)
precos = list(dic_produtos.values())
print(precos)   

#contagem de itens no dicionario
qtde = len(dic_produtos)
print(f"Quantidade de produtos no dicionario: {qtde}")

#exercicio
dic_produtos = {"ipad": 5000, "iphone": 7000, "macbook": 12000, "imac": 15000}
produto_buscado = input("Digite o nome do produto que deseja buscar: ")
produto_buscado = produto_buscado.lower()
produto_buscado = produto_buscado.strip()  #remover espaços em branco no início e no fim

if produto_buscado in dic_produtos:
    preco = dic_produtos[produto_buscado]
    print("Produto encontrado!")
    print(f"O preço do {produto_buscado} é R$ {preco}")
else:
    print("Produto não encontrado")