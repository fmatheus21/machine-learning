import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


def init():
	data = pd.read_csv('data/credit_data.csv')
	base_credit = data.loc[data['age'] < 0]
	filters = base_credit[base_credit['income'] >= 5000.0]  # Filtrando pela renda
	unique = np.unique(base_credit['default'], return_counts=True)  # Retorna os valores unicos
	graphic = sns.countplot(x=base_credit['default'])  # Gera um grafico
	histogram_chart = plt.hist(x=base_credit['age'])  # Grafico de histograma
	histogram_chart_loan = plt.hist(base_credit['loan'])  # Grafico de histograma
	graphic_scatter_age = px.scatter_matrix(base_credit, dimensions=['age', 'income', 'loan'])

	print(base_credit)
	print(filters)
	print(unique)
	print(graphic)
	print(histogram_chart)
	print(histogram_chart_loan)
	print(graphic_scatter_age)


if __name__ == '__main__':
	init()
