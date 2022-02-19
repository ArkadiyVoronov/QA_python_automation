"""
текст: task_execute_many_taskprocessing
суффиксы task, execute
результат True

текст: eval_list_of_functions_run
суффиксы eval, execute
результат False
"""




def check_valid_input():
    text = input().split('_')
    keyword = input().split(', ')
    for word in keywords:
        if word not in text:
            return False
    return True

print(check_valid_input())

text = ['task_execute_many_taskprocessing']
keyword = ['task, execute']