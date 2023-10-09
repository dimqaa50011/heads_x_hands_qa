from typing import List
from random import randint


class ArrayGenerator:
    def __init__(self, n: int) -> None:
        self._n = n
        self._sizes = {}
        self._arrays = []

    def create(self):
        self._get_arrays()
        return self._arrays

    def _get_arrays(self):
        for i in range(0, self._n + 1):
            arr = self._get_array(self._n)
            self._sort(arr, i)
            self._arrays.append(arr)

    def _sort(self, arr: List[int], i: int):
        reverse = True
        if i % 2 == 0:
            reverse = False
        arr.sort(reverse=reverse)

    def _get_array(self, n: int):
        length = randint(1, self._n * 10)
        while True:
            try:
                self._sizes[length]
                continue
            except KeyError as ex:
                self._sizes[length] = True
                arr = [0] * length
                return self._fill_array(arr)

    def _fill_array(self, arr: List[int], min: int = 1, max: int = 10**5):
        for index in range(0, len(arr)):
            arr[index] = randint(min, max)
        return arr
