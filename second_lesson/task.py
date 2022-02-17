a = ["текст: task_execute_many_taskprocessing", "task", "execute"]
b = ["текст: eval_list_of_functions_run", "eval", "execute"]
c = ["текст: task_execute_many_taskprocessing", "execute", "task", "many", "biba"]


def find_suffix(x:list):
    """проверка наличия в первом элементе списка - остальных элементов списка"""
    origin = x[0]
    for c in x[1:]:
        if c not in origin:
            return False
        return True

print(find_suffix(a))
print(find_suffix(b))
print(find_suffix(c))
