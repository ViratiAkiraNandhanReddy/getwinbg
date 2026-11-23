"""Public API for getwinbg."""

import warnings

from getwinbg.background import _BackgroundManager


def get_background() -> str:
    """Return the current Windows desktop background path.

    ### Deprecated
    This function is deprecated and will be removed in **0.2.0** release.

    Use the `Background` class instead.

    ```python
    # old way
    path = get_background()

    # new way
    background = Background()
    path = background.path
    ```
    """

    warnings.warn(
        "get_background() is deprecated and will be removed in 0.2.0. "
        "Use Background().path instead.",
        DeprecationWarning,
        stacklevel=2,
    )

    return Background().path


class Background:
    """Retrieve the current Windows desktop background."""

    def __init__(self) -> None:

        self._manager = _BackgroundManager()

    @property
    def path(self) -> str:
        """Return the current desktop background path."""

        return self._manager.get_path()

    def reveal(self) -> None:
        """Ask File Explorer to reveal the background file."""

        self._manager.reveal()

    def open(self) -> None:
        """Open the background file with its default application."""

        self._manager.open()

    def copy(self) -> None:
        """Copy the desktop background path to the Windows clipboard."""

        self._manager.copy()
