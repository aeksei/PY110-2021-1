def check_iter_obj(fn):
    def wrapper(*args, **kwargs):
        for index, arg in enumerate(args, start=1):
            try:
                iter(arg)
            except TypeError:
                msg = "Объект <название или номер позиционного аргумента> <значение аргумента> не является итерируемым"
                raise TypeError(msg)

        for kwarg_name, kwarg_value in kwargs.items():
            ...

        result = fn(*args, **kwargs)
        return result
    return wrapper


@check_iter_obj
def tmp_1(str_):
    pass


if __name__ == '__main__':
    tmp_1('123')
    tmp_1(12)
