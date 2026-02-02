# Exercícios Python - Strings e Textos

Repositório com exercícios práticos de Python focando em **strings, textos e estruturas de controle**.

## 📚 Conteúdo

### Aula 1 - Introdução a Strings
- Conceitos básicos de strings em Python
- Manipulação e formatação de texto
- Métodos de string

### Aula 2 - Operações com Strings
- Concatenação de strings
- Slicing e indexação
- Transformação de texto (upper, lower, etc)

### Aula 3 - Textos Avançado
- Formatação de strings
- F-strings
- Métodos avançados de manipulação

### Aula 4 - Estruturas de Controle IF
- Condicionais simples (if/else)
- Condicionais aninhadas (elif)
- Operadores lógicos (and, or, not)
- Exemplos práticos com validação de dados

## 🎯 Objetivos

✅ Aprender a manipular strings e textos em Python  
✅ Dominar estruturas de controle de fluxo  
✅ Resolver problemas práticos com condicionais  
✅ Validar e processar dados de entrada do usuário  

## 💻 Como usar

Abra cada arquivo de aula no seu editor Python e execute:

```bash
python Aula1.py
python Aula2.py
python Aula3.py
python Aula4-IF.py
python aula5_dicionario.py

```

📚 Aula 5 — Dicionários em Python

Nesta aula foram estudados os dicionários em Python (dict), uma estrutura de dados fundamental para armazenar informações no formato chave : valor, muito utilizada em sistemas reais, APIs e aplicações backend.

🧠 Conteúdos aprendidos

Criação de dicionários

Diferença entre listas e dicionários

Acesso a valores usando chaves

Inserção de novos dados

Atualização de valores existentes

Remoção de itens

Verificação de existência de chaves

Conversão de chaves e valores em listas

Contagem de elementos com len()

Tratamento de entrada do usuário (lower() e strip())

✅ Buscar valor no dicionário

Acesso direto ao preço do produto usando a chave:

print(dic_produtos["iphone"])

✅ Adicionar e editar produtos

Adicionar novo item:

dic_produtos["airpods"] = 2000


Aplicar desconto em um produto:

dic_produtos["iphone"] = dic_produtos["iphone"] * 0.9

✅ Remover item do dicionário
item_removido = dic_produtos.pop("macbook")

✅ Verificar se um produto existe
print("ipad" in dic_produtos)

✅ Converter dados para listas

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

## 📝 Autor

**VinihMarteleto** - Estudante de Python

---

Último atualizado: Janeiro de 2026
