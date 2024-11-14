import reflex as rx
from app.state import State


def sidebar():
    return rx.box(
        rx.vstack(
            rx.heading("Conversations", class_name="mb-4"),
            rx.divider(),
            rx.vstack(
                rx.foreach(
                    State.conversations,
                    lambda conv: rx.button(
                        conv[1],
                        on_click=lambda: State.load_conversation(conv[0]),
                        class_name="text-left w-full p-2 bg-blue-300 shadow-xl hover:bg-gray-100 rounded",
                        color="black",
                    ),
                ),
                class_name="w-full",
                spacing="2",
            ),
            class_name="h-full w-full p-4",
        ),
        class_name="w-64 h-screen bg-white border-r border-gray-200 fixed left-0 top-0 pt-20",
    )
