import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('ecommerce_estatistica.csv')
print(df.head().to_string())

#Gráfico de Histograma
plt.figure(figsize=(10, 6))
plt.hist(df['Preço'], bins=5, color='blue', alpha=0.8)
plt.xticks(ticks=range(0, int(df['Preço'].max())+50, 50))
plt.title('Histograma - Distribuição dos Preços')
plt.xlabel('Preço')
plt.ylabel('Quantidades')
plt.show()

#Gráfico de dispersão
plt.figure(figsize=(10, 6))
plt.scatter(df['Preço'], df['Desconto'])
plt.title('Dispersão - Preço e Desconto')
plt.xlabel('Preço')
plt.ylabel('Desconto')
plt.show()

#Mapa de calor
htmap = df[['Preço', 'Nota', 'Marca_Cod', 'Qtd_Vendidos_Cod']].corr()
plt.figure(figsize=(10, 8))
sns.heatmap(htmap, annot=True, fmt='.2f')
plt.title('Mapa de calor da correlação entre variáveis')
plt.show()

# Gráfico de barra
sns.countplot(x='Qtd_Vendidos', hue='Gênero', data=df, palette='pastel')
plt.title('Vendas por Gênero')
plt.xlabel('Quantidade de Vendas')
plt.ylabel('Quantidade de Clientes')
plt.legend(title='Gêneros')
plt.show()

#Gráfico de pizza
x = df['Gênero'].value_counts().index
y = df['Gênero'].value_counts().values

plt.pie(y, labels=x, autopct='%.1f%%', startangle=90)
plt.title('Porcentagem das Vendas por Gênero')
plt.show()

#Gráfico de densidade
plt.figure(figsize=(10, 6))
sns.kdeplot(df['Nota'], fill=True, color='#36ba90')
plt.title('Densidade das Notas')
plt.xlabel('Notas')
plt.ylabel('Quantidade')
plt.show()

#Gráfico de regressão
sns.regplot(x='Temporada_Cod', y='Qtd_Vendidos_Cod', data=df, color='#278f65', scatter_kws={'alpha': 0.5, 'color': '#34c289'})
plt.title('Regressão de Quantidade de Vendas por Temporada')
plt.xlabel('Temporada')
plt.ylabel('Quantidade de Vendas')
plt.show()

