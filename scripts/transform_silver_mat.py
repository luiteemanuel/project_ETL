import pandas as pd 
import numpy as np


df = pd.read_csv('data/bronze/matriculas_sp_escolas.csv')
#removendo total escolas
df = df.drop(index=0)
df = df.drop(index=11)

#cria dataframe somente com os dados de professores
idex_prof = [1, 2, 3]
df_prof = df.loc[idex_prof]
df_prof = df_prof.replace({
    "Anos iniciais": "total_professores_inicial", 
    "Anos finais": "total_professores_finais", 
    "Ensino Médio": "total_professores_medio"
})

#cria dataframe somente com os dados de alunos
idex_alunos = [4, 5, 6, 7, 8, 9, 10]
df_alunos = df.loc[idex_alunos]
df_alunos = df_alunos.replace({
    "Creche": "total_alunos_creche", 
    "Pré-escola": "total_alunos_pre-escola", 
    "Anos iniciais": "total_alunos_inicial", 
    "Anos finais": "total_alunos_fundamental", 
    "Ensino Médio": "total_alunos_medio",
    "EJA": "total_alunos_EJA",
    "Educação Especial ": "total_alunos_especial"
})

#cria dataframe professores escolas privadas
idex_prof = [12, 13, 14]
df_prof_pri = df.loc[idex_prof]
df_prof_pri = df_prof_pri.replace({
    "Anos iniciais": "total_professores_inicial", 
    "Anos finais": "total_professores_finais", 
    "Ensino Médio": "total_professores_medio"
})



#criar dataframe com dados alunos escolas privadas
idex_alunos = [15, 16, 17, 18, 19, 20, 21]
df_aluno_pri = df.loc[idex_alunos]
df_aluno_pri = df_aluno_pri.replace({
    "Creche": "total_alunos_creche", 
    "Pré-escola": "total_alunos_pre-escola", 
    "Anos iniciais": "total_alunos_inicial", 
    "Anos finais": "total_alunos_fundamental", 
    "Ensino Médio": "total_alunos_medio",
    "EJA": "total_alunos_EJA",
    "Educação Especial ": "total_alunos_especial"
})

df_all = pd.concat([df_prof, df_alunos, df_prof_pri, df_aluno_pri], axis=0)
df_all = df_all.rename(columns={"Nome": "Categoria", "Matrículas": "Total_Matriculas"})
df_all.to_csv('data/silver/matriculas_sp_escolas.csv', index=False)
print(df_all)