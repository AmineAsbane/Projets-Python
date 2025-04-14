import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter

plt.style.use('seaborn-vibrant')

df = pd.read_csv('netflix_titles.csv')
df.head()

# Nettoyage des données
df.dropna(subset=['country', 'release_year', 'type'], inplace=True)
df['date_added'] = pd.to_datetime(df['date_added'])
df['year_added'] = df['date_added'].dt.year

# Nombre de contenus ajoutés par an
plt.figure(figsize=(10,6))
sns.countplot(data=df, x='year_added', hue='type', palette='Set2')
plt.xticks(rotation=45)
plt.title("Nombre de contenus ajoutés par année")
plt.xlabel("Année")
plt.ylabel("Nombre de titres")
plt.legend(title='Type')
plt.tight_layout()
plt.show()

# Top 10 des pays les plus représentés
top_countries = df['country'].value_counts().head(10)
plt.figure(figsize=(8,5))
sns.barplot(x=top_countries.values, y=top_countries.index, palette='coolwarm')
plt.title("Top 10 des pays les plus présents sur Netflix")
plt.xlabel("Nombre de titres")
plt.ylabel("Pays")
plt.tight_layout()
plt.show()

# Répartition films vs séries
plt.figure(figsize=(6,6))
df['type'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90, colors=['skyblue', 'salmon'])
plt.title("Répartition Films vs Séries")
plt.ylabel("")
plt.show()

# Top 10 genres (extrait de 'listed_in')
all_genres = df['listed_in'].dropna().str.split(', ')
flat_genres = [genre for sublist in all_genres for genre in sublist]
genre_counts = Counter(flat_genres).most_common(10)

genres, counts = zip(*genre_counts)
plt.figure(figsize=(10,5))
sns.barplot(x=list(counts), y=list(genres), palette='magma')
plt.title("Top 10 des genres les plus courants")
plt.xlabel("Nombre de titres")
plt.ylabel("Genres")
plt.show()

# Durée des films
df_movies = df[df['type'] == 'Movie'].copy()
df_movies['duration_int'] = df_movies['duration'].str.extract('(\d+)').astype(float)

plt.figure(figsize=(10,5))
sns.histplot(df_movies['duration_int'], bins=30, color='purple')
plt.title("Durée des films (en minutes)")
plt.xlabel("Durée")
plt.ylabel("Nombre de films")
plt.show()
