from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json 

browser = webdriver.Firefox()

url = 'https://capital.sp.gov.br/w/noticia/prefeitura-libera-creditos-para-compra-de-material-e-uniforme-escolar-para-mais-de-28-6-mil-novos-estudantes-matriculados-na-rede-municipal' 
browser.get(url)

time.sleep(2)

# Encontrar a div com a classe "psp-news-text"
news_div = browser.find_element(By.CLASS_NAME, 'psp-news-text')

# Extrair o texto dos parágrafos dentro dessa div
paragraphs = news_div.find_elements(By.TAG_NAME, 'p')
text_content = [p.text for p in paragraphs]

# Salvar o conteúdo em um arquivo
with open('/home/luite/Documentos/data_engineer_test/data/bronze/auxilio_materiais.json', 'w', encoding='utf-8') as json_file:
    json.dump({"content": text_content}, json_file, ensure_ascii=False, indent=4)

# Fechar o navegador
browser.quit()