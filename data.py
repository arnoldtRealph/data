import streamlit as st
import pandas as pd
import plotly.express as px

# Set the title of the web page
st.title('Learner Data Analysis')

# Allow the user to upload an excel file
uploaded_file = st.file_uploader("Choose an Excel file", type="xlsx")

if uploaded_file is not None:
    # Load the excel file into a pandas dataframe
    df = pd.read_excel(uploaded_file)

    # Display the dataframe in a table
    st.write(df)

    # Display a histogram of the marks
    fig = px.histogram(df, x="Marks", nbins=10, title="Distribution of Marks")
    st.plotly_chart(fig)

    # Display a scatter plot of the marks vs. the learner names
    fig = px.scatter(df, x="Learner names", y="Marks", title="Marks vs. Learner Names")
    st.plotly_chart(fig)

    # Calculate and display some statistics about the data
    mean = df['Marks'].mean()
    st.write(f"Mean: {mean:.2f}")
    median = df['Marks'].median()
    st.write(f"Median: {median:.2f}")
    mode = df['Marks'].mode()[0]
    st.write(f"Mode: {mode}")
