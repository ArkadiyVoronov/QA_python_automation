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

def sword() -> int:
    """
    Это даёт меч
    Игрок может взять меч(1) или нет(2)
    :return:
    """
    sw = int(random.randint(1, 10))
    print("Перед тобой меч силой атаки:",
          sw,
          "Сейчас у вас меч силой атаки:",
          hero_power,
          "Нажмите 1 - взять новый меч "
          "или 2 оставить прежний меч")
    take_new_sword = int(input())
    if take_new_sword == 1:
        hero_power = sw
        print("Вы взяли новый меч и ваша сила атаки:", hero_power,)
        return hero_power
    elif take_new_sword == 2:
        print("Старый конь, борозды не портит,"
              "ваша сила атаки:", hero_power)
        return hero_power
    else:
        print("Управление через 1 и 2!")
        take_new_sword = int(input())
        return take_new_sword


def apple() -> int:
    """
    Это даёт яблоко,
    случайный бонус к здоровью
    :return:
    """
    life_bonus = int(random.randint(1, 5))
    hero_life_on_start()
    hero_life += life_bonus
    print("Вы нашли яблоко."
          "Количество вашего здоровья выросло на:",
          life_bonus,
          " и составляет:",
          hero_life)
    return life_bonus


def hero_life_on_start():
    """
    Изначально у рыцаря не менее 10 жизни и 10 сила удара,
    и счетчик монстров у нас на 0
    :return:
    """
    hero_life = 10
    hero_power = 10
    monstr_counter = 0



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