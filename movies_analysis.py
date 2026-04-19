import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv(r"C:\Users\spenc\OneDrive\Desktop\Python\tmdb_5000_movies.csv")

# Basic info
print("Dataset Shape:", df.shape)
print("\nFirst 5 rows:")
print(df.head())
print("\nBasic Statistics:")
print(df[['budget', 'revenue', 'vote_average', 'popularity']].describe())

# Plot 1 - Top 10 highest rated movies
top_rated = df[df['vote_count'] > 100].nlargest(10, 'vote_average')
plt.figure(figsize=(12, 6))
sns.barplot(x='vote_average', y='title', data=top_rated)
plt.title('Top 10 Highest Rated Movies')
plt.xlabel('Average Rating')
plt.ylabel('Movie Title')
plt.tight_layout()
plt.savefig(r"C:\Users\spenc\OneDrive\Desktop\Python\chart1_top_rated.png")
print("\nChart 1 saved!")

# Plot 2 - Budget vs Revenue
plt.figure(figsize=(10, 6))
sns.scatterplot(x='budget', y='revenue', data=df[df['budget'] > 0])
plt.title('Movie Budget vs Revenue')
plt.xlabel('Budget')
plt.ylabel('Revenue')
plt.tight_layout()
plt.savefig(r"C:\Users\spenc\OneDrive\Desktop\Python\chart2_budget_revenue.png")
print("Chart 2 saved!")

print("\nAnalysis complete! Check your Python folder for the chart images.")