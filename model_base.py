from abc import ABC, abstractmethod

class BaseLLM(ABC):
  @abstractmethod
  def initialize_model(self):
    """Initialize the model. Must be implemented by subclasses."""
    pass
  
  @abstractmethod
  def chat(self, prompt):
    """Send a prompt to the LLM and return the response."""
    pass
