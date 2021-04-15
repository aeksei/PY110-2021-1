from itertools import count


def pow_2(num):
    return num ** 2


def is_even(num):
    return num % 2 == 0


if __name__ == '__main__':
    iter_even = filter(is_even, count(1))
    iter_pow_2 = map(pow_2, iter_even)

    iter_pow_2 = map(pow_2,
                     filter(is_even, count(1)))

    for _ in range(10):
        print(next(iter_pow_2))

    print("-" * 20)

    for num in iter_pow_2:
        print(num)
        if num > 1000000:
            break
