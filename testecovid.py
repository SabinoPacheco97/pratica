import pandas as pd

# Carregando o arquivo CSV
df = pd.read_csv('owid-covid-data.csv')

# Visualizando as primeiras linhas
print(df.head())

# Verificando as colunas disponíveis
print(df.columns)

# Verificando valores ausentes
print(df.isnull().sum())

# Convertendo a coluna de data
df['date'] = pd.to_datetime(df['date'])

# Filtrando países de interesse
paises = ['Brazil', 'United States', 'India', 'Kenya']
df_paises = df[df['location'].isin(paises)]

# Removendo linhas com dados críticos ausentes
df_paises = df_paises.dropna(subset=['total_cases', 'total_deaths'])

# Preenchendo valores ausentes com interpolação
df_paises = df_paises.fillna(method='ffill')

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(12,6))
for pais in paises:
    dados = df_paises[df_paises['location'] == pais]
    plt.plot(dados['date'], dados['total_cases'], label=pais)

plt.title('Total de Casos Confirmados de COVID-19')
plt.xlabel('Data')
plt.ylabel('Total de Casos')
plt.legend()
plt.grid(True)
plt.show()



df_paises['taxa_mortalidade'] = df_paises['total_deaths'] / df_paises['total_cases']

# Exemplo para um país
kenya = df_paises[df_paises['location'] == 'Kenya']

plt.figure(figsize=(10,5))
plt.plot(kenya['date'], kenya['taxa_mortalidade'])
plt.title('Taxa de Mortalidade - Quênia')
plt.xlabel('Data')
plt.ylabel('Taxa de Mortalidade')
plt.grid(True)
plt.show()




plt.figure(figsize=(12,6))
for pais in paises:
    dados = df_paises[df_paises['location'] == pais]
    plt.plot(dados['date'], dados['total_vaccinations'], label=pais)

plt.title('Total de Vacinas Administradas')
plt.xlabel('Data')
plt.ylabel('Vacinas')
plt.legend()
plt.grid(True)
plt.show()




import plotly.express as px

# Dados mais recentes
df_latest = df[df['date'] == df['date'].max()]
fig = px.choropleth(df_latest, 
                    locations="iso_code",
                    color="total_cases",
                    hover_name="location",
                    color_continuous_scale="Reds",
                    title="Casos Totais de COVID-19 por País (Data mais recente)")

fig.show()
