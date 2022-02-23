# Написать игру
# python3 -m unittest test_rpg.py
# pytest -s

import random


"""
Изначально у рыцаря не менее 10 жизни и 10 сила удара,
и счетчик монстров у нас на 0
:return:
"""
hero_life = 10
hero_power = 10
monstr_counter = 0


def user_turn() -> int:
    """
    Ход игрока, случайное число от 1 до 3:
    встретили новый меч, яблоко или монстра
    :return:
    """
    turn = int(random.randint(1, 3))
    return turn


def sword() -> int:
    """
    Это даёт меч
    Игрок может взять меч(1) или нет(2)
    :return:
    """
    global hero_power
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
    global hero_life
    hero_life += life_bonus
    print("Вы нашли яблоко."
          "Количество вашего здоровья выросло на:",
          life_bonus,
          " и составляет:",
          hero_life)
    return life_bonus


def game():
    """
    Поприветствуем юзера и расскажем правила игры
    :return:
    """
    print("Привет, игрок!")
    print("Ты рыцарь в фантастической стране.")
    print("Твоя задача - победить 10 чудовищ,")
    print("чтобы спасти королевство от нападения и тем самым выиграть игру.")
    print("Управление происходит с помощью цифр '1' и '2'")
    print("Иди и сражайся!")

    """
    Начинаем игру
    """
    global hero_life
    global hero_power
    global monstr_counter
    # Нам надо победить 10 монстров
    while monstr_counter < 10:
        # 1-яблочко, 2-новый меч, 3-монстр
        next_turn = user_turn()
        if next_turn == 1:
            apple()
        if next_turn == 2:
            sword()
        if next_turn == 3:
            monstr_life = int(random.randint(1, 20))
            monstr_power = int()
            print("Вы встретили огра!"
                  "У него здоровья:", monstr_life,
                  " и сила удара:", monstr_power,
                  " ."
                  "У вас здоровья:", hero_life,
                  " и сила удара:", hero_power,
                  " ."
                  "Нажмите на 1, чтобы атаковать этого гада"
                  "или 2, чтобы убежать от этого гада")
            fight_or_chicken = int(input())
            if fight_or_chicken == 1:
                if hero_power > monstr_life:
                    hero_life -= monstr_power
                    if hero_life <= 0:
                        print("Наступила смерть от ударов монстра!"
                              "Попробуйте еще раз!")
                        return False
                    else:
                        monstr_counter += 1
                        print("Вы победили ", monstr_counter,
                              " гадов."
                              "Ваше здоровье:", hero_life)
                else:
                    print("Наступила смерть от ударов монстра!")
                    return False
            if fight_or_chicken == 2:
                user_turn()
        print("Победа! Мы победили 10 страшных монстров, ура!")


# Главная функция, запустив которую начнется игра
game()
