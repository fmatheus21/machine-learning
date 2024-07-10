import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.preprocessing import StandardScaler


def standardisation():
	id_cliente = 'Id_Cliente'
	renda = 'income'
	idade = 'age'
	emprestimo = 'loan'
	pagamento = 'default'
	separador = '-------------------------------'

	base_credit = pd.read_csv('data/credit_data.csv')
	# base_credit = data.rename(columns=novos_cabecalhos, inplace=True)
	# base_credit = data.loc[data[idade] < 0]  # Verificando informacoes inconsistentes
	# base_credit = data.drop(data[data[idade] < 0].index)  # Removendo dados inconsistentes
	media_idade = base_credit[idade].mean()
	print(f'Media de Idade: {media_idade}')

	base_credit.loc[base_credit[idade] < 0, idade] = 40.80
	print(base_credit.loc[base_credit[idade] < 0])

	base_credit[idade] = base_credit[idade].fillna(base_credit[idade].mean())  # Preenche os valors nulos do campo

	'''filters = base_credit[base_credit[renda] >= 5000.0]  # Filtrando pela renda
	unique = np.unique(base_credit[pagamento], return_counts=True)  # Retorna os valores unicos
	graphic = sns.countplot(x=base_credit[pagamento])  # Gera um grafico
	histogram_chart = plt.hist(x=base_credit[idade])  # Grafico de histograma
	histogram_chart_loan = plt.hist(base_credit[emprestimo])  # Grafico de histograma
	graphic_scatter_age = px.scatter_matrix(base_credit, dimensions=[idade, renda, emprestimo])
	is_null = base_credit.isnull().sum()
	is_null_age = base_credit.loc[pd.isnull(base_credit[idade])]

	print(base_credit)
	print(filters)
	print(unique)
	print(graphic)
	print(histogram_chart)
	print(histogram_chart_loan)
	print(graphic_scatter_age)
	print(is_null)
	print(is_null_age)
	'''

	print(base_credit)

	print(separador)

	# Saber se o cliente vai pagar o emprestimo
	# x = Classes previsoras
	# y = Variavel de classe
	x_credit = base_credit.iloc[:, 1:4].values
	y_credit = base_credit.iloc[:, 4].values

	'''	
	Normalizacao (Normalization)
	x = (x - minimo(x)) / (maximo(x) - minimo(x))
	'''

	'''
	Padronizacao (Standardisation)
	x = (x - media(x))/desvio padrao(x)
	'''
	scaler_credit = StandardScaler()
	x_credit = scaler_credit.fit_transform(x_credit)

	menor_renda = x_credit[:, 0].min()
	maior_renda = x_credit[:, 0].max()

	menor_idade = x_credit[:, 1].min()
	maior_idade = x_credit[:, 1].max()

	menor_emprestimo = x_credit[:, 2].min()
	maior_emprestimo = x_credit[:, 2].max()

	print(x_credit)
	print(y_credit)
	print(f'Menor Renda: {menor_renda} | Menor Idade: {menor_idade} | Menor Emprestimo: {menor_emprestimo}')
	print(f'Maior Renda: {maior_renda} | Maior Idade: {maior_idade} | Maior Emprestimo: {maior_emprestimo}')


def test():
	base_census = pd.read_csv('data/census.csv')

	print(base_census)
	print(base_census.describe())
	print(base_census.isnull().sum())


def init():
	# standardisation()
	test()


if __name__ == '__main__':
	init()
