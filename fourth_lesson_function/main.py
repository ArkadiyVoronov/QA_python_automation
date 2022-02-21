# Написать игру
# python3 -m unittest test_rpg.py
# pytest -s
import random

def userChoise():
    """
    Ввод юзера, управление на 1 и 2
    :return:
    """
    i = int(input())
    while( i != 1 or i != 2 ):
        print("Только 1 или 2 нужно нажимать")
        i = int(input())
    return 1

def sword():
    """
    Это даёт меч
    :return:
    """
    sw = random.randint(1,10)
    print("Перед тобой меч силой в {sw}")

def apple():
    """
    Это даёт яблоко
    :return:
    """
    print("Яблоко")

def hero_life_on_start():
    """
    Изначально у рыцаря не менее 10 жизни и 10 сила удара
    :return:
    """
    hero_life = 10
    hero_power = 10



def game():
    """
    Поприветствуем юзера и расскажем правила игры
    :return:
    """
    print("Привет, игрок!")
    print("Вы рыцарь в фантастической стране.")
    print("Ваша задача - победить 10 чудовищ,")
    print("чтобы спасти королевство от нападения и тем самым выиграть игру.")
    print("Управление происходит с помощью цифр '1' и '2'")
    print("Иди и сражайся!")

# Главная функция, запустив которую начнется игра
game()