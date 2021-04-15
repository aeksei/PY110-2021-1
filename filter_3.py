from itertools import repeat


def task_3(str_, list_index):
    result = "".join(map(get_char,
                         repeat(str_), list_index))
    return result


def get_char(str_, index):  # todo operator
    return str_[index]


if __name__ == '__main__':
    example_str = "Всем привет"
    indexes = [1, 3, 5]

    print(task_3(example_str, indexes))
    # todo list comprehension
