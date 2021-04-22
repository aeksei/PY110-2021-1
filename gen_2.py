from random import choice


def random_password(alphabet, n=8):
    alphabet = list(map(str, alphabet))
    while True:
        random_list = (choice(alphabet)
                       for _ in range(n))
        yield "".join(random_list)


if __name__ == '__main__':
    gen_pass = random_password(list(range(9)))

    print(next(gen_pass))
