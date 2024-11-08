import reflex as rx
from .components import hero
from .components import nav


@rx.page(route="/", title="Chat")
def index() -> rx.Component:
    return rx.box(
        nav.nav_section(),
        hero.hero_section(),
        class_name="w-full mt-2",
    )


style = {
    "font_family": "Lexend",
}


app = rx.App(
    style=style,
    stylesheets=["/fonts/font.css"],
)
