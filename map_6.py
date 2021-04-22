from operator import add

def my_sum(a, b):
    return a + b

lambda a, b: a + b


if __name__ == '__main__':
    l1 = [1, 2, 3]
    l2 = [4, 5, 6]
    list(map(lambda a, b: a + b,
             l1,
             l2))

    # print(list(map(, l1, l2)))
