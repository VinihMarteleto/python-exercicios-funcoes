# 🐍 Curso Python - Exercícios Práticos Completos

Repositório com exercícios práticos de **Python** abrangendo desde conceitos fundamentais até APIs e módulos avançados. Este é um **curso completo** com 9 aulas que cobrem as principais estruturas e conceitos do Python.

---

## 📚 Conteúdo Completo

### 🔹 Aula 1 - Introdução a Strings e Formatação de Texto

**Arquivo:** `Aula1-codigo.py`

Aprenda a manipular e formatar strings em Python:

```python
# F-strings para formatação
faturamento = 1000
custo = 600
lucro = faturamento - custo
texto = f"o lucro foi de R${lucro} e o faturamento foi de R${faturamento}"
print(texto)

# Métodos de string
email = " EMAIL_FALSO@gmail.com "
email = email.lower()      # Converter para minúscula
email = email.strip()      # Remover espaços
print(len(email))          # Tamanho da string

# Encontrar posição de um caractere
posicao = email.find("@")
print(email[posicao:])     # Slicing

# Substituir parte da string
novo_email = email.replace("gmail.com", "yahoo.com.br")

# Capitalizar texto
nome = "vinicius marteleto"
nome = nome.capitalize()   # Vinicius marteleto
nome = nome.title()        # Vinicius Marteleto
nome = nome.upper()        # VINICIUS MARTELETO

# Formatação numérica
texto = f"Lucro: R${lucro:,.2f} | Margem: {(lucro/faturamento):.1%}"
```

**Conceitos:** F-strings, métodos de string (lower, upper, strip, capitalize, title, replace, find), slicing, formatação numérica

---

### 🔹 Aula 2 - Entrada de Dados e Conversão de Tipos

**Arquivo:** `Aula2-imputs.py`

Trabalhe com input do usuário e conversão entre tipos de dados:

```python
# Converter entrada de texto para número
faturamento = input("Preencha o faturamento (apenas números): ")
faturamento = faturamento.replace("R$", "").replace(",", ".")
faturamento = float(faturamento)  # Converter para float

custo = 600
lucro = faturamento - custo
print(lucro)

# Múltiplas entradas
vendas_dia1 = float(input("Vendas Dia 1: "))
vendas_dia2 = float(input("Vendas Dia 2: "))
print(vendas_dia1 + vendas_dia2)
```

**Conceitos:** `input()`, conversão de tipos (float, int, str), manipulação de string, tratamento de dados

---

### 🔹 Aula 3 - Listas e Operações de Array

**Arquivo:** `Aula3-lista.py`

Domine listas, uma das estruturas de dados mais importantes do Python:

```python
# Criar e acessar listas
vendas = [100, 200, 300, 400, 500]
print(vendas[-1])           # Último elemento: 500
print(len(vendas))          # Tamanho: 5

# Operações matemáticas
print(sum(vendas))          # Soma: 1500
print(max(vendas))          # Máximo: 500
print(min(vendas))          # Mínimo: 100
print(sum(vendas) / len(vendas))  # Média: 300

# Verificação e busca
lista_produtos = ["camiseta", "calça", "tênis", "bermuda"]
print("calça" in lista_produtos)  # True
posicao = lista_produtos.index("calça")  # Índice: 1

# Editar elementos
lista_valor = [5000, 15000, 25000, 35000]
lista_valor[1] = lista_valor[1] * 1.1  # Aumentar em 10%

# Adicionar e remover elementos
lista_produtos.append("meia")           # Adicionar ao final
lista_produtos.remove("tênis")          # Remover elemento
lista_produtos.insert(2, "carteira")    # Inserir em posição específica

# Concatenar listas
lista2_produtos = ["boné", "óculos"] + lista_produtos
```

**Conceitos:** Criação, indexação, slicing, métodos (append, remove, insert, index, count), operações (sum, max, min, len)

---

### 🔹 Aula 4 - Estruturas de Controle (IF/ELSE/ELIF)

**Arquivo:** `Aula-if.py`

Controle o fluxo do programa com condicionais:

```python
# IF/ELSE simples
faturamento = 1000
custo = 600
lucro = faturamento - custo

if lucro > 0:
    print("lucro de R$", lucro)
else:
    print("prejuizo de R$", lucro)

# Verificação em lista
produtos = ["iphone", "ipad", "macbook", "imac"]
novo_produto = input("Digite o nome do produto :")

if novo_produto in produtos:
    print("Produto já existe na lista")
else:
    print(f"{novo_produto} adicionado com sucesso")
    produtos.append(novo_produto)

# IF/ELIF/ELSE para múltiplas condições
vendas = 20000

if vendas >= 15000:
    bonus = 500
elif vendas >= 5000:
    bonus = 100
else:
    bonus = 0

print("Bonus do funcionario: R$", bonus)

# Operadores lógicos (AND, OR, NOT)
vendas_empresa = 200_000
meta_empresa = 100_000
vendas_funcionario = 11000

if vendas_funcionario >= 15000 and vendas_empresa >= meta_empresa:
    bonus = 500
elif vendas_funcionario >= 5000 and vendas_empresa >= meta_empresa:
    bonus = 100
else:
    bonus = 0
```

**Conceitos:** if/else, elif, operadores lógicos (and, or, not), comparações, verificação em listas

---

### 🔹 Aula 5 - Dicionários (Estrutura Chave-Valor)

**Arquivo:** `aula5_dicionario.py`

Trabalhe com dicionários para armazenar dados estruturados:

```python
# Criar dicionário
dic_produtos = {"ipad": 5000, "iphone": 7000, "macbook": 12000, "imac": 15000}

# Acessar valores
print(dic_produtos["iphone"])  # 7000

# Adicionar novo item
dic_produtos["airpods"] = 2000

# Editar valor
dic_produtos["iphone"] = dic_produtos["iphone"] * 0.9  # Desconto de 10%

# Remover item
item_removido = dic_produtos.pop("macbook")

# Verificar existência
print("ipad" in dic_produtos)              # True
print("iphone" in dic_produtos.keys())    # True
print(15000 in dic_produtos.values())     # True

# Converter para listas
produtos = list(dic_produtos.keys())      # ["ipad", "iphone", ...]
precos = list(dic_produtos.values())      # [5000, 7000, ...]

# Contar itens
qtde = len(dic_produtos)

# Exercício prático - busca de produtos
dic_produtos = {"ipad": 5000, "iphone": 7000, "macbook": 12000, "imac": 15000}
produto_buscado = input("Digite o nome do produto: ").lower().strip()

if produto_buscado in dic_produtos:
    preco = dic_produtos[produto_buscado]
    print(f"O preço do {produto_buscado} é R$ {preco}")
else:
    print("Produto não encontrado")
```

**Conceitos:** Criação, acesso, inserção, atualização, remoção, verificação, métodos (keys, values, items, pop, get)

---

### 🔹 Aula 6 - Loops com FOR e Iteração

**Arquivo:** `aula6_for.py`

Automatize tarefas repetitivas com loops:

```python
# FOR com range
for i in range(10):
    print("python é legal")

# FOR em lista
lista_precos = [5000, 7000, 12000, 15000]

for preco in lista_precos:
    if preco > 5000:
        taxa = 0.15
    else:
        taxa = 0.1
    imposto = preco * taxa
    print(f"Preço: R$ {preco} - Imposto: R$ {imposto}")

# FOR em dicionário
vendas_25 = {"janeiro": 15000, "fevereiro": 18000, "março": 12000, "abril": 15000}
vendas_26 = {"janeiro": 16000, "fevereiro": 29000, "março": 51100, "abril": 18000}

# Calcular crescimento de vendas
for mes in vendas_25:
    valor_25 = vendas_25[mes]
    valor_26 = vendas_26[mes]
    crescimento = (valor_26 / valor_25) - 1
    print(f"Mês: {mes} - Crescimento: {crescimento:.1%}")

# FOR com .items()
produtos = {"meia": 20, "camiseta": 35, "calça": 80, "tênis": 120}

for produto, preco in produtos.items():
    if preco > 50:
        print(f"{produto}: R$ {preco}")
    else:
        print(f"{produto}: R$ {preco} - Em promoção!")

# Calcular totais
total_estoque = 0
for preco in produtos.values():
    total_estoque += preco

preco_medio = total_estoque / len(produtos)

# Produtos acima da média
for produto, preco in produtos.items():
    if preco > preco_medio:
        print(f"{produto}: R$ {preco}")

# Calcular impostos
imposto_total = 0
for preco in produtos.values():
    imposto = preco * 0.08
    imposto_total += imposto
print(f"Total de imposto: R$ {imposto_total:.2f}")
```

**Conceitos:** range(), iteração em listas, iteração em dicionários, .items(), .keys(), .values(), accumulation

---

### 🔹 Aula 7 - Funções e Reutilização de Código

**Arquivo:** `aula7_funcoes.py`

Escreva funções para organizar e reutilizar código:

```python
# Definir função com parâmetro
def definir_taxa(preco):
    if preco > 2000:
        taxa = 0.2
    else:
        taxa = 0.1
    return taxa

# Função que chama outra função
def calcular_imposto(lista_valores):
    imposto_total = 0
    for preco in lista_valores:
        taxa = definir_taxa(preco)
        imposto = preco * taxa
        imposto_total = imposto_total + imposto
    return imposto_total

# Usando as funções
lista_precos = [1500, 1000, 800, 2000]
imposto_lista1 = calcular_imposto(lista_precos)
print(f"O imposto total da lista 1 é R$ {imposto_lista1}")

lista2_precos = [500, 4000, 3200, 2600, 1000]
imposto_lista2 = calcular_imposto(lista2_precos)
print(f"O imposto total da lista 2 é R$ {imposto_lista2}")

# Função simples
def se_escreve_no_canal():
    print("Se escreve no canal Aula de Python")
    print("de um like e se inscreve no canal")

se_escreve_no_canal()
```

**Conceitos:** Definição de funções, parâmetros, retorno de valores, reutilização de código, escopo de variáveis

---

### 🔹 Aula 8 - Tuplas e Retorno Múltiplo

**Arquivo:** `aula8_tuplas.py`

Use tuplas para estruturas imutáveis e retorno múltiplo:

```python
# Listas vs Tuplas
lista_vendas = [1000, 2000, 1500, 3000, 2500]
tupla_vendas = (1000, 2000, 1500, 3000, 2500)

# Acesso é igual
print(lista_vendas[0])   # 1000
print(tupla_vendas[0])   # 1000

# Mas tuplas são imutáveis (não podem ser alteradas depois de criadas)
# tupla_vendas[0] = 2000  # ❌ Isso daria erro!

# Retorno múltiplo de uma função
def calcular_bonus(lista_vendas):
    bonus1 = 2 * len(lista_vendas)           # R$ 2 por venda
    bonus2 = sum(lista_vendas) * 0.01        # 1% do valor das vendas
    return bonus1, bonus2                     # Retorna uma tupla

# Unpacking da tupla
vendas = [100, 250, 400, 1000]
bonus1, bonus2 = calcular_bonus(vendas)

print(f"Bonus 1: R$ {bonus1}")
print(f"Bonus 2: R$ {bonus2}")

# Iterar sobre tuplas em lista
lista_telas = [(1090, 1080), (2140, 1080)]
for altura, largura in lista_telas:
    print(altura, largura)

# Exemplo prático com múltiplos vendedores
vendas = {
    "André": [1000, 500, 300, 5000, 1500, 80, 3000],
    "Andressa": [1500, 9000, 300, 150, 1500, 120, 130, 55, 500, 8500],
    "Alan": [800, 100],
    "Ana": [800, 900, 950, 1200, 1600, 130, 50, 50, 50, 50, 65, 60, 70, 70, 70, 200, 180, 100, 120, 110, 130, 140]
}

total_bonus1 = 0
total_bonus2 = 0

for vendedor in vendas:
    bonus1, bonus2 = calcular_bonus(vendas[vendedor])
    print(f"Bonus do {vendedor}: R$ {bonus1} + R$ {bonus2}")
    total_bonus1 = total_bonus1 + bonus1
    total_bonus2 = total_bonus2 + bonus2

print(f"Total de bonus 1: R$ {total_bonus1}")
print(f"Total de bonus 2: R$ {total_bonus2}")
```

**Conceitos:** Tuplas, imutabilidade, unpacking, retorno múltiplo, tuplas vs listas

---

### 🔹 Aula 9 - Módulos e Bibliotecas (APIs e Requisições HTTP)

**Arquivo:** `aula9_modulos_bibliiioteca.py`

Trabalhe com módulos da biblioteca padrão e externas:

#### Módulo OS - Operações com Sistema de Arquivos
```python
import os

# Ver diretório atual
print(os.getcwd())

# Listar arquivos
lista_arquivos = os.listdir("arquivos")

# Mover arquivos
for nome_arquivo in lista_arquivos:
    if "txt" in nome_arquivo:
        if "22" in nome_arquivo:
            os.rename(f"arquivos/{nome_arquivo}", f"arquivos/22/{nome_arquivo}")
        elif "23" in nome_arquivo:
            os.rename(f"arquivos/{nome_arquivo}", f"arquivos/23/{nome_arquivo}")
```

#### Módulo Requests - Consumindo APIs
```python
import requests

# Fazer requisição HTTP
link = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"
resposta = requests.get(link)

# Converter resposta para JSON
dic_resposta = resposta.json()

# Iterar sobre os dados
for moeda in dic_resposta:
    dic_conversao_moeda = dic_resposta[moeda]
    valor_moeda = dic_conversao_moeda["bid"]
    print(moeda, valor_moeda)

# Exemplo de resposta:
# USDBRL: 5.1962
# EURBRL: 6.1805
# BTCBRL: 359251
```

**Conceitos:** Módulos (import), módulo os, módulo requests, APIs REST, JSON, requisições HTTP

---

## 🎯 Resumo de Conceitos Aprendidos

| Aula | Conceito | Arquivo |
|------|----------|---------|
| 1 | Strings e Formatação | `Aula1-codigo.py` |
| 2 | Input e Conversão de Tipos | `Aula2-imputs.py` |
| 3 | Listas | `Aula3-lista.py` |
| 4 | Condicionais (IF/ELSE/ELIF) | `Aula-if.py` |
| 5 | Dicionários | `aula5_dicionario.py` |
| 6 | Loops (FOR) | `aula6_for.py` |
| 7 | Funções | `aula7_funcoes.py` |
| 8 | Tuplas e Retorno Múltiplo | `aula8_tuplas.py` |
| 9 | Módulos e APIs | `aula9_modulos_bibliiioteca.py` |

---

## 💻 Como Usar

Execute os arquivos Python diretamente:

```bash
python Aula1-codigo.py
python Aula2-imputs.py
python Aula3-lista.py
python Aula-if.py
python aula5_dicionario.py
python aula6_for.py
python aula7_funcoes.py
python aula8_tuplas.py
python aula9_modulos_bibliiioteca.py
```

---

## 📝 Estrutura de Dados Comparativa

### Listas vs Tuplas vs Dicionários

```python
# LISTAS - Mutáveis, ordenadas, com índice
lista = [1, 2, 3, 4, 5]
lista[0] = 10  # ✅ Pode ser modificada

# TUPLAS - Imutáveis, ordenadas, com índice
tupla = (1, 2, 3, 4, 5)
tupla[0] = 10  # ❌ Erro! Não pode ser modificada

# DICIONÁRIOS - Mutáveis, com chaves, não ordenados (até Python 3.7)
dicionario = {"nome": "João", "idade": 30}
dicionario["idade"] = 31  # ✅ Pode ser modificado
```

---

## 🚀 Próximos Passos

Agora que você domina:
- ✅ Tipos de dados (strings, números, listas, tuplas, dicionários)
- ✅ Estruturas de controle (if/elif/else)
- ✅ Loops (for)
- ✅ Funções
- ✅ Módulos e APIs

Você está pronto para:
1. Criar aplicações mais complexas
2. Trabalhar com bancos de dados
3. Desenvolver APIs com Flask/Django
4. Automação com scripts Python
5. Data Science e Machine Learning

---

## 📌 Dicas Importantes

1. **Pratique constantemente** - A prática é a chave para aprender programação
2. **Entenda os conceitos** - Não apenas decore o código
3. **Reutilize código** - Use funções para evitar repetição
4. **Documente seu código** - Adicione comentários explicativos
5. **Teste seus programas** - Sempre teste com diferentes entradas

---

## 🏆 Conclusão

Este curso cobriu os **fundamentos essenciais do Python** necessários para começar desenvolvimentos mais avançados. Parabéns por completar todas as 9 aulas! 🎉

**Bora codar!** 💻🐍

Converter chaves e valores:

produtos = list(dic_produtos.keys())
precos = list(dic_produtos.values())

🧪 Exercício prático — Sistema de busca de produtos

Foi desenvolvido um sistema que:

Recebe o nome do produto pelo teclado

Normaliza o texto digitado

Verifica se o produto existe no dicionário

Retorna o preço ao usuário

Esse exercício simula um cenário real de consulta de dados em sistemas.

🎯 Objetivo da Aula 5

Dominar estruturas de dados em Python

Trabalhar com dados organizados

Criar lógica de consulta dinâmica

Construir base para aplicações backend e automações

📚 Aula 7 — Funções em Python

Nesta aula foram estudadas as funções em Python, um conceito fundamental da programação que permite criar blocos de código reutilizáveis.

🧠 Conteúdos aprendidos

- Definição de funções com `def`
- Parâmetros e argumentos
- Retorno de valores com `return`
- Reutilização de código através de funções
- Estruturação lógica de programas

✅ Exercício prático — Sistema de cálculo de impostos

Foi desenvolvido um sistema que:
- Define uma função para calcular a taxa de imposto baseada no preço
- Calcula o imposto total de uma lista de produtos
- Aplica lógica condicional para diferentes faixas de preço
- Demonstra como funções simplificam código complexo

📚 Aula 8 — Tuplas em Python

Nesta aula foram estudadas as tuplas, uma estrutura de dados imutável muito importante para trabalhar com dados que não devem ser alterados.

🧠 Conteúdos aprendidos

- Criação e acesso a tuplas
- Diferença entre listas (mutáveis) e tuplas (imutáveis)
- Desempacotamento de tuplas (unpacking)
- Retorno de múltiplos valores em funções
- Performance: tuplas são mais rápidas que listas
- Iteração sobre tuplas

✅ Exercício prático — Sistema de cálculo de bônus

Foi desenvolvido um sistema que:
- Define uma função que retorna múltiplos valores (tupla)
- Calcula dois tipos de bônus: R$2 por venda + 1% do faturamento
- Utiliza desempacotamento de tuplas para receber múltiplos retornos
- Itera sobre um dicionário de vendedores com seus dados
- Calcula bônus individuais e totalizações

Esse exercício combina conhecimentos de funções, tuplas, dicionários e iterações, simulando um cenário real de cálculo de folha de pagamento.

🎯 Objetivos das Aulas 7 e 8

✅ Dominar a criação e uso de funções para reutilizar código
✅ Entender a diferença entre mutabilidade e imutabilidade
✅ Trabalhar com retorno de múltiplos valores
✅ Aplicar conceitos em cenários práticos e realistas
✅ Preparar-se para programação mais avançada e orientada a objetos

## 📝 Autor

**VinihMarteleto** - Estudante de Python

---

Último atualizado: Fevereiro de 2026
