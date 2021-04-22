from itertools import zip_longest

print(list(zip("abc", [1, 2, 3, 4])))
print(list(zip_longest("abc", [1, 2, 3, 4],
                       fillvalue=None)))