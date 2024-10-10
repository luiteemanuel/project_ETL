from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select 
import time
import pandas as pd  

browser = webdriver.Firefox()
browser.get('https://qedu.org.br/municipio/3550308-sao-paulo/censo-escolar')
time.sleep(2)

# Função para extrair os dados de matrículas
def extract_data():
    main_divs = browser.find_elements(By.CSS_SELECTOR, '.flex.flex-row.justify-between.w-full.border-b.border-gray-200.pb-4')

    names = []
    matriculas = []

    # Iterar por cada uma das divs encontradas
    for div in main_divs:
        # Encontrar a div que contém o nome
        name_div = div.find_element(By.CLASS_NAME, 'font-bold')
        name = name_div.text if name_div else 'N/A'

        # Encontrar a div que contém o número de matrículas
        matriculas_div = div.find_element(By.CSS_SELECTOR, '.flex.flex-col.justify-center.items-end.w-1\\/3.font-bold.text-xl')
        
        # Extrair o número de matrículas
        matriculas_span = matriculas_div.find_elements(By.TAG_NAME, 'span')
        matricula_count = matriculas_span[0].text if matriculas_span else 'N/A'

        names.append(name)
        matriculas.append(matricula_count)

    return names, matriculas

dropdown = Select(browser.find_element(By.CSS_SELECTOR, 'select.text-xs:nth-child(2)'))
dropdown.select_by_value('5')  
time.sleep(2)  

publica_names, publica_matriculas = extract_data()
tipo_escola_publica = ['Pública'] * len(publica_names)  

dropdown.select_by_value('4')  # Seleciona a opção "Privada"
time.sleep(2)  

privada_names, privada_matriculas = extract_data()
tipo_escola_privada = ['Privada'] * len(privada_names)  

df = pd.DataFrame({
    'Nome': publica_names + privada_names,
    'Matrículas': publica_matriculas + privada_matriculas,
    'Tipo de Escola': tipo_escola_publica + tipo_escola_privada
})

# Salvar em CSV
df.to_csv('/home/luite/Documentos/data_engineer_test/data/bronze/matriculas_sp_escolas.csv', index=False)

# Fecha o navegador
browser.quit()
