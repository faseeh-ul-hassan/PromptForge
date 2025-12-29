import google.generativeai as genai

class GeminiModel:
    def __init__(self, api_key, system_prompt):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(
            model_name="gemini-2.5-flash",
            system_instruction=system_prompt
        )
        self.chat = self.model.start_chat()

    def send(self, prompt: str) -> str:
        response = self.chat.send_message(prompt)
        return response.text
