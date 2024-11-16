import os
import json
import openai
from typing import List, Tuple, Dict
from enum import Enum
from pathlib import Path


def _load_provider_names() -> List[str]:
    config_path = Path(__file__).parent.parent.parent / "config.json"
    with open(config_path) as f:
        config_data = json.load(f)
    return list(config_data["providers"].keys())


class ModelProvider(str, Enum):
    def __new__(cls):
        providers = _load_provider_names()
        values = {provider.upper(): provider for provider in providers}
        return str.__new__(cls)

    @classmethod
    def _missing_(cls, value):
        # Handle case-insensitive lookup
        for member in cls._member_map_.values():
            if member.lower() == value.lower():
                return member
        return None

    def __str__(self):
        return self.value

ModelProvider = Enum('ModelProvider', {provider.upper(): provider for provider in _load_provider_names()})


class ModelConfig:
    def __init__(self, base_url: str, api_key: str, available_models: List[str]):
        self.base_url = base_url
        self.api_key = api_key if api_key == "ollama" else os.environ.get(api_key, "")
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


def load_provider_configs() -> Dict[ModelProvider, ModelConfig]:
    config_path = Path(__file__).parent.parent.parent / "config.json"
    with open(config_path) as f:
        config_data = json.load(f)

    configs = {}
    for provider_name, provider_config in config_data["providers"].items():
        provider_enum = ModelProvider(provider_name)
        configs[provider_enum] = ModelConfig(
            base_url=provider_config["base_url"],
            api_key=provider_config["api_key"],
            available_models=provider_config["available_models"],
        )
    return configs


# Configuration for different providers
PROVIDER_CONFIGS: Dict[ModelProvider, ModelConfig] = load_provider_configs()


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
