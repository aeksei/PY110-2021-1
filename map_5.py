if __name__ == '__main__':
    list_words = [
        "Goldenrod",
        "Purple",
        "Salmon",
        "Turquoise",
        "Cyan"
    ]

    iter_words = map(str.upper, list_words)
    for word in iter_words:
        print(word)

    for word in map(str.upper, list_words):
        print(word)


