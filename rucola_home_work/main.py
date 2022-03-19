import requests
from rucola import blossom
from typing import Callable, Any


@blossom(max_retries=3) # Сохраняет все отловленные исключения, прогоняя функцию до трёх раз
def get_page_content(url):
    resp = requests.get(url)
    return resp.content

content_with_retry = get_page_content("http://very_fake_address.com")
print(content_with_retry)

content_with_no_retry = get_page_content("https://httpbin.org/get")
print(content_with_retry)