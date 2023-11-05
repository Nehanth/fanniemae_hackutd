# pages/insights.py
import streamlit as st
import pandas as pd
from .chatgpt_integration import get_chatgpt_response
from .cosine_model import calculate_cosine_similarity
from .recommendations import generate_recommendations

def display():
    st.title('Homebuyer Readiness Evaluation')

    uploaded_file = st.file_uploader("Upload your dataset", type=["csv", "xlsx"])
    if uploaded_file is not None:
        if uploaded_file.type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
            df = pd.read_excel(uploaded_file)
        else:
            df = pd.read_csv(uploaded_file)

        st.write(df.head())

        # Calculate Cosine Similarity
        similarity_matrix = calculate_cosine_similarity(df)

        # Select User
        user_index = st.selectbox('Select the index of the user for recommendations', df.index)

        # Generate recommendations
        if st.button('Generate Recommendations'):
            recommendations = generate_recommendations(df, similarity_matrix, user_index)
            st.write(recommendations)

        # ChatGPT advice
        question = st.text_input('Ask for advice or clarification:')
        if question:
            response = get_chatgpt_response(question)
            st.write(response)
