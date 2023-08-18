"""
Used as a base class for SimpleLoggingConfig to ensure only one instance can be created
"""


class Singleton(type):
    """Ensure only one instance of a derived class can exist."""
    def __init__(cls, name, bases, dct):
        super().__init__(name, bases, dct)
        cls.instance = None

    def __call__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.instance
