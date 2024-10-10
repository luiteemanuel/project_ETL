import json
import re
import pandas as pd

# Lendo o arquivo JSON
with open('data/bronze/auxilio_materiais copy.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Convertendo o conteúdo para uma string única
text = " ".join(data["content"])

# pega os valores de material escolar
material_values = re.findall(r'(Berçário I e II: R\$ [\d,.]+|Mini-Grupo I e II: R\$ [\d,.]+|Infantil I e II: R\$ [\d,.]+|Ciclo de Alfabetização: R\$ [\d,.]+|Ciclo Interdisciplinar: R\$ [\d,.]+|Ciclo Autoral: R\$ [\d,.]+|Ensino Médio e Educação de Jovens e Adultos: R\$ [\d,.]+|CELPs: R\$ [\d,.]+)', text)
# pegar os valores de uniforme
uniforme_values = re.findall(r'R\$\s*[\d,.]+', text)


# Criando DataFrames material escolar
df_material = pd.DataFrame({'Material Escolar': material_values})
df_material[['categoria', 'valor']] = df_material['Material Escolar'].str.split(': R\$ ', expand=True)
df_material['valor'] = df_material['valor'].str.replace(',', '.').astype(float)
df_material = df_material.drop(columns=['Material Escolar'])

df_material = df_material.replace({"Ensino Médio e Educação de Jovens e Adultos":"Ensino Media e EJA"})
#print(df_material)


# Criando DataFrame para uniforme
df_uniforme = pd.DataFrame({'categoria': uniforme_values})
uni_index=[8] 
df_uniforme = df_uniforme.loc[uni_index]
df_uniforme['valor'] = df_uniforme['categoria']
df_uniforme['categoria'] = 'Uniforme'


# Concatenando os dois DataFrames
df = pd.concat([df_material, df_uniforme], ignore_index=True)
last_index = df.index[-1]

# Remover o símbolo 'R$', substituir a vírgula por ponto e converter para float apenas na última linha
df.loc[last_index, 'valor'] = df.loc[last_index, 'valor'].replace('R$', '').replace(',', '.').strip()
df.loc[last_index, 'valor'] = float(df.loc[last_index, 'valor'])

df.to_csv('data/silver/auxilio_materiais.csv', index=False)
print(df)