"""
Used as a base class for SimpleLoggingConfig to ensure only one instance can be created
"""

from typing import Any


class Singleton(type):
    """Ensure only one instance of a derived class can exist."""

    def __init__(cls, name: str, bases: tuple[Any], dct: dict[str, Any]) -> None:
        super().__init__(name, bases, dct)
        cls._instance = None

    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instance

    def clear(cls) -> None:
        """Remove singleton reference."""
        cls._instance = None
