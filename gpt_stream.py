import openai
from keys import OPENAI_API_KEY

def get_completions_stream(systemMessage, userMessage, model, temperature):
    openai.api_key = OPENAI_API_KEY

    completion = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": systemMessage},
            {"role": "user", "content": userMessage}
        ],
        temperature=temperature,
        stream = True
    )
    return completion
