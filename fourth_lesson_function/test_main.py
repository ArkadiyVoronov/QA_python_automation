import pytest
import os

# Главный (он же единственный),
# файл вашего решения называется main.py
def test_if_name_main():
    assert os.path.isfile('./main.py')

# Главная функция, запустив которую начнется игра -
# это функция с названием game() без параметров


def test_if_name_game():
    pass


class TestClass:


    @pytest.mark.parametrize("arg", ["a"])
    def test_stuff(self, request, arg):
        print("originalname:", request.node.originalname)
        print("name:", request.node.name)
        print("nodeid:", request.node.nodeid)