import reflex as rx
from app.state import State
from typing import List, Tuple
from .sidebar import sidebar

component_map = {
    # "h1": lambda text: rx.heading(text, size="5", margin_y="1em"),
    # "h2": lambda text: rx.heading(text, size="3", margin_y="1em"),
    # "h3": lambda text: rx.heading(text, size="2", margin_y="1em"),
    # "p": lambda text: rx.text(text, margin_y="1em", font_family="Inter"),
    # "code": lambda text: rx.code(text, color="purple"),
    "codeblock": lambda text, **props: rx.code_block(
        text,
        **props,
        theme=rx.code_block.themes.atom_dark,
        margin_y="1em",
        border_radius="16px",
        font_family="Inter",
    ),
    "a": lambda text, **props: rx.link(
        text, **props, color="blue", _hover={"color": "black"}, font_family="Inter"
    ),
}


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
            component_map=component_map,
            class_name="self-start max-w-[80%] text-left mb-4 text-lg",
        ),
        width="100%",
    )


def chat_section():
    return rx.hstack(
        sidebar(),  # Add the sidebar
        rx.box(
            rx.vstack(
                # Chat messages
                rx.box(
                    rx.vstack(
                        rx.foreach(State.chat_history, chat_message),
                        spacing="4",
                        align_items="stretch",
                        class_name="w-full max-w-[1000px] mx-auto py-8",
                        size=4,
                    ),
                    class_name="px-40 mt-24 mb-24 w-full",  # Added margin bottom to prevent overlap with input
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
                            on_click=[State.handle_generation, State.gen_response],
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
            class_name="ml-64 w-full",  # Add margin to accommodate sidebar
        ),
        width="100%",
        height="100vh",
    )
