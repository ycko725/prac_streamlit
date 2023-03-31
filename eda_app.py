import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt 
import plotly.express as px 
import seaborn as sns
import scipy.stats as stats
import plotly.graph_objects as go

def run_eda_app():

    st.title("Research Information")

    iris_df = pd.read_csv('data/iris.csv')

    submenu = st.sidebar.selectbox("Submenu", ['Tables', 'Graph'])
    if submenu == "Tables":
        st.dataframe(iris_df)

        with st.expander("Data Types"):
            result = pd.DataFrame(iris_df.dtypes).transpose()
            result.index = ["Data Type"]
            st.dataframe(result)

        with st.expander("Information"):
            result2 = pd.DataFrame(iris_df.describe()).transpose()
            st.dataframe(result2)

        with st.expander("Species"):
            result3 = iris_df['species'].value_counts()
            st.dataframe(result3)

    elif submenu == "Graph":
        st.subheader("Plots")
        fig1 = px.scatter(iris_df, 
                          x = 'sepal_width', 
                          y = 'sepal_length', 
                          color = 'species', 
                          size = 'petal_width', 
                          hover_data = ['petal_length'], 
                          title = "Scatter Plot")
        st.plotly_chart(fig1)
        

        col1, col2 = st.columns(2)
        with col1:
            with st.expander("Boxplot with Seaborn"):
                fig, ax = plt.subplots()
                sns.boxplot(iris_df, x = 'species', y = 'sepal_length', ax = ax)
                st.pyplot(fig)
        with col2:
            with st.expander("Histogram with matplotlib"):
                fig, ax = plt.subplots()
                ax.hist(iris_df['sepal_length'], color = 'green')
                st.pyplot(fig)

        tab1, tab2 = st.tabs(['Scatter Plot', 'Scatter Plot with Regression Line'])
        with tab1:
            val_species = st.selectbox('Select Species', ('Iris-setosa', 'Iris-versicolor', 'Iris-virginica'))
            st.write('Select Species:', val_species)

            result = iris_df[iris_df['species'] == val_species]
            st.dataframe(result)

            fig1 = px.scatter(result, 
                              x = 'sepal_width', 
                              y = 'sepal_length', 
                              size = 'petal_width', 
                              hover_data = ['petal_length'])
            st.plotly_chart(fig1)

        with tab2:
            val_species2 = st.selectbox('Select Species', ('Iris-setosa', 'Iris-versicolor', 'Iris-virginica'), key='species2')
            st.write('Select Species:', val_species2)

            result2 = iris_df[iris_df['species'] == val_species2]
            st.dataframe(result2)

            fig2 = px.scatter(result2, 
                            x='sepal_width', 
                            y='sepal_length', 
                            size='petal_width', 
                            hover_data=['petal_length'])
                    
            slope, intercept, r_value, p_value, std_err = stats.linregress(result2['sepal_width'], result2['sepal_length'])
            line = slope * result2['sepal_width'] + intercept
            fig2.add_trace(go.Scatter(x=result2['sepal_width'], y=line, name='Regression Line', line=dict(color='red')))
            st.plotly_chart(fig2)

    else:
        st.write("What is this for anyways?")