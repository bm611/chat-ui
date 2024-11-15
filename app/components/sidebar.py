import reflex as rx
from app.state import State

def sidebar():
    return rx.cond(
        State.sidebar_visible,
        rx.box(
            rx.vstack(
                rx.heading("Conversations", class_name="mb-4"),
                rx.divider(),
                rx.vstack(
                    rx.foreach(
                        State.conversations,
                        lambda conv: rx.hstack(
                            rx.box(
                                rx.button(
                                    rx.text(
                                        conv[1],
                                        class_name="truncate block",
                                        width="100%",
                                    ),
                                    on_click=lambda: State.load_conversation(conv[0]),
                                    class_name="text-left w-full p-2 bg-white hover:bg-gray-100 rounded text-lg",
                                    color="black",
                                ),
                                flex="1",
                                min_width="0",  # This allows the box to shrink below its content size
                                overflow="hidden",  # Ensures content doesn't overflow
                            ),
                            rx.button(
                                rx.icon("trash-2"),
                                on_click=lambda: State.delete_conversation(conv[0]),
                                class_name="p-2 text-red-500 hover:bg-red-100 rounded flex-shrink-0",
                                variant="ghost",
                            ),
                            width="100%",
                            overflow="hidden",
                        ),
                    ),
                    class_name="w-full",
                    spacing="4",
                    overflow_y="auto",
                    overflow_x="hidden",
                ),
                class_name="h-full w-full p-4",
                overflow="hidden",
            ),
            class_name="w-72 md:w-80 h-screen bg-white border-r border-gray-200 fixed left-0 top-0 pt-20 z-40 transition-all duration-300 ease-in-out transform translate-x-0",
            overflow="hidden",
        ),
        rx.box(),  # Empty box when sidebar is hidden
    )
