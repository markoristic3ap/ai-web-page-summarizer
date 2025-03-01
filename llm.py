from enum import Enum
from llm_models.model_openai import ModelOpenAI
from llm_models.model_ollama import ModalOllama

class SUPPORTED_LLMS(Enum):
  OPEN_AI = 'openai',
  OLLAMA = 'ollama',

class LLMInterface:
  def __init__(self, provider = SUPPORTED_LLMS.OPEN_AI, **kwargs):
    self.llm = self.initialize_llm(provider, **kwargs)

  def initialize_llm(self, provider, **kwargs):
    if provider == SUPPORTED_LLMS.OPEN_AI:
      return ModelOpenAI()
    elif provider == SUPPORTED_LLMS.OLLAMA:
      return ModalOllama()
    else:
      raise Exception('Unsupported LLM provider')


  def chat(self, prompt):
    return self.llm.chat(prompt)