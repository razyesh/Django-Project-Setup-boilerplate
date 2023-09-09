try:
    from src.settings.env import *
except ImportError:
    raise Exception(
        "Please create env.py file in core/settings/ directory."
    )
