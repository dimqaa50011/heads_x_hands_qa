from typing import List

from app.array_generator import ArrayGenerator


def print_arrays(arrs: List):
    for arr in arrs:
        print(arr)


def start():
    n = 10
    arr_gen = ArrayGenerator(n)
    arrs = arr_gen.create()
    print_arrays(arrs)


if __name__ == "__main__":
    start()
