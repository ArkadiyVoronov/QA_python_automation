import itertools


available_ingredients = [
    {
    "атмосфера" : ["кислородосодержащая", "отсутствует"],
    "населённость" : ["растения"],
    "размер" : ["средний"],
    "температура" : ["средняя"]
    }
]


print(list(itertools.product(available_ingredients, repeat=1)))


def product(*args, repeat=1):
    pools = [tuple(pool) for pool in args] * repeat
    result = [[]]
    for pool in pools:
        result = [x + [y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)

prod = []
result = []


print(result)
print((itertools.combinations(available_ingredients, r=1)))
