import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Charger le dataset (Boston Housing Dataset)
url = "https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv"
df = pd.read_csv(url)
print(df.head())

print(df.info())

# Sélectionner les variables indépendantes (caractéristiques des maisons) et la variable dépendante (prix)
X = df.drop('medv', axis=1)  # 'medv' est la variable cible, le prix des maisons
y = df['medv']

# Séparer les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Créer et entraîner le modèle de régression linéaire
model = LinearRegression()
model.fit(X_train, y_train)

# Faire des prédictions avec l'ensemble de test
y_pred = model.predict(X_test)

# Évaluation du modèle
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

# Affichage des métriques de performance
print(f"RMSE: {rmse}")
print(f"R²: {r2}")

# Visualisation des résultats avec un nuage de points
plt.figure(figsize=(10, 6))
sns.regplot(x=y_test, y=y_pred, scatter_kws={"color": "blue"}, line_kws={"color": "red"})
plt.xlabel("Valeurs réelles")
plt.ylabel("Valeurs prédites")
plt.title("Régression Linéaire - Prédiction du Prix des Maisons")
plt.show()
