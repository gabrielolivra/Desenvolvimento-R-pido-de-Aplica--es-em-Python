from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import pandas as pd

def enviar_dados(url, codigo, nome, quantidade, valor_unitario):
    driver = webdriver.Chrome()
    driver.get(url)
    
    
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, 'codigo')))
    except TimeoutException:
        print("Timed out waiting for page to load")
        return
    
    
    campo_codigo = driver.find_element(By.NAME, 'codigo')
    campo_codigo.send_keys(codigo)
    
    campo_nome = driver.find_element(By.NAME, 'nome')
    campo_nome.send_keys(nome)
    
    campo_quantidade = driver.find_element(By.NAME, 'quantidade')
    campo_quantidade.send_keys(quantidade)
    
    campo_valor = driver.find_element(By.NAME, 'valor_unitario')
    campo_valor.send_keys(valor_unitario)
    
   
    campo_valor.submit()
    
    
    driver.implicitly_wait(2) 
   

url_formulario = 'http://127.0.0.1:5500/index.html'  


planilha_csv = 'produtos.csv'  
dados = pd.read_csv(planilha_csv)

for index, item in dados.iterrows():
    codigo_item = item['codigo_item']
    nome = item['nome']
    quantidade = str(item['quantidade'])  
    valor_unitario = str(item['valor_unitario'])  
    
    enviar_dados(url_formulario, codigo_item, nome, quantidade, valor_unitario)
    
    print(f'Dados para o item {codigo_item} enviados com sucesso!')

print('Envio de todos os itens concluído!')
