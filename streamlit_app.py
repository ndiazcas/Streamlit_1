import streamlit as st
import pandas as pd

st.title("Data App Assignment")

st.write("### Input Data and Examples")
df = pd.read_csv("Superstore_Sales_utf8.csv", parse_dates=True)
st.dataframe(df)

# This bar chart will not have solid bars--but lines--because the detail data is being graphed independently
st.bar_chart(df, x="Category", y="Sales")

# Now let's do the same graph where we do the aggregation first in Pandas... (this results in a chart with solid bars)
st.dataframe(df.groupby("Category").sum())
# Using as_index=False here preserves the Category as a column.  If we exclude that, Category would become the datafram index and we would need to use x=None to tell bar_chart to use the index
st.bar_chart(df.groupby("Category", as_index=False).sum(), x="Category", y="Sales", color="#04f")

# Aggregating by time
# Here we ensure Order_Date is in datetime format, then set is as an index to our dataframe
df["Order_Date"] = pd.to_datetime(df["Order_Date"])
df.set_index('Order_Date', inplace=True)
# Here the Grouper is using our newly set index to group by Month ('M')
sales_by_month = df.filter(items=['Sales']).groupby(pd.Grouper(freq='M')).sum()

st.dataframe(sales_by_month)

# Here the grouped months are the index and automatically used for the x axis
st.line_chart(sales_by_month, y="Sales")

st.write("## Your additions")
st.write("### (1) add a drop down for Category (https://docs.streamlit.io/library/api-reference/widgets/st.selectbox)")
st.write("### (2) add a multi-select for Sub_Category *in the selected Category (1)* (https://docs.streamlit.io/library/api-reference/widgets/st.multiselect)")
st.write("### (3) show a line chart of sales for the selected items in (2)")
st.write("### (4) show three metrics (https://docs.streamlit.io/library/api-reference/data/st.metric) for the selected items in (2): total sales, total profit, and overall profit margin (%)")
st.write("### (5) use the delta option in the overall profit margin metric to show the difference between the overall average profit margin (all products across all categories)")


# Create a dropdown for selecting a category
option = st.selectbox('Select a category:', df['Category'].unique(), placeholder="Select category...")
st.write('You selected:', option)

# Filter df based on the selected category
filtered_df = df[df['Category'] == option]

# Create a multiselect for selecting data based on the selected category
options = st.multiselect('Select data:', filtered_df['Sub_Category'].unique())

# Display the selected data
st.write('Selected data:', options)

# Show a line chart of sales for the selected items in option and options
# If selected_data is not empty, filter data based on selected_data
if options:
    filtered_df = filtered_df[filtered_df['Sub_Category'].isin(options)]
    st.dataframe(filtered_df)

# Aggregate sales data by month
# filtered_df['Order_Date'] = pd.to_datetime(filtered_df['Order_Date'])
filtered_df.set_index('Order_Date', inplace=True)
aggregated_data = filtered_df.filter(items=['Sales']).groupby(pd.Grouper(freq='M')).sum()
st.dataframe(aggregated_data)

# Plot the line chart
if not aggregated_data.empty:
    st.write('Line chart for selected Category and Sub_Categories:')
    st.line_chart(aggregated_data, y="Sales")
else:
    st.write('No data available for the selected category and sub_categories.')