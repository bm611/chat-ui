import reflex as rx
from app.api import api
from typing import List, Tuple


class State(rx.State):
    query: str = ""
    response: str = ""
    is_gen: bool = False

    chat_history: List[Tuple[str, str]] = []

    def set_query(self, query: str):
        self.query = query

    def refresh(self):
        self.query = ""
        self.response = ""
        self.chat_history = []
        return rx.redirect("/")

    def gen_response(self):
        self.is_gen = True
        res = api.get_chat_response(
            self.query, "cerebras", "llama3.1-8b", self.chat_history
        )
        if res:
            self.response = res
        self.is_gen = False
        self.chat_history.append((self.query, self.response))
        self.query = ""
        return rx.redirect("/chat")
