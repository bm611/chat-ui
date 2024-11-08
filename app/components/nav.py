import reflex as rx
from app.state import State


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
                "SwiftFlare",
                class_name="text-6xl font-regular tracking-tight bg-gradient-to-r from-pink-500 to-orange-500 bg-clip-text text-transparent drop-shadow-lg",
            ),
            rx.color_mode.button(),
            class_name="w-full flex justify-between items-center px-4",
        ),
    )
