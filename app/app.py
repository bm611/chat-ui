import reflex as rx
from .components import hero


@rx.page(route="/", title="Chat")
def index() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            hero.hero_section(),
            justify="center",
            align="center",
            min_height="40vh",
        ),
        size="4",
    )


style = {
    "font_family": "Lexend",
}


app = rx.App(
    style=style,
    stylesheets=["/fonts/font.css"],
)
