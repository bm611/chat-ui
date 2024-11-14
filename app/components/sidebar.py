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
                    lambda conv: rx.hstack(
                        rx.button(
                            rx.text(
                                conv[1],
                                class_name="truncate w-48 text-lg",  # Fixed width and truncate text
                            ),
                            on_click=lambda: State.load_conversation(conv[0]),
                            class_name="text-left flex-grow p-2 bg-white hover:bg-gray-100 rounded w-52",  # Fixed width for button
                            color="black",
                        ),
                        rx.button(
                            rx.icon("trash-2"),
                            on_click=lambda: State.delete_conversation(conv[0]),
                            class_name="p-2 text-red-500 hover:bg-red-100 rounded",
                            variant="ghost",
                        ),
                        class_name="w-full",
                    ),
                ),
                class_name="w-full",
                spacing="4",
            ),
            class_name="h-full w-full p-4",
        ),
        class_name="w-72 h-screen bg-white border-r border-gray-200 fixed left-0 top-0 pt-20",
    )
