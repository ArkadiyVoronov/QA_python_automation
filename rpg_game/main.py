import random

# Изначально у рыцаря не менее 10 жизни и 10 сила удара,
# и счетчик монстров у нас на 0.

hp = 10
attack = 10
monster_counter = 0


def apple() -> int:
    """Обнаружили яблочко.

    При обнаружении яблочка — рыцарь съедает его и
    узнаёт насколько он увеличил количество жизней и чему теперь
    равно его количество жизней. В случае нахождения яблочка игроку
    не даётся выбора действия.
    """
    apple_v = random.randint(1, 5)
    global hp
    hp += apple_v
    print("Ты съел яблочко на ", apple_v, "жизней\nи стало жизней:", hp)


def user_choise() -> int:
    """Выбор юзера."""
    user_choise_v = int(input())
    while user_choise_v != 1 and user_choise_v != 2:
        print("Введите 1 или 2")
        user_choise_v = int(input())
    return user_choise_v


def sword() -> int:
    """Какой меч мы нашли.

    При обнаружении меча, на экран должна быть выведена его сила атаки и игроку даётся (вводимый с клавиатуры)
    выбор 1-взять меч себе выбросив старый, 2-пройти мимо меча. При взятии нового меча сила атаки рыцаря
    принимается равной силе атаки нового подобранного меча.
    """
    global attack
    forse = random.randint(1, 20)
    print("Новый МЕЧ силой:", forse)
    print("Нажми на 1 чтобы взять этот меч\nили 2 чтобы оставить старый меч силой:", attack)
    a = user_choise()
    if a == 1:
        print("Ты взял новый меч")
        attack = forse
    else:
        print("Оставил старый меч")


def monster() -> int:
    """Опишем, что за монстра мы встретили.

    При встрече с чудовищем, у чудовища есть случайное число здоровья и атаки,
    а у игрока - выбор (вводимый с клавиатуры) 1-сражаться, 2-убежать, чтобы набраться сил.
    При встрече с чудовищем нужно показать на экране его жизни и силу удара.
    В случае сражения рыцарь побеждает, если число его атаки превосходит число жизней чудовища.
    При этом чудовище отнимает у рыцаря число жизней, соответствующее его атаке.
    Если чудовище сильнее рыцаря, то есть если сила атаки чудовища превосходит
    количество жизней рыцаря — рыцарь умирает, выводится сообщение «ПОРАЖЕНИЕ!
    игра окончена» и происходит завершение программы.
    """
    monster_hp = random.randint(1, 20)
    monster_attack = random.randint(1, 10)
    print("Встретил монстра, у него жизней:", monster_hp," и сила удара:", monster_attack)
    print("Будет БОЙ или нет решать тебе:")
    print("1 - драка, 2 - бежим")
    b = user_choise()
    if b == 1:
        print("Битва")
        global hp, attack
        while hp > 0 and monster_hp > 0:
            hp -= monster_attack
            monster_hp -= attack
        if hp <= 0:
            return 0
        else:
            return 1
    else:
        return 2


def event_game() -> int:
    """Событие возникающие перед героем."""
    event_t = random.randint(1, 3)
    return event_t


def game() -> None:
    """Поприветствуем юзера и расскажем правила игры."""
    print("Привет, игрок!")
    print("Ты рыцарь в фантастической стране.")
    print("Твоя задача - победить 10 чудовищ,")
    print("чтобы спасти королевство от нападения и тем самым выиграть игру.")
    print("Управление происходит с помощью цифр '1' и '2'")
    print("Иди и сражайся!")
    print("---------------")

    # Начинаем игру
    global monster_counter
    while monster_counter < 10:
        g = event_game()
        # яблоко 1, меч 2, бой 3
        if g == 1:
            apple()
        elif g == 2:
            sword()
        else:
            m = monster()
            if m == 0:
                print("ПОРАЖЕНИЕ!\nигра окончена")
                break
            elif m == 1:
                monster_counter += 1
                print("Победили очередного монстра, всего замочили:", monster_counter, " ")
                print("После битвы осталось жизней:", hp)
            else:
                print("Убежал, зато шкура цела.")
                print("Новый ход, будь готов!")
    else:
        print("ПОБЕДА")


game()
