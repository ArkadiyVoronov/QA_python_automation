# Тут будет Ваше исполнение ДЗ

def read_file() -> tuple:
    """Подготовим данные в файле."""
    with open("test.txt", "r") as file:
        crater_map = file.readlines()
    crater_map = [[int(n) for n in x.split()] for x in crater_map]
    return crater_map


def calculate(crater_map: list) -> int:
    """Подсчет кратеров."""
    count = 0
    for i in range(len(crater_map)):
        for j in range(len(crater_map[i])):
            if crater_map[i][j] == 1:
                find_crater(crater_map, i, j)
                count += 1
    return count


def find_crater(crater_map: list, x: int, y: int) -> list:
    """Проходим по массиву и ищем единицы."""
    if 0 <= x < len(crater_map) and 0 <= y < len(crater_map[0]):
        if crater_map[x][y] == 1:
            crater_map[x][y] = 0
            find_crater(crater_map, x - 1, y)
            find_crater(crater_map, x + 1, y)
            find_crater(crater_map, x, y - 1)
            find_crater(crater_map, x, y + 1)


result = calculate(read_file())
print(result)
