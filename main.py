import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


def init():
	base_credit = pd.read_csv('data/credit_data.csv')
	filters = base_credit[base_credit['income'] >= 5000.0]  # Filtrando pela renda
	print(filters)


if __name__ == '__main__':
	init()
