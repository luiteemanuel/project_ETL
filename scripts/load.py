import pandas as pd 
import sqlite3


# Conectar ao banco de dados (ou criar se não existir)
conn = sqlite3.connect('test_engineer.db')
cursor = conn.cursor()

#load dados escolas 

df_escolas_publicas = pd.read_csv('data/silver/matriculas_sp_escolas.csv')
df_escolas_publicas.rename(columns={'Tipo de Escola':'tipo_escola'}, inplace=True)

df_escolas_publicas.to_sql('matriculas', conn, if_exists='replace', index=False)


#load dados beneficios
df_beneficios = pd.read_csv('data/silver/auxilio_materiais.csv')
df_beneficios.to_sql('beneficio', conn, if_exists='replace', index=False)




cursor.close()
conn.commit()