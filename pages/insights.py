# pages/insights.py
import streamlit as st
import pandas as pd
from .chatgpt_integration import get_chatgpt_response
from .cosine_model import calculate_cosine_similarity
from .recommendations import generate_recommendations

def display():
    st.title('Homebuyer Readiness Evaluation')
    
    data_source = st.radio('Select data source', ['Input your own data', 'Use original dataset'])
    df = None  # Initialize df to None
    
    if data_source == 'Input your own data':
      with st.form(key='user_input_form'):
        st.write('Please enter your data:')
        gross_monthly_income = st.number_input('Gross Monthly Income', value=0)
        credit_card_payment = st.number_input('Credit Card Payment', value=0)
        car_payment = st.number_input('Car Payment', value=0)
        student_loan_payments = st.number_input('Student Loan Payments', value=0)
        appraised_value = st.number_input('Appraised Value', value=0)
        down_payment = st.number_input('Down Payment', value=0)
        loan_amount = st.number_input('Loan Amount', value=0)
        monthly_mortgage_payment = st.number_input('Monthly Mortgage Payment', value=0)
        credit_score = st.number_input('Credit Score', value=0)
        
        submitted = st.form_submit_button('Submit')
        
        if submitted:
            data = {
                'GrossMonthlyIncome': [gross_monthly_income],
                'CreditCardPayment': [credit_card_payment],
                'CarPayment': [car_payment],
                'StudentLoanPayments': [student_loan_payments],
                'AppraisedValue': [appraised_value],
                'DownPayment': [down_payment],
                'LoanAmount': [loan_amount],
                'MonthlyMortgagePayment': [monthly_mortgage_payment],
                'CreditScore': [credit_score]
            }
            df = pd.DataFrame(data)
            st.write(df)
            
            # Now inside the if submitted: block
            similarity_matrix = calculate_cosine_similarity(df)
            user_index = st.selectbox('Select the index of the user for recommendations', df.index)
            
            if st.button('Generate Recommendations'):
                recommendations = generate_recommendations(df, similarity_matrix, user_index)
                st.write(recommendations)

    elif data_source == 'Use original dataset':
        uploaded_file = st.file_uploader("Upload your dataset", type=["csv", "xlsx"])
        
        if uploaded_file is not None:
            df = pd.read_excel(uploaded_file) if uploaded_file.type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" else pd.read_csv(uploaded_file)
            st.write(df.head())
            
            # Now inside the if uploaded_file is not None: block
            similarity_matrix = calculate_cosine_similarity(df)
            user_index = st.selectbox('Select the index of the user for recommendations', df.index)
            
            if st.button('Generate Recommendations'):
                recommendations = generate_recommendations(df, similarity_matrix, user_index)
                st.write(recommendations)

    # ChatGPT advice
    question = st.text_input('Ask for advice or clarification:')
    if question:
        if df is not None and not df.empty:
            user_financial_data = df.iloc[user_index].to_string()
            response = get_chatgpt_response(question, user_financial_data)
            st.write(response)
        else:
            st.warning("Please input data or upload a dataset to proceed.")

