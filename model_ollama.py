import requests
from model_base import BaseLLM 
import ollama

DEFAULT_MODEL = "llama3.2"

class ModalOllama(BaseLLM):
  def __init__(self, api_url, model=DEFAULT_MODEL):
      self.api_url = api_url
      self.model = model
      self.initialize_model()
  
  def initialize_model(self):
        # Placeholder for potential Ollama-specific setup
        pass
  
  def chat(self, prompt):
        try:
          response = ollama.chat(self.model, prompt)
          return response['message']['content']
        except requests.RequestException as e:
            return f"Ollama API error: {e}"
