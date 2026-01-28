import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("zomato.csv", encoding='latin-1')

# Preview
print(df.head())
print(df.shape)

# Clean Data
df.drop_duplicates(inplace=True)
df = df.dropna(subset=["Restaurant Name", "Aggregate rating"])

# Display missing values
print(df.isnull().sum())

# Top Cities with Most Restaurants
plt.figure(figsize=(10,5))
df["City"].value_counts().head(10).plot(kind="bar")
plt.title("Top Cities with Most Restaurants")
plt.xlabel("City")
plt.ylabel("Count")
plt.show()

# Rating Distribution
plt.figure(figsize=(8,5))
sns.histplot(df["Aggregate rating"], bins=20)
plt.title("Ratings Distribution")
plt.show()

# Popular Cuisines
plt.figure(figsize=(10,5))
df["Cuisines"].value_counts().head(10).plot(kind='barh')
plt.title("Most Popular Cuisines")
plt.show()