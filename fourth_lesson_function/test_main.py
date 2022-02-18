import pytest
import os

# Главный (он же единственный),
# файл вашего решения называется main.py
def test_name_is_main():
    assert os.path.isfile('./main.py')
