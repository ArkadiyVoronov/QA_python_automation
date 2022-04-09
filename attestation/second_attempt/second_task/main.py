"""Task #2 for attestation."""
import itertools
from typing import Any


class TooMuchParametersException(Exception):
    """Create my exception."""

    def __init__(self: Any, message: str) -> None:
        """Наследуем из исключения."""
        super().__init__(message)


def calculate(dictionary: dict):
    """Calculate all combinations."""
    atmospheric_list = []
    total = []
    for key in dictionary:
        key_values = dictionary.get(key)
        for item in key_values:
            atmospheric_parameters = {key: item}
            atmospheric_list.append(atmospheric_parameters)
        total.append(atmospheric_list)
        atmospheric_list = []

    result = list(itertools.product(*total))
    new_dict = {}
    new_result = []
    for item in result:
        for x in item:
            new_dict.update(x)
        new_result.append(new_dict)
        new_dict = {}

    if len(new_result) > 100:
        raise TooMuchParametersException("Too much parameters")
    else:
        return new_result


if __name__ == '__main__':
    first_test = {
        "атмосфера": ["кислородосодержащая"],
        "населённость": ["растения"],
        "размер": ["средний"],
        "температура": ["средняя"]
    }

    second_test = {
        "атмосфера": ["кислородосодержащая", "отсутствует"],
        "размер": ["карлик", "великан"],
        "температура": ["низкая", "средняя", "высокая"],
        "посещалась ранее": ["да", "нет"]
    }

    bad_test = {
        "атмосфера": ["кислородосодержащая", "отсутствует"],
        "размер": ["карлик", "средний", "великан"],
        "населённость": ["растения", "существа", "разумные существа", "нет"],
        "температура": ["низкая", "средняя", "высокая"],
        "посещалась ранее": ["да", "нет"]
    }

    print(calculate(first_test))
    print(calculate(second_test))
    print(calculate(bad_test))
