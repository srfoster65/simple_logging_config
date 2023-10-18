"""
Used as a base class for SimpleLoggingConfig to ensure only one instance can be created
"""


class Singleton(type):
    """Ensure only one instance of a derived class can exist."""
    def __init__(cls, name, bases, dct):
        super().__init__(name, bases, dct)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instance

    def clear(cls):
        """Remove singleton reference."""
        cls._instance = None
