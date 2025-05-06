<<<<<<< HEAD
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("owid-covid-data.csv")  


print("Dataset preview:")
print(df.head())


df['date'] = pd.to_datetime(df['date'])
latest_data = df.sort_values('date').groupby('location').tail(1)

latest_data = latest_data[['location', 'total_cases', 'total_deaths']].dropna()

top_countries = latest_data.sort_values(by='total_cases', ascending=False).head(10)

plt.figure(figsize=(12, 6))
sns.barplot(x='total_cases', y='location', data=top_countries, palette='Blues_d')
plt.title("Top 10 Countries by Total COVID-19 Cases")
plt.xlabel("Total Cases")
plt.ylabel("Country")
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
sns.barplot(x='total_deaths', y='location', data=top_countries, palette='Reds_d')
plt.title("Top 10 Countries by Total COVID-19 Deaths")
plt.xlabel("Total Deaths")
plt.ylabel("Country")
plt.tight_layout()
plt.show()
=======
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("owid-covid-data.csv")  


print("Dataset preview:")
print(df.head())


df['date'] = pd.to_datetime(df['date'])
latest_data = df.sort_values('date').groupby('location').tail(1)

latest_data = latest_data[['location', 'total_cases', 'total_deaths']].dropna()

top_countries = latest_data.sort_values(by='total_cases', ascending=False).head(10)

plt.figure(figsize=(12, 6))
sns.barplot(x='total_cases', y='location', data=top_countries, palette='Blues_d')
plt.title("Top 10 Countries by Total COVID-19 Cases")
plt.xlabel("Total Cases")
plt.ylabel("Country")
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
sns.barplot(x='total_deaths', y='location', data=top_countries, palette='Reds_d')
plt.title("Top 10 Countries by Total COVID-19 Deaths")
plt.xlabel("Total Deaths")
plt.ylabel("Country")
plt.tight_layout()
plt.show()
>>>>>>> 1d891c31b2fa8f651180ea07c94bee6b144a5e09
