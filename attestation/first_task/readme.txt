Задание
Вместе с командой вы трудитесь над созданием игры "первая галактика", суть которой - путешествовать по различным планетам на космолёте и выполнять задания. Вам досталась задача по генерации таких планет.

У каждой планеты есть параметры атмосферы, населённости, температура, размер. Ваша задача - сгенерировать все возможные варианты планет из представленных опций таких параметров. Известно что сам список параметров планеты и количество опций у параметров скорее всего будет меняться в ходе разработки игры.

Напишите программу, которая принимает набор таких опций для планет в виде json-объекта в таком виде:

 {
    "атмосфера" : ["кислородосодержащая", "отсутствует"],
    "населённость" : ["растения"],
    "размер" : ["средний"],
    "температура" : ["средняя"]
 }
Результатом работы программы будет список всех возможных сочетаний параметров для планеты в таком виде:

[
    {
        "атмосфера": "кислородосодержащая",
        "населённость": "растения",
        "размер": "средний",
        "температура": "средняя"
    },
    {
        "атмосфера": "отсутствует",
        "населённость": "растения",
        "размер": "средний",
        "температура": "средняя"
    }
]
Если всевозможных вариантов на выходе окажется сильно много, более 100, программа должна оповестить об этом,выдав исключение TooMuchParametersException.

В программе должна быть функция calculate, которая принимает исходный набор параметров и возвращает список возможных комбинаций таких параметров для планет.