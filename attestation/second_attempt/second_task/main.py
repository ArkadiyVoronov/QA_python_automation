"""Task #2 for attestation."""
import itertools
from typing import Any


class TooMuchParametersException(Exception):
    """Create my exception."""
    def __init__(self: Any, message: str) -> None:
        super().__init__(message)


if __name__ == '__main__':
    print(calculate(a))
