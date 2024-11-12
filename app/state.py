import reflex as rx
from app.api import api
from typing import List, Tuple


class State(rx.State):
    query: str = ""
    response: str = ""
    is_gen: bool = False

    # New state variables for provider and model selection
    selected_provider: str = "cerebras"  # default provider
    selected_model: str = "llama3.1-8b"  # default model
    available_providers: List[str] = api.get_available_providers()
    available_models: List[str] = api.get_available_models(
        "cerebras"
    )  # default provider models

    chat_history: List[Tuple[str, str]] = []

    def set_query(self, query: str):
        self.query = query

    def set_provider(self, provider: str):
        """Update provider and available models when provider changes"""
        self.selected_provider = provider
        self.available_models = api.get_available_models(provider)
        # Set default model for the new provider
        self.selected_model = self.available_models[0]

    def set_model(self, model: str):
        """Update selected model"""
        self.selected_model = model

    def handle_generation(self):
        self.is_gen = True

    def refresh(self):
        self.query = ""
        self.response = ""
        self.chat_history = []
        self.is_gen = False
        # Reset provider and model to defaults
        self.selected_provider = "cerebras"
        self.selected_model = "llama3.1-8b"
        self.available_models = api.get_available_models("cerebras")
        return rx.redirect("/")

    def gen_response(self):
        res = api.get_chat_response(
            prompt=self.query,
            provider=self.selected_provider,
            model=self.selected_model,
            chat_history=self.chat_history,
        )
        print(res)
        if res:
            self.response = res
        self.is_gen = False
        self.chat_history.append((self.query, self.response))
        self.query = ""
        return rx.redirect("/chat")
