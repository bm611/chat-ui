import reflex as rx
from app.state import State


def nav_section():
    return (
        rx.hstack(
            rx.hstack(
                rx.cond(
                    State.sidebar_visible,
                    rx.icon(
                        "chevron-left",
                        on_click=State.toggle_sidebar,
                        class_name="cursor-pointer hover:bg-gray-100 rounded-lg p-2",
                        size=40,
                    ),
                    rx.icon(
                        "chevron-right",
                        on_click=State.toggle_sidebar,
                        class_name="cursor-pointer hover:bg-gray-100 rounded-lg p-2",
                        size=40,
                    ),
                ),
                rx.icon(
                    "square-pen",
                    on_click=State.refresh,
                    class_name="cursor-pointer hover:bg-gray-100 rounded-lg p-2",
                    size=40,
                ),
                spacing="1",
            ),
            rx.text(
                "Reflexity",
                class_name="text-3xl md:text-5xl font-bold",
            ),
            rx.hstack(
                rx.link(
                    rx.icon("github", size=32),
                    href="https://github.com/bm611/chat-ui/",
                    is_external=True,
                ),
            ),
            class_name="w-full flex justify-between items-center px-4 md:px-8 mt-4 fixed top-0 bg-white z-50 h-16 md:h-20",
        ),
    )
