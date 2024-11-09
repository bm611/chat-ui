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
            # This pushes the title to the center
            rx.text(
                "chat/ui",
                class_name="text-6xl font-extralight",
            ),
            rx.color_mode.button(),
            class_name="w-full flex justify-between items-center px-4 mt-4",
        ),
    )
