import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\alpes\OneDrive\Desktop\DataCentre\DataFiles\Walmart_Sales.csv")

print(data.info())

# Convert 'Date' to datetime format
data['Date'] = pd.to_datetime(data['Date'], format='%d-%m-%Y')

# Check for missing values 
print(data.isnull().sum())

# Convert the 'Holiday_Flag' to a categorical column (for better visualization)
data['Holiday_Flag'] = data['Holiday_Flag'].astype('category')

# Sales distribution (Weekly_Sales)
fig = px.histogram(data, x='Weekly_Sales', title='Weekly Sales Distribution')

# Sales by Store
fig = px.bar(data, x='Store', y='Weekly_Sales', color='Store', title='Weekly Sales by Store')
fig.show()

# Correlation heatmap
corr_matrix = data.corr()
fig = px.imshow(corr_matrix, text_auto=True, title='Correlation Heatmap')
fig.show()

import streamlit as st

st.title('My First Streamlit App')
st.write('Hello, world!')

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load Walmart dataset
data = pd.read_csv('C:/Users/alpes/OneDrive/Desktop/DataCentre/DataFiles/Walmart_Sales.csv')

# Convert 'Date' column to datetime
data['Date'] = pd.to_datetime(data['Date'],format='%d-%m-%Y')

# Convert 'Holiday_Flag' to categorical type for better visualization
data['Holiday_Flag'] = data['Holiday_Flag'].astype('category')

# Sidebar for filters
st.sidebar.header('Filter Data')

# Filter by store
store_filter = st.sidebar.multiselect(
    'Select Store',
    options=data['Store'].unique(),
    default=data['Store'].unique()
)

# Filter by holiday flag
holiday_filter = st.sidebar.multiselect(
    'Select Holiday Flag',
    options=data['Holiday_Flag'].unique(),
    default=data['Holiday_Flag'].unique()
)

# Filter DataFrame based on selections
df_selection = data.query(
    "Store == @store_filter & Holiday_Flag == @holiday_filter"
)

# Display filtered data
st.subheader('Filtered Walmart Sales Data')
st.write(df_selection)

# Sales Distribution
st.subheader('Sales Distribution')
fig1 = px.histogram(df_selection, x='Weekly_Sales', title='Weekly Sales Distribution')
st.plotly_chart(fig1)

# Sales Over Time
st.subheader('Sales Over Time')
fig2 = px.line(df_selection, x='Date', y='Weekly_Sales', title='Sales Over Time')
st.plotly_chart(fig2)

# Sales by Store
st.subheader('Sales by Store')
fig3 = px.bar(df_selection, x='Store', y='Weekly_Sales', color='Store', title='Weekly Sales by Store')
st.plotly_chart(fig3)

# Correlation Heatmap
st.subheader('Correlation Heatmap')
fig4 = go.Figure(go.Heatmap(z=df_selection.corr(), colorscale='Viridis', x=df_selection.columns, y=df_selection.columns))
fig4.update_layout(title='Correlation Heatmap')
st.plotly_chart(fig4)

# Weekly Sales vs Temperature
st.subheader('Weekly Sales vs Temperature')
fig5 = px.scatter(df_selection, x='Temperature', y='Weekly_Sales', color='Holiday_Flag', title='Sales vs Temperature')
st.plotly_chart(fig5)

# Weekly Sales vs Fuel Price
st.subheader('Weekly Sales vs Fuel Price')
fig6 = px.scatter(df_selection, x='Fuel_Price', y='Weekly_Sales', color='Holiday_Flag', title='Sales vs Fuel Price')
st.plotly_chart(fig6)

# Key Metrics (KPI cards)
st.subheader('Key Metrics')

# Average Weekly Sales
avg_sales = df_selection['Weekly_Sales'].mean()
st.metric(label="Average Weekly Sales", value=f"${avg_sales:,.2f}")

# Total Weekly Sales
total_sales = df_selection['Weekly_Sales'].sum()
st.metric(label="Total Weekly Sales", value=f"${total_sales:,.2f}")

# Total Number of Stores
total_stores = df_selection['Store'].nunique()
st.metric(label="Total Stores", value=total_stores)