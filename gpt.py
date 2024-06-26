import openai
from keys import OPENAI_API_KEY

def get_completions(systemMessage, userMessage, model, temperature):
    openai.api_key = OPENAI_API_KEY

    completion = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": systemMessage},
            {"role": "user", "content": userMessage}
        ],
        temperature=temperature
    )
    return completion.choices[0].message.content
