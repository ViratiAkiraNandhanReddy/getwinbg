"""Public API for getwinbg."""

from getwinbg.system.background import Background


def get_background() -> str:
    """Return the current Windows desktop background path."""

    return Background().get_path()
