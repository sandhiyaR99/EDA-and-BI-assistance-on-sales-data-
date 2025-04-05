#!/usr/bin/env python
# coding: utf-8

# In[4]:


import streamlit as st
import pandas as pd


# In[5]:


df = pd.read_excel(r"C:\Users\USER\Downloads\Sales_data.xlsx", engine="openpyxl")


# In[9]:


df.head()


# In[ ]:


st.title("BI Assistant")
st.write("Ask me anything about your sales data!")

query = st.text_input("Enter your question:")

def answer_query(query, df):
    query = query.lower()

    if "total revenue" in query:
        total_revenue = df["Total Price"].sum()
        st.write("Total Revenue")
        st.write(f"${total_revenue:,.2f}")

    elif "total orders" in query:
        total_orders = df["Order ID"].nunique()
        st.write("Total unique Orders")
        st.write(total_orders)

    elif "top selling products" in query:
        top_products = df.groupby("Item ID")["Total Price"].sum().sort_values(ascending=False).head(5)
        st.write("Top 5 Selling Products")
        st.bar_chart(top_products)

    elif "items generating highest revenue" in query:
        top_items = df.groupby("Item ID")["Total Price"].sum().sort_values(ascending=False).head(10)
        st.write("Items Generating Highest Revenue")
        st.bar_chart(top_items)

    elif "customer returned the most items" in query:
        returns = df.groupby("Customer ID")["Qty Returned"].sum().sort_values(ascending=False).head(1)
        st.write("Customer with Most Returns")
        st.write(returns)

    elif "monthly sales trends" in query:
        df["Month"] = df["Order Date"].dt.to_period("M")
        monthly_sales = df.groupby("Month")["Total Price"].sum()
        st.write("Monthly Sales Trends")
        st.line_chart(monthly_sales)

    elif "best-selling warehouse" in query:
        warehouse_sales = df.groupby("Ship Warehouse")["Total Price"].sum().sort_values(ascending=False).head(1)
        st.write("Best-Selling Warehouse")
        st.write(warehouse_sales)

    elif "most profitable customer" in query:
        customer_profit = df.groupby("Customer ID")["Total Price"].sum().sort_values(ascending=False).head(1)
        st.write("Most Profitable Customer")
        st.write(customer_profit)

    elif "region with highest sales" in query:
        region_sales = df.groupby("Ship To")["Total Price"].sum().sort_values(ascending=False).head(1)
        st.write("Region with Highest Sales")
        st.write(region_sales)

    elif "average order value" in query:
        avg_order_value = df.groupby("Order ID")["Total Price"].sum().mean()
        st.write("Average Order Value")
        st.write(f"${avg_order_value:.2f}")

    elif "top 5 customers by sales" in query:
        top_customers = df.groupby("Customer ID")["Total Price"].sum().sort_values(ascending=False).head(5)
        st.write("Top 5 Customers by Sales")
        st.bar_chart(top_customers)

    elif "worst performing product" in query:
        worst_product = df.groupby("Item ID")["Total Price"].sum().sort_values(ascending=True).head(1)
        st.write("Worst-Performing Product")
        st.write(worst_product)

    elif "average shipping time" in query:
        avg_shipping_time = (df["Due Date"] - df["Order Date"]).dt.days.mean()
        st.write("Average Shipping Time (Days)")
        st.write(f"{avg_shipping_time:.1f} days")

    elif "sales distribution by warehouse" in query:
        warehouse_sales = df.groupby("Ship Warehouse")["Total Price"].sum()
        st.write("Sales Distribution by Warehouse")
        st.bar_chart(warehouse_sales)

    elif "top returned items" in query:
        returned_items = df.groupby("Item ID")["Qty Returned"].sum().sort_values(ascending=False).head(2)
        st.write("Top Returned Items")
        st.bar_chart(returned_items)

    elif "warehouse with most orders" in query:
        warehouse_orders = df["Ship Warehouse"].value_counts()
        st.write("Warehouse with Most Orders")
        st.bar_chart(warehouse_orders)

    elif "on-time vs delayed shipments" in query:
        df["On Time"] = df["Order Date"] <= df["Due Date"]
        on_time_ratio = df["On Time"].value_counts(normalize=True) * 100
        st.write("n-Time vs Delayed Shipments")
        st.bar_chart(on_time_ratio)

    else:
        st.write("I am sorry, I didn't understand that, please try asking about sales, customers, products,trends, revenue,warehouse")

if query:
    answer_query(query, df)

