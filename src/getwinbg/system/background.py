"""Windows desktop background retrieval."""

import ctypes
from pathlib import Path
from typing import Final

_SPI_GET_DESKTOP_WALLPAPER: Final[int] = 0x0073
_BUFFER_SIZE: Final[int] = 512


class Background:
    """Retrieve the current Windows desktop background."""

    def _fetch_path(self) -> str:
        """Retrieve the raw background path from Windows."""

        buffer = ctypes.create_unicode_buffer(_BUFFER_SIZE)

        success = ctypes.windll.user32.SystemParametersInfoW(
            _SPI_GET_DESKTOP_WALLPAPER,
            len(buffer),
            buffer,
            0,
        )

        if not success:
            raise Exception("Failed to retrieve the current desktop background.")

        path = buffer.value

        if not path:
            raise Exception("No desktop background is currently set.")

        return path

    @staticmethod
    def _normalize_path(path: str) -> str:
        """Normalize a background path."""

        path = path.strip()

        if not path:
            return ""

        return str(Path(path).expanduser())

    @staticmethod
    def _validate_path(path: str) -> bool:
        """Validate that a background path exists and is a file."""

        if not path:
            return False

        background_path = Path(path)

        return background_path.exists() and background_path.is_file()
