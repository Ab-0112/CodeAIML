import ollama

class ChatOllama:
    def __init__(self, model_name):
        self.model_name = model_name

    def get_response(self, prompt):
        response = ollama.chat(model=self.model_name, messages=[{"role": "user", "content": prompt}])
        return response["message"]["content"]

# Example usage:
# chat_model = ChatOllama("mistral")
# print(chat_model.get_response("What is AI?"))
