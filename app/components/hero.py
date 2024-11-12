import reflex as rx
from app.state import State


def hero_section():
    return (
        rx.vstack(
            # Center section with prompt text and input
            rx.vstack(
                rx.text(
                    "What can I help you with?",
                    class_name="text-4xl font-regular drop-shadow-sm text-center",
                ),
                rx.hstack(
                    rx.input(
                        placeholder="Enter your prompt...",
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
                rx.hstack(
                    rx.box(
                        rx.hstack(
                            rx.icon("calendar", color="blue"),
                            rx.text("Make a plan"),
                            align="center",
                            justify="center",
                        ),
                        class_name="px-4 py-2 rounded-full bg-gray-100 hover:bg-gray-300 text-lg cursor-pointer",
                        background_color=rx.color_mode_cond(
                            light="gray.100", dark="gray"
                        ),
                        on_click=lambda: State.set_query(
                            "Help me create a detailed study plan for the next month"
                        ),
                    ),
                    rx.box(
                        rx.hstack(
                            rx.icon("lightbulb", color="gold"),
                            rx.text("Brainstorm"),
                            align="center",
                            justify="center",
                        ),
                        class_name="px-4 py-2 rounded-full bg-gray-100 hover:bg-gray-300 text-lg cursor-pointer",
                        background_color=rx.color_mode_cond(
                            light="gray.100", dark="gray"
                        ),
                        on_click=lambda: State.set_query(
                            "Let's brainstorm creative marketing ideas for a new coffee shop"
                        ),
                    ),
                    rx.box(
                        rx.hstack(
                            rx.icon("circle-help", color="green"),
                            rx.text("Get Advice"),
                            align="center",
                            justify="center",
                        ),
                        class_name="px-4 py-2 rounded-full bg-gray-100 hover:bg-gray-300 text-lg cursor-pointer",
                        background_color=rx.color_mode_cond(
                            light="gray.100", dark="gray"
                        ),
                        on_click=lambda: State.set_query(
                            "What should I consider when buying my first home?"
                        ),
                    ),
                    rx.box(
                        rx.hstack(
                            rx.icon("pencil", color="red"),
                            rx.text("Help Me Write"),
                            align="center",
                            justify="center",
                        ),
                        class_name="px-4 py-2 rounded-full bg-gray-100 hover:bg-gray-300 text-lg cursor-pointer",
                        background_color=rx.color_mode_cond(
                            light="gray.100", dark="gray"
                        ),
                        on_click=lambda: State.set_query(
                            "Help me write a professional email to request a meeting with my manager"
                        ),
                    ),
                    rx.box(
                        rx.hstack(
                            rx.icon("file-text", color="purple"),
                            rx.text("Summarize Text"),
                            align="center",
                            justify="center",
                        ),
                        class_name="px-4 py-2 rounded-full bg-gray-100 hover:bg-gray-300 text-lg cursor-pointer",
                        background_color=rx.color_mode_cond(
                            light="gray.100", dark="gray"
                        ),
                        on_click=lambda: State.set_query(
                            "Summarize the main points of this academic paper"
                        ),
                    ),
                    spacing="4",
                    padding_y="4",
                ),
                spacing="6",
                padding_top="20em",
                width="100%",
                align="center",  # Centers the content horizontally
            ),
            # Response section
            # rx.box(
            #     rx.cond(
            #         State.is_gen,
            #         rx.markdown(State.response, class_name="max-w-3xl text-xl"),
            #         rx.text(),
            #     ),
            #     class_name="mx-10",
            # ),
            width="100%",
            height="100vh",
            spacing="4",
        ),
    )
