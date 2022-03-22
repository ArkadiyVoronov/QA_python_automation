from typing import Any, Callable
from functools import wraps
import json
import requests


class ConfigurationError(Exception):
    """Исключение для параметра.

    Если значение параметра - не целое число
    или целое число но меньшее 1 - выбросить ConfigurationError
    """
    def __init__(self, message: str) -> None:
        """Наследуем исключение."""
        super().__init__(message)
        self.message = message

    def __str__(self) -> Any:
        """Исправляю, что ругается flake8."""
        return "Проверка передаваемого параметра"


def blossom(max_retries: int = 1) -> Callable:
    """
    Значение по умолчанию.

    Декоратор повторяет указанную функцию до max_retries раз,
    пока не завершится без исключений.
    """
    if max_retries < 1 or not isinstance(max_retries, int):
        raise ConfigurationError("Число не целое или меньше 1")

    def decorate(fn: Callable) -> Callable:
        @wraps(fn)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            err = None
            result = dict()
            run = list()
            for _ in range(max_retries):
                try:
                    y = fn(*args, **kwargs)
                    run.append({"exception": None, "return": str(y)})
                    result = {fn.__name__: {'is_success': True, "run": run}}
                    break
                except requests.ConnectionError as exc:
                    err = type(exc).__name__
                    run.append({"exception": err, "return": None})
                    result = {fn.__name__: {'is_success': False, "run": run}}
            return json.dumps(result, indent=4)

        return wrapper

    return decorate


@blossom(3)
def get_page_content(url: str) -> Any:
    """Основная функция, отправляет запросы на сервер."""
    resp = requests.get(url)
    return resp.content


content_with_retry = get_page_content("https://httpbin.org/get")
print(content_with_retry)
