

# тест для значения 1 успешен
# тест для значения 2 успешен
# тест для значения 3 успешен
# тест для значения 8 успешен
# тест для значения 9 успешен
# AssertionError
from typing import Callable, Any


def my_parametrizer(x: str, list_) -> Callable:
    def decoration(func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for i in list_:

                print(list_)
                kwargs[x] = i
                # assert isinstance(list_, object)

                result = func(**kwargs)
            return result
        return wrapper
    return decoration
    # print("то что происходит ПОСЛЕ вызова функции")

           # return result
 # return wrapper
 # return decoration



@my_parametrizer('x', [1,2,3,8,9,10,11])
def test_x_lt_10(x):
    assert x < 10
    print('тест для значения', x, 'успешен')

test_x_lt_10(x=0)
