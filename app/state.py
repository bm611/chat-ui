import reflex as rx
from app.api import api
from app.db.database import Database
from typing import List, Tuple, Optional


class State(rx.State):
    query: str = ""
    response: str = ""
    is_gen: bool = False

    current_conversation_id: Optional[int] = None
    conversations: List[Tuple[int, str, str]] = []

    # New state variables for provider and model selection
    selected_provider: str = "ollama"  # default provider

    available_providers: List[str] = api.get_available_providers()
    available_models: List[str] = api.get_available_models(
        "ollama"
    )  # default provider models
    selected_model: str = available_models[0]  # default model

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
        self.selected_provider = "ollama"

        self.available_models = api.get_available_models("ollama")
        self.selected_model = self.available_models[0]

        # Create a new conversation with a default title
        self.current_conversation_id = Database.get_instance().create_conversation(
            "New Chat"
        )
        # Refresh the conversations list
        self.conversations = Database.get_instance().get_conversations()
        return rx.redirect("/")

    def on_mount(self):
        """Load conversations when the app starts"""
        self.conversations = Database.get_instance().get_conversations()

    def create_new_conversation(self):
        """Create a new conversation"""
        title = self.query[:30] + "..." if len(self.query) > 30 else self.query
        self.current_conversation_id = Database.get_instance().create_conversation(
            title
        )
        self.conversations = Database.get_instance().get_conversations()

    def load_conversation(self, conversation_id: int):
        """Load a specific conversation"""
        self.current_conversation_id = conversation_id
        messages = Database.get_instance().get_conversation_messages(conversation_id)

        # Reset chat history
        self.chat_history = []

        # Group messages into user-assistant pairs
        for i in range(0, len(messages), 2):
            if i + 1 < len(
                messages
            ):  # Make sure we have both user and assistant messages
                user_message = messages[i]
                assistant_message = messages[i + 1]
                if user_message[0] == "user" and assistant_message[0] == "assistant":
                    self.chat_history.append((user_message[1], assistant_message[1]))

        return rx.redirect("/chat")

    def delete_conversation(self, conversation_id: int):
        db = Database.get_instance()
        db.delete_conversation(conversation_id)
        self.conversations = db.get_conversations()  # Refresh the list

        # If the deleted conversation was the current one, reset the state
        if conversation_id == self.current_conversation_id:
            self.current_conversation_id = None
            self.chat_history = []
            return rx.redirect("/")

    def gen_response(self):
        if not self.current_conversation_id:
            self.create_new_conversation()

        res = api.get_chat_response(
            prompt=self.query,
            provider=self.selected_provider,
            model=self.selected_model,
            chat_history=self.chat_history,
        )

        if res:
            self.response = res
            db = Database.get_instance()

            # Update conversation title if this is the first message
            if len(self.chat_history) == 0:
                title = self.query[:30] + "..." if len(self.query) > 30 else self.query
                db.update_conversation_title(self.current_conversation_id, title)
                self.conversations = (
                    db.get_conversations()
                )  # Refresh conversations list

            # Save messages to database
            db.add_message(self.current_conversation_id, "user", self.query)
            db.add_message(self.current_conversation_id, "assistant", self.response)

        self.is_gen = False
        self.chat_history.append((self.query, self.response))
        self.query = ""
        return rx.redirect("/chat")
