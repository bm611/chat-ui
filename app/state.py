import reflex as rx
from app.api import api


class State(rx.State):
    query: str = ""
    response: str = ""
    is_gen: bool = False

    def set_query(self, query: str):
        self.query = query

    def refresh(self):
        self.query = ""
        self.response = ""

    def gen_response(self):
        self.is_gen = True
        res = api.get_chat_response(self.query)
        print(res)
        if res:
            self.response = res
        # self.is_gen = False
