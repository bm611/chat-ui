import os
import openai
from typing import List, Tuple
from enum import Enum


class ModelProvider(Enum):
    CEREBRAS = "cerebras"
    OPENAI = "openai"
    ANTHROPIC = "anthropic"
    # Add more providers as needed


class ModelConfig:
    def __init__(self, base_url: str, api_key: str, available_models: List[str]):
        self.base_url = base_url
        self.api_key = api_key
        self.available_models = available_models
        self._client = None

    @property
    def client(self):
        if not self._client:
            self._client = openai.OpenAI(
                base_url=self.base_url,
                api_key=self.api_key,
            )
        return self._client


# Configuration for different providers
PROVIDER_CONFIGS: dict[ModelProvider, ModelConfig] = {
    ModelProvider.CEREBRAS: ModelConfig(
        base_url="https://api.cerebras.ai/v1",
        api_key=os.environ.get("CEREBRAS_API_KEY", ""),
        available_models=["llama3.1-8b"],
    ),
    ModelProvider.OPENAI: ModelConfig(
        base_url="https://api.openai.com/v1",
        api_key=os.environ.get("OPENAI_API_KEY", ""),
        available_models=["gpt-3.5-turbo", "gpt-4"],
    ),
}


def get_available_providers():
    return [provider.value for provider in ModelProvider]


def get_available_models(provider: str):
    provider_enum = ModelProvider(provider)
    return PROVIDER_CONFIGS[provider_enum].available_models


def get_chat_response(
    prompt: str, provider: str, model: str, chat_history: List[Tuple[str, str]] = None
):
    provider_enum = ModelProvider(provider)
    config = PROVIDER_CONFIGS[provider_enum]

    # Validate model selection
    if model not in config.available_models:
        raise ValueError(f"Model {model} not available for provider {provider}")

    # Convert chat history into messages format
    messages = []

    # Add previous conversation context if exists
    if chat_history:
        for user_msg, assistant_msg in chat_history:
            messages.append({"role": "user", "content": user_msg})
            messages.append({"role": "assistant", "content": assistant_msg})

    # Add the current prompt
    messages.append({"role": "user", "content": prompt})

    # Get response from selected provider
    try:
        chat_completion = config.client.chat.completions.create(
            messages=messages,
            model=model,
        )
        response = chat_completion.choices[0].message.content
        return response
    except Exception as e:
        # Handle provider-specific errors
        raise Exception(f"Error with {provider}: {str(e)}")
