import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
import streamlit as st

st.title("Diwali Sales Analysis")

# File uploader
uploaded_file = st.file_uploader("Choose a file", type=["csv"])

if uploaded_file is not None:
    # Load the data
    df = pd.read_csv(uploaded_file, encoding='unicode_escape')
    
    # Drop unnecessary columns
    df.drop(['Status', 'unnamed1'], axis=1, inplace=True)

    # Drop rows with missing values
    df.dropna(inplace=True)

    # Convert Amount column to integer type
    df['Amount'] = df['Amount'].astype('int')

    # Rename columns
    df.rename(columns={'Marital_Status': 'Shaadi'}, inplace=True)

    # Plotting a countplot for Gender
    fig, ax = plt.subplots()
    sns.countplot(x='Gender', data=df, ax=ax)
    for bars in ax.containers: 
        ax.bar_label(bars)

    # Display the countplot in Streamlit
    st.pyplot(fig)

    # Plotting a bar chart for gender vs total amount
    if st.button("Find"):
        sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
        
        fig2, ax2 = plt.subplots()
        sns.barplot(x='Gender', y='Amount', data=sales_gen, ax=ax2)
        
        # Display the bar chart in Streamlit
        st.pyplot(fig2)
else:
    st.write("Please upload a CSV file.")
