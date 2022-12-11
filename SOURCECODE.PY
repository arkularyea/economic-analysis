# nii arku laryea / nii.azubiafrica.org
import pandas as pd

#Data entities in dictionary
Data = {
    "product id" : [23, 96, 97, 15, 87],
    "name" : ["computer", "Python Workout", "Pandas Workout", "banana", "sandwich"],
    "wholesale_price" : [500, 35, 35, 0.5, 3],
    "retail_price": [1000, 75, 75, 1, 5],
    "sales" : [100, 1000, 500, 200, 300]
}

print()
#Convert dictionary to dataframe
df_Data = pd.DataFrame(Data)
print(df_Data)

print()
#Calculate Total profit for each product
df_Data["net_revenue_per_product"] = (df_Data["retail_price"] - df_Data["wholesale_price" ]) * df_Data["sales"]
print(df_Data)

print()
#Total revenue from all sales
Total_revenue = df_Data["net_revenue_per_product"].sum()
print(f"Total net revenue from all sales is {Total_revenue}")

print()
#Products with retail price more than twice the wholesale price
filter = df_Data.loc[df_Data["retail_price"] > (df_Data["wholesale_price"] * 2)]
print("Products with retail price more than twice the wholesale price")
print(filter)

print()
#How much did the store make from food vs. computers vs. books
Food_Revenue = sum(df_Data.iloc[[3,4]]["net_revenue_per_product"])
print(f"Food Revenue: {Food_Revenue}")

Computer_Revenue = (df_Data.iloc[0]["net_revenue_per_product"])
print(f"Computer Revenue: {Computer_Revenue}")

Books_Revenue = sum(df_Data.iloc[[1,2]]["net_revenue_per_product"])
print(f"Books Revenue: {Books_Revenue}")

print()
#New net revenue with 30% discount
df_Data["wholesale_discount"] = df_Data["wholesale_price"] * (30/100)

df_Data["new_net_revenue_per_product"] = (df_Data["retail_price"] - (df_Data["wholesale_price"] - df_Data["wholesale_discount"])) * df_Data["sales"]
print(df_Data)

print()
#Total new net revenue from all sales
Total_new_net_revenue = df_Data["new_net_revenue_per_product"].sum()
print(f"Total net revenue from all sales is {Total_new_net_revenue}")

