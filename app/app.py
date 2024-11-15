import reflex as rx
from .components import hero
from .components import nav
from .components import chat
from app.state import State
from typing import List, Tuple
from app.db.database import Database

# Initialize database singleton
Database.get_instance()


@rx.page(route="/", title="Chat")
def index() -> rx.Component:
    return rx.box(
        nav.nav_section(),
        hero.hero_section(),
        on_mount=State.on_mount,
        class_name="w-full mt-4",
    )


@rx.page(route="/chat", title="Response")
def chat_page() -> rx.Component:
    return rx.box(
        nav.nav_section(),
        chat.chat_section(),
        on_mount=State.on_mount,
    )


style = {
    "font_family": "Argon",
}


app = rx.App(
    style=style,
    stylesheets=["/fonts/font.css"],
    theme=rx.theme(
        appearance="light",
    ),
)
