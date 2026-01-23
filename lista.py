# Exemplo de listas em Python
Vendas = [100, 200, 300, 400, 500]
print(Vendas[-1])  # Acessa o último elemento da lista

qtde_vendas = len(Vendas)
print(qtde_vendas)  # Imprime o tamanho da lista

#soma dos elementos da lista
total_vendas = sum(Vendas)
print(total_vendas)

#valor maximo e minimo
print(max(Vendas))
print(min(Vendas))
print(total_vendas / len(Vendas))  # média das vendas

#encontrar um elemento na lista

lista_produtos = ["camiseta", "calça", "tênis", "bermuda"]
print("calça" in lista_produtos)  # Verifica se "calça" está na lista
posicao = lista_produtos.index("calça")
print(posicao)  # Imprime a posição de "calça" na lista

pedaço_lista = lista_produtos[posicao:]
print(pedaço_lista)  # Imprime o pedaço da lista a partir de "calça"

# editar um elemento da lista
lista_produtos = [5000, 15000, 25000, 35000]
novo_valor = lista_produtos[1] * 1.1  # Aumenta o primeiro valor em 10%
lista_produtos[1] = novo_valor
print(lista_produtos)  # Imprime a lista atualizada

