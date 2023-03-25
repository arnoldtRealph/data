import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Set the title of the web page
st.title('Learner Data Analysis')

# Allow the user to upload an excel file
uploaded_file = st.file_uploader("Choose an Excel file", type="xlsx")

if uploaded_file is not None:
    # Load the excel file into a pandas dataframe
    df = pd.read_excel(uploaded_file)

    # Display the dataframe in a table
    st.write(df)

    # Ask the user which analysis to perform
    analysis = st.selectbox("Select an analysis", ["Distribution of Marks", "Marks vs. Learner Names", "Box Plot of Marks", "Number of Learners per Mark"])

    if analysis == "Distribution of Marks":
        # Display a histogram of the marks
        fig = px.histogram(df, x="Marks", nbins=10, title="Distribution of Marks", color_discrete_sequence=['#FFC300'])
        st.plotly_chart(fig)

    elif analysis == "Marks vs. Learner Names":
        # Display a scatter plot of the marks vs. the learner names
        fig = px.scatter(df, x="Learner names", y="Marks", title="Marks vs. Learner Names", color="Marks", color_continuous_scale='RdBu')
        st.plotly_chart(fig)

    elif analysis == "Box Plot of Marks":
        # Create a box plot of the marks
        fig = go.Figure()
        fig.add_trace(go.Box(y=df['Marks'], name='Marks', boxpoints="outliers", marker=dict(color='#FF5733')))
        fig.update_layout(title='Box Plot of Marks', yaxis_title='Marks')
        st.plotly_chart(fig)

    elif analysis == "Number of Learners per Mark":
        # Create a bar chart of the number of learners who achieved each mark
        counts = df['Marks'].value_counts()
        fig = go.Figure()
        fig.add_trace(go.Bar(x=counts.index, y=counts.values, name='Number of Learners', marker=dict(color='#4CAF50')))
        fig.update_layout(title='Number of Learners per Mark', xaxis_title='Marks', yaxis_title='Number of Learners')
        st.plotly_chart(fig)

    # Calculate and display some statistics about the data
    mean = df['Marks'].mean()
    st.write(f"Mean: {mean:.2f}")
    median = df['Marks'].median()
    st.write(f"Median: {median:.2f}")
    mode = df['Marks'].mode()[0]
    st.write(f"Mode: {mode}")
