import pandas as pd


data = {
    "name": [
        "iPhone 14", "Samsung TV", "Bluetooth Speaker", "Laptop", "Wireless Mouse",
        "Jeans", "T-Shirt", "Jacket", "Sneakers", "Watch",
        "Python Book", "Data Science Book", "Cookbook", "Novel", "Notebook",
        "Sofa", "Dining Table", "Lamp", "Mixer Grinder", "Water Bottle",
        "Headphones", "Smartwatch"
    ],

    "category": [
        "Electronics", "Electronics", "Electronics", "Electronics", "Electronics",
        "Clothing", "Clothing", "Clothing", "Clothing", "Clothing",
        "Books", "Books", "Books", "Books", "Books",
        "Home", "Home", "Home", "Home", "Home",
        "Electronics", "Electronics"
    ],

    "price": [
        80000, 45000, 1500, 70000, 800,
        2000, 500, 3500, 4000, 2500,
        600, 1200, 900, 700, 200,
        25000, 15000, 1200, 3000, 400,
        2500, 10000
    ],

    "stock": [
        50, 30, 100, 20, 150,
        200, 300, 120, 80, 90,
        60, 40, 70, 110, 500,
        10, 5, 60, 75, 250,
        95, 40
    ],

    "rating": [
        4.8, 4.5, 4.2, 4.6, 4.1,
        3.9, 4.0, 4.3, 4.4, 4.1,
        4.7, 4.6, 4.2, 4.3, 3.8,
        4.5, 4.4, 4.0, 4.1, 3.9,
        4.6, 4.3
    ],

    "num_reviews": [
        500, 300, 150, 250, 180,
        90, 60, 120, 110, 95,
        200, 180, 75, 130, 40,
        50, 35, 80, 60, 45,
        220, 170
    ]
}

df = pd.DataFrame(data)

print("First 5 rows")
print(df.head())

print("\nDataFrame Info")
print(df.info())

print("\nSummary Statistics")
print(df.describe())

print("\nColumns")
print(df.columns)

print("\nShape")
print(df.shape)

print("\nMissing Values")
print(df.isnull().sum())


print("\nAll Electronics Products")
electronics = df.loc[df["category"] == "Electronics"]
print(electronics)

print("\nProducts rated > 4.0 and price < 5000")
filtered = df.loc[(df["rating"] > 4.0) & (df["price"] < 5000)]
print(filtered)

print("\nUpdating stock for Wireless Mouse")
df.loc[df["name"] == "Wireless Mouse", "stock"] = 130
print(df.loc[df["name"] == "Wireless Mouse"])


print("\nFirst 5 products")
print(df.iloc[:5])

print("\nLast 5 products")
print(df.iloc[-5:])

print("\nEvery other row")
print(df.iloc[::2])

print("\nRows 10-15 and columns 0-3")
print(df.iloc[10:16, 0:4])


budget_products = df[df["price"] < 1000]
premium_products = df[df["price"] > 10000]
popular_products = df[(df["num_reviews"] > 100) & (df["rating"] > 4.0)]

print("\nBudget Products")
print(budget_products)

print("\nPremium Products")
print(premium_products)

print("\nPopular Products")
print(popular_products)


filtered_dfs = {
    "budget_products": budget_products,
    "premium_products": premium_products,
    "popular_products": popular_products
}

for name, dataframe in filtered_dfs.items():
    dataframe.to_csv(f"{name}.csv", index=False)

print("\nCSV files exported successfully.")
