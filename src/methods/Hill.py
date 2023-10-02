import numpy as np
from .__base import EncMethod


class Hill(EncMethod):
    def __init__(self, key: str) -> None:
        csv = self.__parse_csv(key)
        if not all([len(row) == len(csv) for row in csv]):
            raise ValueError("Invalid key. Matrix must be square.")
        self.key = csv
        super().__init__()

    def __parse_csv(self, csv: str) -> list[list[int]]:
        return [[int(num) for num in row.split(",")] for row in csv.split("\n")]

    def __get_substrings(self, text, size):
        substrings = []
        for i in range(0, len(text), size):
            substrings.append(text[i : i + size])
        return substrings

    def encrypt(self, data: str) -> str:
        while len(data) % len(self.key) != 0:
            data += "X"
        subs = self.__get_substrings(data, len(self.key))
        sub_vectors = [[ord(i) - 65 for i in block] for block in subs]
        res_vectors = [
            [i % 26 for i in np.matmul(self.key, block)] for block in sub_vectors
        ]
        res_chars = ["".join([chr(i + 65) for i in block]) for block in res_vectors]
        return "".join(res_chars)

    def decrypt(self, data: str) -> str:
        pass
