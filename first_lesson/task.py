# «Найди Вальдо». Дан случайный словарь, в котором,
# на одном из уровней вложенности есть ключ «Waldo».
# Написать функцию, которая бы принимала случайный
# словарь и возвращала бы другой словарь, в котором был бы только один ключ «Waldo» и
# значение этого  ключа из оригинального словаря.

simple = {
    "_id": "5eca0224bbf81beccba525d5",
    "index": 0,
    "guid": "7c53ffb4-5152-4e58-bfd7-49c7b00a92d2",
    "isActive": False,
    "balance": "$1,905.45",
    "picture": "http://placehold.it/32x32",
    "age": 23,
    "eyeColor": "blue",
    "name": "Mendez Love",
    "gender": "male",
    "company": "NIQUENT",
    "email": "mendezlove@niquent.com",
    "phone": "+1 (803) 421-3635",
    "address": "883 Garnet Street, Roy, Federated States Of Micronesia, 288",
    "about": "Magna do sunt id mollit non nulla est. Dolor ea occaecat minim veniam sit in Lorem excepteur et sint minim ea esse. Consequat incididunt tempor labore proident exercitation dolor quis Lorem. Veniam ipsum pariatur pariatur id officia.\r\n",
    "registered": "2015-07-21T07:09:56 -03:00",
    "latitude": -85.74001,
    "longitude": -36.020207,
    "tags": [
      "ipsum",
      "pariatur",
      "officia",
      "incididunt",
      "labore",
      "exercitation",
      "occaecat"
    ],
    "friends": [
      {
        "id": 0,
        "name": "Gardner Quinn"
      },
      {
        "id": 1,
        "name": "Antonia Mercer",
        "waldo": "Я здесь!",
      },
      {
        "id": 2,
        "name": "Allie Sharp"
      }
    ],
    "greeting": "Hello, Mendez Love! You have 6 unread messages.",
    "favoriteFruit": "banana"
  }


def waldo(simple):
    for key, value in simple.items():
        # key, value
        if key == "waldo":
            print({"waldo": value})
        if isinstance(value, dict):
            waldo(value)
        if isinstance(value, list):
            for x in value:
                if isinstance(x, dict):
                    waldo(x)
    # if "waldo" in simple:
    #     return simple.get("waldo")


print(waldo(simple))
