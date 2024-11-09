import reflex as rx
from app.state import State
from typing import List, Tuple


def chat_message(message_pair: Tuple[str, str]) -> rx.Component:
    return rx.vstack(
        rx.box(
            rx.text(
                message_pair[0],
                class_name="p-3 text-lg",
            ),
            class_name="bg-slate-500 px-6 text-white rounded-bl-full rounded-tl-full rounded-br-full self-end max-w-[80%] mb-4",
        ),
        rx.markdown(
            message_pair[1],
            class_name="self-start max-w-[80%] text-left mb-4 text-lg",
        ),
        width="100%",
    )


def chat_section():
    return rx.box(
        rx.vstack(
            # Chat messages
            rx.box(
                rx.vstack(
                    rx.foreach(State.chat_history, chat_message),
                    spacing="4",
                    align_items="stretch",
                    class_name="w-full mx-auto py-8",
                    size=4,
                ),
                class_name="px-40 mb-24",  # Added margin bottom to prevent overlap with input
                overflow_y="auto",
                flex="1",
            ),
            # Input box fixed at bottom
            rx.box(
                rx.hstack(
                    rx.input(
                        placeholder="Ask a Follow up...",
                        class_name="w-full h-12 md:h-20 px-8 md:px-10 pr-16 rounded-full text-slate-600 text-xl md:text-2xl bg-transparent",
                        value=State.query,
                        on_change=State.set_query,
                    ),
                    rx.button(
                        rx.icon("send-horizontal"),
                        class_name="rounded-full bg-gray-600 hover:bg-black absolute right-8 top-1/2 transform -translate-y-1/2",
                        size="4",
                        type="submit",
                        on_click=State.gen_response,
                        loading=State.is_gen,
                        disabled=State.is_gen,
                    ),
                    class_name="w-full max-w-[1000px] relative flex items-center",
                ),
                class_name="fixed bottom-0 left-1/2 -translate-x-1/2 bg-white p-4 border-t border-gray-200 w-full flex justify-center items-center",
            ),
            height="100vh",
            width="100%",
        ),
    )
