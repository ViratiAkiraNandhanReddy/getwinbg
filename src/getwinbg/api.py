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

    _manager = _BackgroundManager()

    def __init__(self) -> None:

        # Initialize the background path
        self._path: str = self._manager.get_path()

    @property
    def path(self) -> str:
        """Return the current desktop background path."""

        # Update the path each time it is accessed to ensure it is current
        self._path = self._manager.get_path()

        # Return the current desktop background path
        return self._path
