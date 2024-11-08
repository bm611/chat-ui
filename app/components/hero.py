import reflex as rx
from app.state import State


def hero_section():
    return (
        rx.vstack(
            rx.text(
                "SwiftFlare",
                class_name="text-6xl font-regular tracking-tight bg-gradient-to-r from-pink-500 to-orange-500 bg-clip-text text-transparent drop-shadow-lg mx-10",
            ),
            rx.text(
                "Let's find answers",
                class_name="text-3xl font-regular text-slate-500 drop-shadow-sm mx-10",
            ),
            rx.hstack(
                rx.input(
                    placeholder="Enter your prompt...",
                    class_name="w-full h-20 md:h-24 px-4 md:px-8 pr-8 md:pr-16 rounded-full text-slate-600 text-xl md:text-2xl bg-transparent",
                    value=State.query,
                    on_change=State.set_query,
                ),
                rx.button(
                    rx.icon("send-horizontal"),
                    class_name="rounded-full bg-gray-600 hover:bg-black absolute right-8 top-1/2 transform -translate-y-1/2",
                    size="4",
                    type="submit",
                    on_click=State.gen_response,
                ),
                class_name="w-full max-w-[800px] relative flex items-center px-4",
            ),
            rx.button(
                rx.text("Clear chat"),
                class_name="rounded-full bg-gradient-to-r from-red-500 to-red-700 text-white px-4 py-2 hover:from-red-600 hover:to-red-800 mx-10",
                on_click=State.refresh,
                size="4",
            ),
            rx.box(
                rx.cond(
                    State.is_gen,
                    rx.markdown(State.response, class_name="mx-10 max-w-3xl text-xl"),
                    rx.text(),
                ),
            ),
            width="100%",
            class_name="flex items-left",
        ),
    )
