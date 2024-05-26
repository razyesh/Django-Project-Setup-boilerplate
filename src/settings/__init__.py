try:
    from src.settings.env import * # noqa
except ImportError:
    raise Exception(
        "Please create env.py file in core/settings/ directory."
    )
