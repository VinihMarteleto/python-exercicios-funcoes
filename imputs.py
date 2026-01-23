# exemplo de input e conversão de tipos
faturamento = input("preencha o faturamento (apenas numeros) : ")
faturamento = faturamento.replace("R$", "").replace(",", ".")
faturamento = float(faturamento)
custo = 600

lucro = faturamento - custo
print(lucro)

vendas_dia1 = float(input("Vendas Dia 1: "))
vendas_dia2 = float(input("Vendas Dia 2: "))

print(vendas_dia1 + vendas_dia2)
# exemplo de input e conversão de tipos

