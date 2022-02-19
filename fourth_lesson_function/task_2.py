
def inf_params(**params):
    # принимает неограниченое кол-во параметров, печатает только name, city, job
    # Если хотя бы один из параметров не задан, то не печатать ничего
    if "name" and "city" and "job" in params.keys():
        print(params['name'], params['city'], params['job'])
    else:
        print()

inf_params(name='John', city='Nizhiy Tagil', job='Driver')
inf_params(name='Mary', city='Kushva', job='Teacher', kids=True, age=45)
inf_params(name='Max', city='Neviynky')
