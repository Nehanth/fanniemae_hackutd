import openai

# Set your OpenAI API key here
openai.api_key = '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'

def get_chatgpt_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()
