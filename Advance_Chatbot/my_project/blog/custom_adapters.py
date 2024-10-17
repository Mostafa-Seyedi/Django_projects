import os
import openai
from chatterbot.logic import LogicAdapter
from django.conf import settings

class OpenAILogicAdapter(LogicAdapter):
    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)
        self.api_key = settings.OPENAI_API_KEY  # Ensure this line is after loading settings
        openai.api_key = self.api_key

    def can_process(self, statement):
        return True  # This adapter can process any input.

    def process(self, input_statement, additional_response_selection_parameters=None):
        response = self.get_openai_response(input_statement.text)
        response_statement = self.chatbot.storage.get_or_create(response)
        response_statement.confidence = 1  # Set a high confidence for this adapter
        return response_statement

    def get_openai_response(self, user_input):
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",  # or any other GPT engine
                prompt=user_input,
                max_tokens=150,  # Adjust this value as needed
                n=1,
                stop=None,
                temperature=0.7,
            )
            return response.choices[0].text.strip()
        except Exception as e:
            return f"An error occurred: {str(e)}"
