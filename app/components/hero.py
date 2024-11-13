import reflex as rx
from app.state import State


def hero_section():
    return (
        rx.vstack(
            # Center section with prompt text and input
            rx.vstack(
                rx.text(
                    "What can I help you with?",
                    class_name="text-4xl font-regular drop-shadow-sm text-center mb-2",
                ),
                rx.hstack(
                    rx.box(
                        rx.hstack(
                            rx.icon("calendar", color="blue"),
                            rx.text("Make a plan"),
                            align="center",
                            justify="center",
                        ),
                        class_name="px-4 py-2 rounded-full bg-blue-100 hover:bg-blue-200 text-lg cursor-pointer",
                        background_color=rx.color_mode_cond(
                            light="blue.50", dark="blue.900"
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
                        class_name="px-4 py-2 rounded-full bg-yellow-100 hover:bg-yellow-200 text-lg cursor-pointer",
                        background_color=rx.color_mode_cond(
                            light="yellow.50", dark="yellow.900"
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
                        class_name="px-4 py-2 rounded-full bg-green-100 hover:bg-green-200 text-lg cursor-pointer",
                        background_color=rx.color_mode_cond(
                            light="green.50", dark="green.900"
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
                        class_name="px-4 py-2 rounded-full bg-red-100 hover:bg-red-200 text-lg cursor-pointer",
                        background_color=rx.color_mode_cond(
                            light="red.50", dark="red.900"
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
                        class_name="px-4 py-2 rounded-full bg-purple-100 hover:bg-purple-200 text-lg cursor-pointer",
                        background_color=rx.color_mode_cond(
                            light="purple.50", dark="purple.900"
                        ),
                        on_click=lambda: State.set_query(
                            "Summarize the main points of this academic paper"
                        ),
                    ),
                    spacing="4",
                    padding_y="4",
                ),
                rx.hstack(
                    rx.input(
                        placeholder="Enter your prompt...",
                        class_name="w-full h-12 md:h-20 px-8 md:px-10 rounded-full text-slate-600 text-lg md:text-2xl bg-transparent",
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
                rx.hstack(
                    rx.hstack(
                        rx.text("Select Provider:", class_name="text-xl"),
                        rx.select(
                            State.available_providers,
                            placeholder="Select Provider",
                            value=State.selected_provider,
                            on_change=State.set_provider,
                            class_name="text-lg",
                        ),
                        justify="center",
                        align="center",
                    ),
                    # Model selection dropdown
                    rx.hstack(
                        rx.text("Select Model:", class_name="text-xl"),
                        rx.select(
                            State.available_models,
                            placeholder="Select Model",
                            value=State.selected_model,
                            on_change=State.set_model,
                            class_name="text-lg",
                        ),
                        justify="center",
                        align="center",
                    ),
                    justify="center",
                    align="center",
                    spacing="6",
                ),
                spacing="4",
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
