import reflex as rx
from app.state import State

doto_style = {
    "font_family": "Doto, sans-serif",
}


def nav_section():
    return (
        rx.hstack(
            rx.icon(
                "square-pen",
                on_click=State.refresh,
                class_name="cursor-pointer hover:bg-gray-100 rounded-lg p-2",
                size=40,
            ),
            rx.text(
                "Reflexity",
                class_name="text-6xl font-bold",
                style={"font_family": "SourGummy"},
            ),
            rx.hstack(
                rx.link(
                    rx.icon("github"),
                    href="https://github.com/bm611/chat-ui/",
                    is_external=True,
                ),
            ),
            class_name="w-full flex justify-between items-center px-8 mt-4 fixed top-0 bg-white z-50",
        ),
    )
