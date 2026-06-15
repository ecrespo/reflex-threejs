"""Reflex configuration for the reflex-threejs demo app."""

import reflex as rx

config = rx.Config(
    app_name="reflex_threejs_demo",
    # The custom component lives in ../custom_components and is installed via
    # `pip install -e ..` (see requirements.txt).
)
