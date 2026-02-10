import os 

print(os.getcwd()) # mostra o caminho do diretório atual  

lista_arquivos = os.listdir("arquivos") # lista os arquivos do diretório especificado
print(lista_arquivos)

for nome_arquivo in lista_arquivos: # percorre a lista de arquivos
    if "txt" in nome_arquivo: # verifica se o arquivo é um arquivo de texto
        if "22" in nome_arquivo: # verifica se o nome do arquivo contém "22"
            os.rename(f"arquivos/{nome_arquivo}", f"arquivos/22/{nome_arquivo}") # move o arquivo para a pasta "22"
        elif "23" in nome_arquivo: # verifica se o nome do arquivo contém "23"
            os.rename(f"arquivos/{nome_arquivo}", f"arquivos/23/{nome_arquivo}") # move o arquivo para a pasta "23"
        else:
            os.rename(f"arquivos/{nome_arquivo}", f"arquivos/outros/{nome_arquivo}") # move o arquivo para a pasta "outros" 
            
           
import requests

link = " https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"

resposta = requests.get(link)
print(resposta)
dic_resposta = resposta.json()

for moeda in dic_resposta:
    dic_conversao_moeda = dic_resposta[moeda]
    valor_moeda = dic_conversao_moeda["bid"]    
    print(moeda, valor_moeda)
# {'USDBRL': {'code': 'USD', 'codein': 'BRL', 'name': 'Dólar Americano/Real Brasileiro', 'high': '5.2378', 'low': '5.17864', 'varBid': '0.0042', 'pctChange': '0.080895', 'bid': '5.1962', 'ask': '5.1992', 'timestamp': '1770753264', 'create_date': '2026-02-10 16:54:24'},
# 'EURBRL': {'code': 'EUR', 'codein': 'BRL', 'name': 'Euro/Real Brasileiro', 'high': '6.23053', 'low': '6.1597', 'varBid': '0.00766', 'pctChange': '0.12409', 'bid': '6.1805', 'ask': '6.1885', 'timestamp': '1770753088', 'create_date': '2026-02-10 16:51:28'},
# 'BTCBRL': {'code': 'BTC', 'codein': 'BRL', 'name': 'Bitcoin/Real Brasileiro', 'high': '369225', 'low': '352658', 'varBid': '-8929', 'pctChange': '-2.425', 'bid': '359251', 'ask': '359299', 'timestamp': '1770753265', 'create_date': '2026-02-10 16:54:25'}}