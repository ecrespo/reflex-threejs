"""Shared state for the demo's interactive examples."""

from __future__ import annotations

import reflex as rx


class DemoState(rx.State):
    """Interactivity for the demo scenes."""

    # Cycle of pleasant colors for the "click to recolor" example.
    _palette: list[str] = [
        "#6366f1",  # indigo
        "#ec4899",  # pink
        "#22c55e",  # green
        "#f59e0b",  # amber
        "#06b6d4",  # cyan
        "#ef4444",  # red
    ]
    color_index: int = 0
    hovered: bool = False

    @rx.var
    def active_color(self) -> str:
        """The currently selected color."""
        return self._palette[self.color_index % len(self._palette)]

    @rx.event
    def next_color(self):
        """Advance to the next color in the palette."""
        self.color_index += 1

    @rx.event
    def set_hovered(self, value: bool):
        """Track pointer hover for the interactive mesh."""
        self.hovered = value

    # Toggles for the staging example.
    auto_rotate: bool = True
    wireframe: bool = False

    @rx.event
    def toggle_auto_rotate(self):
        """Toggle auto-rotation of the staging scene."""
        self.auto_rotate = not self.auto_rotate

    @rx.event
    def toggle_wireframe(self):
        """Toggle wireframe rendering in the staging scene."""
        self.wireframe = not self.wireframe
