"""Windows desktop background retrieval."""

import ctypes
import os
import subprocess
from pathlib import Path
from typing import Final

_SPI_GET_DESKTOP_WALLPAPER: Final[int] = 0x0073
_BUFFER_SIZE: Final[int] = 512


class _BackgroundManager:
    """Retrieve the current Windows desktop background."""

    def get_path(self) -> str:
        """Return the current desktop background path."""

        path = self._normalize_path(self._fetch_path())

        if not self._validate_path(path):
            raise Exception(f"Invalid background path: {path}")

        return path

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

        path: str = buffer.value  # type: ignore

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

    def reveal(self) -> None:
        """Ask File Explorer to reveal the background file."""

        path = self.get_path()

        try:
            subprocess.run(["explorer", "/select,", path], check=False)
        except Exception as error:
            raise Exception(
                "Failed to reveal the current desktop background in File Explorer."
            ) from error

    def open(self) -> None:
        """Open the background file with its default application."""

        path = self.get_path()

        try:
            os.startfile(path)
        except Exception as error:
            raise Exception(f"Could not open the desktop background: {path}") from error
