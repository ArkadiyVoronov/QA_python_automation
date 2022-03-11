# Напишите декоратор, валидирующий входные и выходные данные функции. В
# качестве таких валидаторов выступят другие функции.
# Пример использования и ожидаемого значения

# def time_it(f: Callable) -> Callable:
#     def wrap_fn(*arg, **kw):
#         t1 = time.time()
#         result = f(*arg, **kw)
#         t2 = time.time()
#         print(t2 - t1)
#         return result
#
#     return wrap_fn


"""


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

"""

from typing import Callable, Any

def input_validator_with_params(kwarg_key: str, validator: Callable):
    def decoration(func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:

            if validator(kwargs.get(kwarg_key)):
                result = func(*args, **kwargs)
                return result
            else:
                print(f"что-то не так с параметром {kwarg_key}")
        return wrapper
    return decoration


validate_input_x = lambda a: a != 0
validate_input_y_gt0 = lambda a: a > 0

@input_validator_with_params("y", validate_input_y_gt0)
@input_validator_with_params("x", validate_input_x)
def div_(y, x):
    result = y / x
    return result


print(div_(y=6,x=2))
# 3
div_(y=6,x=0)
# что-то не так с параметром x
div_(y=-6,x=0)
