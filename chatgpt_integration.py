import openai
import os

# Initialize the OpenAI API
openai.api_key = os.getenv('OPENAI_KEY')

def chatgpt_prompt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
    )
    return (response['choices'][0]['message']['content'].strip())
    #assistant_message = [msg for msg in response['choices'][0]['messages'] if msg['role'] == 'assistant']
    #return assistant_message[0]['content']

# Example: Get a code suggestion from ChatGPT
code_suggestion_prompt = "Write a Python function to calculate the factorial of a number using recursion."
code_suggestion = chatgpt_prompt(code_suggestion_prompt)
print("Code Suggestion:")
print(code_suggestion)