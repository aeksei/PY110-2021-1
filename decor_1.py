def decorator(fn):
    def wrapper():
        ...
        result = fn()
        ...
        return result
    return wrapper


def make_string_upper(fn):
    def wrapper(string):
        string = string.upper()
        result = fn(string)
        ...
        return result
    return wrapper


# @make_string_upper
def print_text(string):  # аргумент может быть в любом регистре
    print(string)  # на выходе всегда в верхнем регистре
# print_text = make_string_upper(print_text)


if __name__ == '__main__':
    print_text('abc')
