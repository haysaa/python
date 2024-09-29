import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
pd.set_option('display.max_columns', None)
df=pd.read_csv("Housing.csv")

plt.subplot(1,3,1)
plt.hist(df['area'],bins=20,weights=df['price'],alpha=0.9,color='red')
plt.xlabel('area')
plt.ylabel('price')
plt.title('relation between area and price')

plt.subplot(1,3,2)
plt.hist(df['bedrooms'],bins=20,weights=df['price'],alpha=0.9,color='blue')
plt.xlabel('bedrooms')
plt.ylabel('price')
plt.title('relation between bedrooms and price')

plt.subplot(1,3,3)
plt.hist(df['stories'],bins=15,weights=df['price'],color='green',alpha=0.9)
plt.xlabel('stories')
plt.ylabel('price')
plt.title('relation between stories and price')
plt.show()
plt.tight_layout()

avg_price_bathroom=df.groupby('bathrooms').agg({"price" : ["mean"]})
avg_price_bathroom=avg_price_bathroom.round(2)
avg_price_furnishing = df.groupby("furnishingstatus").agg({"price" : ["mean"]})
avg_price_furnishing = avg_price_furnishing.round(2)

plt.subplot(1,2,1)
plt.bar(avg_price_bathroom.index,avg_price_bathroom['price']['mean'],color='skyblue')
plt.title('average price according to bathroom count')
plt.xlabel('bathroom count')
plt.ylabel('price')

plt.subplot(1,2,2)
plt.bar(avg_price_furnishing.index.astype(str),avg_price_furnishing['price']['mean'],color='purple')
plt.title('average price according to furnishing')
plt.xlabel('furnishing')
plt.ylabel('price')

plt.show()
plt.tight_layout()

data = pd.read_csv('Housing.csv')

numerical_columns = ['price', 'area', 'bedrooms', 'bathrooms', 'stories', 'parking']

correlation_matrix = data[numerical_columns].corr()
print(correlation_matrix)

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix')
plt.show()
