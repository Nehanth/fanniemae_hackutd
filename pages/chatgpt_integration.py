# In chatgpt_integration.py
import openai
openai.api_key = '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'


def get_chatgpt_response(question, user_financial_data):
    # Format the user data and question as a conversation with a series of messages
    messages = [
        {"role": "system", "content": "You are a loan officer."},
        {"role": "user", "content": f"The user has the following financial data:\n{user_financial_data}"},
        {"role": "user", "content": question}
    ]
    
    # Use the 'gpt-3.5-turbo' engine and the 'v1/chat/completions' endpoint
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=150,
        temperature=0.1  # Set the temperature to 0.1 for more focused and definitive responses
    )
    
    # Extract the text from the response
    answer = response['choices'][0]['message']['content'].strip()
    return answer
