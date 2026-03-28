import pandas as pd

jan_data = {
    "order_id": [1,2,3,4,5,6,7],
    "product": ["Laptop","Mouse","Keyboard","Monitor","Mouse","Laptop","Speaker"],
    "price": [70000,800,1500,12000,800,70000,2000],
    "quantity": [1,2,1,1,3,1,2]
}

feb_data = {
    "order_id": [8,9,10,11,12,13,14],
    "product": ["Laptop","Keyboard","Mouse","Monitor","Speaker","Mouse","Laptop"],
    "price": [72000,1500,900,12500,2100,900,72000],
    "quantity": [1,2,3,1,2,1,1]
}

mar_data = {
    "order_id": [15,16,17,18,19,20,21],
    "product": ["Monitor","Mouse","Laptop","Keyboard","Speaker","Mouse","Laptop"],
    "price": [13000,850,71000,1600,2200,850,71000],
    "quantity": [1,4,1,2,2,2,1]
}

jan_df = pd.DataFrame(jan_data)
feb_df = pd.DataFrame(feb_data)
mar_df = pd.DataFrame(mar_data)


for df in [jan_df, feb_df, mar_df]:
    df["revenue"] = df["price"] * df["quantity"]


def monthly_metrics(df):

    total_revenue = df["revenue"].sum()

    avg_order_value = df["revenue"].mean()

    top_product = (
        df.groupby("product")["quantity"]
        .sum()
        .idxmax()
    )

    return total_revenue, avg_order_value, top_product


jan_metrics = monthly_metrics(jan_df)
feb_metrics = monthly_metrics(feb_df)
mar_metrics = monthly_metrics(mar_df)


summary = pd.DataFrame({
    "Total Revenue": [jan_metrics[0], feb_metrics[0], mar_metrics[0]],
    "Average Order Value": [jan_metrics[1], feb_metrics[1], mar_metrics[1]],
    "Top Selling Product": [jan_metrics[2], feb_metrics[2], mar_metrics[2]]
}, index=["January", "February", "March"])

print("\nSummary Comparison Report")
print(summary)


print("\nHigh Revenue Orders (> 20000) in January")
high_orders = jan_df.query("revenue > 20000")
print(high_orders)


all_sales = pd.concat(
    [jan_df.assign(month="January"),
     feb_df.assign(month="February"),
     mar_df.assign(month="March")]
)

print("\nCombined Sales Data")
print(all_sales.head())


print("\nTop 3 Largest Orders by Revenue")
largest_orders = all_sales.nlargest(3, "revenue")
print(largest_orders)

print("\nSmallest 3 Orders by Revenue")
smallest_orders = all_sales.nsmallest(3, "revenue")
print(smallest_orders)