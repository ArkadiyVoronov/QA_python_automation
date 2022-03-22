import unittest
from blossom import get_page_content


class TestNegative(unittest.TestCase):
    """Попробуем плохой адрес."""

    def test_with_bad_address(self) -> None:
        """Исправляю flake8."""
        expected = '{\n    "get_page_content": {\n        "is_success": false'
        actual = get_page_content("http://very_fake_address.com")
        self.assertIn(expected, actual)


class TestPositive(unittest.TestCase):
    """Попробуем хороший адрес."""

    def test_with_good_address(self) -> None:
        """Исправляю flake8."""
        expected = '{\n    "get_page_content": {\n        "is_success": true'
        actual = get_page_content("https://httpbin.org/get")
        self.assertIn(expected, actual)
        return None


if __name__ == '__main__':
    unittest.main()
