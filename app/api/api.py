import os
import json
from enum import Enum
from pathlib import Path
from typing import List, Tuple, Dict, Optional
import openai
from openai import OpenAI


def load_config() -> dict:
    """Load the configuration from config.json file."""
    config_path = Path(__file__).parent.parent.parent / "config.json"
    with open(config_path) as f:
        return json.load(f)


# Create ModelProvider enum from config
config_data = load_config()
ModelProvider = Enum('ModelProvider', {
    provider.upper(): provider 
    for provider in config_data["providers"].keys()
}, type=str)


class ModelConfig:
    """Configuration class for each model provider."""
    def __init__(self, base_url: str, api_key: str, available_models: List[str]):
        self.base_url = base_url
        self.api_key = api_key if api_key == "ollama" else os.environ.get(api_key, "")
        self.available_models = available_models
        self._client: Optional[OpenAI] = None

    @property
    def client(self) -> OpenAI:
        """Lazy initialization of OpenAI client."""
        if not self._client:
            self._client = OpenAI(
                base_url=self.base_url,
                api_key=self.api_key,
            )
        return self._client


class ChatAPI:
    """Main API class for handling chat operations."""
    def __init__(self):
        self.provider_configs = self._load_provider_configs()

    @staticmethod
    def _load_provider_configs() -> Dict[ModelProvider, ModelConfig]:
        """Initialize provider configurations from config file."""
        config_data = load_config()
        return {
            ModelProvider[provider_name.upper()]: ModelConfig(
                base_url=provider_config["base_url"],
                api_key=provider_config["api_key"],
                available_models=provider_config["available_models"],
            )
            for provider_name, provider_config in config_data["providers"].items()
        }

    def get_available_providers(self) -> List[str]:
        """Get list of available providers."""
        return [provider.value for provider in ModelProvider]

    def get_available_models(self, provider: str) -> List[str]:
        """Get available models for a specific provider."""
        provider_enum = ModelProvider[provider.upper()]
        return self.provider_configs[provider_enum].available_models

    def get_chat_response(
        self, 
        prompt: str, 
        provider: str, 
        model: str, 
        chat_history: Optional[List[Tuple[str, str]]] = None
    ) -> str:
        """
        Get a chat response from the specified provider and model.
        
        Args:
            prompt: The user's input prompt
            provider: The provider to use (e.g., "openai", "anthropic")
            model: The specific model to use
            chat_history: Optional list of previous (user, assistant) message pairs
            
        Returns:
            The model's response as a string
            
        Raises:
            ValueError: If the model is not available for the provider
            Exception: If there's an error communicating with the provider
        """
        provider_enum = ModelProvider[provider.upper()]
        config = self.provider_configs[provider_enum]

        if model not in config.available_models:
            raise ValueError(f"Model '{model}' not available for provider '{provider}'")

        messages = []
        if chat_history:
            for user_msg, assistant_msg in chat_history:
                messages.extend([
                    {"role": "user", "content": user_msg},
                    {"role": "assistant", "content": assistant_msg}
                ])

        messages.append({"role": "user", "content": prompt})

        try:
            chat_completion = config.client.chat.completions.create(
                messages=messages,
                model=model,
            )
            return chat_completion.choices[0].message.content
        except Exception as e:
            raise Exception(f"Error with {provider}: {str(e)}")


# Initialize the API
chat_api = ChatAPI()

# Export the public functions
get_available_providers = chat_api.get_available_providers
get_available_models = chat_api.get_available_models
get_chat_response = chat_api.get_chat_response
