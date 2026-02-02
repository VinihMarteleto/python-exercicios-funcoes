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
```
📚 Aula 5 — Dicionários em Python

Nesta aula foram estudados os dicionários em Python (dict), uma das estruturas de dados mais importantes da linguagem, utilizadas para armazenar informações no formato chave : valor.

🧠 Conceitos aprendidos

Criação de dicionários

Acesso a valores por chave

Diferença entre listas e dicionários

Inserção de novos dados

Atualização de valores

Remoção de itens

Verificação de existência de chaves

Conversão para listas (keys() e values())

Contagem de elementos com len()

Tratamento de entrada do usuário (lower() e strip())

✅ Exemplo — Buscar preço de produto

Acesso direto usando a chave do dicionário:

print(dic_produtos["iphone"])

✅ Adicionar e atualizar dados

Adicionar novo produto:

dic_produtos["airpods"] = 2000


Aplicar desconto:

dic_produtos["iphone"] = dic_produtos["iphone"] * 0.9

✅ Remover item do dicionário
item_removido = dic_produtos.pop("macbook")

✅ Verificar existência de produto
print("ipad" in dic_produtos)

✅ Converter chaves e valores em listas
produtos = list(dic_produtos.keys())
precos = list(dic_produtos.values())

🧪 Exercício prático — Sistema de busca de produto

Foi implementado um sistema que:

Recebe o nome do produto via input()

Normaliza o texto (lower() e strip())

Verifica se o produto existe

Retorna o preço ao usuário

Isso simula um cenário real de consulta de dados em sistemas.

🎯 Objetivo da aula

Aprender a trabalhar com estruturas chave-valor

Melhorar organização dos dados

Criar lógica de consulta dinâmica

Desenvolver base para sistemas maiores (APIs, banco de dados, backend)


## 📝 Autor

**VinihMarteleto** - Estudante de Python

---

Último atualizado: Janeiro de 2026
