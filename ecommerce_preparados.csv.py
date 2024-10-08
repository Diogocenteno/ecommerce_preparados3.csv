import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from math import sqrt

# Carrega os dados
df = pd.read_csv('/data/ecommerce_preparados.csv')
df = df.dropna()

# Define as variáveis preditoras e a variável alvo
X = df[['N_Avaliações_MinMax', 'Nota_MinMax', 'Preco_MinMax', 'Desconto_MinMax', 'Temporada_Cod', 'Marca_Freq', 'Material_Freq']]  # Preditor
Y = df['Qtd_Vendidos_Cod']

# Divide os dados em conjuntos de treino e teste
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Cria e treina o modelo de Regressão Linear
modelo_lr = LinearRegression()
modelo_lr.fit(x_train, y_train)

# Faz previsões com o conjunto de teste
y_prev = modelo_lr.predict(x_test)

# Avalia o modelo
r2 = r2_score(y_test, y_prev)
rmse = sqrt(mean_squared_error(y_test, y_prev))
desvio_padrao = Y.std()

# Exibe os resultados
print(f'Coeficiente de Determinação - R²: {r2:.2f}')
print(f"Raiz do Erro Quadrático Médio - RMSE: {rmse:.2f}")
print(f"Desvio Padrão do campo Qtd_Vendidos_Cod: {desvio_padrao:.2f}")
