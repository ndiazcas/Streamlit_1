import streamlit as st
import pandas as pd

st.title("Data App Assignment")

st.write("### Input Data and Examples")
df = pd.read_csv("Superstore_Sales_utf8.csv", parse_dates=True)
st.dataframe(df)

option = st.selectbox(
   "Which Category would you like to see?",
   (df['Category'].unique()),
   index=None,
   placeholder="Select category...",
)
st.write('You selected:', option)

if option == 'Furniture':
   st.bar_chart(df, x=df[df['Category'] == 'Furniture'], y='Sales')

   st.dataframe(df.groupby("Category").sum())
   st.bar_chart(df.groupby("Category", as_index=False).sum(), x=df[df['Category'] == 'Furniture'], y="Sales", color="#04f")
   
   df["Order_Date"] = pd.to_datetime(df["Order_Date"])
   df.set_index('Order_Date', inplace=True)
   sales_by_month_furniture = df.filter(items=['Sales', df['Category'] == 'Furniture']).groupby(pd.Grouper(freq='M')).sum()
   
   st.dataframe(sales_by_month_furniture)
   
   st.line_chart(sales_by_month_furniture, y="Sales")

   elif option == 'Office Supplies':
      st.bar_chart(df, x=df[df['Category'] == 'Office Supplies'], y='Sales')

      st.dataframe(df.groupby("Category").sum())
      st.bar_chart(df.groupby("Category", as_index=False).sum(), x=df[df['Category'] == 'Office Supplies'], y="Sales", color="#04f")
   
      df["Order_Date"] = pd.to_datetime(df["Order_Date"])
      df.set_index('Order_Date', inplace=True)
      sales_by_month_office = df.filter(items=['Sales', df['Category'] == 'Office Supplies']).groupby(pd.Grouper(freq='M')).sum()
   
      st.dataframe(sales_by_month_office)
   
      st.line_chart(sales_by_month_office, y="Sales")

   else:
      st.bar_chart(df, x=df[df['Category'] == 'Technology'], y='Sales')

      st.dataframe(df.groupby("Category").sum())
      st.bar_chart(df.groupby("Category", as_index=False).sum(), x=df[df['Category'] == 'Technology'], y="Sales", color="#04f")
   
      df["Order_Date"] = pd.to_datetime(df["Order_Date"])
      df.set_index('Order_Date', inplace=True)
      sales_by_month_tech = df.filter(items=['Sales', df['Category'] == 'Technology']).groupby(pd.Grouper(freq='M')).sum()
   
      st.dataframe(sales_by_month_tech)
   
      st.line_chart(sales_by_month_tech, y="Sales")

