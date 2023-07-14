import openai


class ChatGPT:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = self.api_key

    def generate_response(self, message):
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

    def initial_setup(self):
        prompt = "Become the perfect customer support chat member by learning from me. Let's have a conversation where I act as a customer, and you respond as a customer support representative. This way, you'll be able to understand and answer my clients exactly like a professional. Let's get started!"
        response = self.generate_response(prompt)
        return response
