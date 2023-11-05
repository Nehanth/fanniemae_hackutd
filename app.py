import streamlit as st
import pandas as pd
from chatgpt_integration import get_chatgpt_response
from cosine_model import calculate_cosine_similarity
from recommendations import generate_recommendations

st.set_page_config(layout="wide")

st.title('Homebuyer Readiness Evaluation')

# Option for user to select the dataset source
dataset_option = st.selectbox(
    'Select your dataset source',
    ('Upload my dataset', 'Use HackUTD-2023-HomeBuyerInfo dataset')
)

if dataset_option == 'Upload my dataset':
    uploaded_file = st.file_uploader("Upload your dataset", type=["csv", "xlsx"])
    if uploaded_file is not None:
        # Process the file uploaded
        df = pd.read_csv(uploaded_file)
        st.write(df.head())
else:
    # Load the predefined dataset
    df = pd.read_csv('HackUTD-2023-HomeBuyerInfo.csv')  # replace with the actual path to your dataset
    st.write(df)

# Proceed with the rest of the app if a dataset is loaded
if 'df' in locals():
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

# Run the Streamlit app with `streamlit run app.py`
