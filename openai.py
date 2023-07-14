import openai

# OpenAI API key (replace with your own key)
OPENAI_API_KEY = 'YOUR_OPENAI_API_KEY'

# Set up OpenAI API
openai.api_key = OPENAI_API_KEY

# Define a function to generate a ChatGPT response


def generate_response(message):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=message,
        max_tokens=50,
        temperature=0.7,
        n=1,
        stop=None,
        log_level="info"
    )
    return response.choices[0].text.strip()
