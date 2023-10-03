import numpy as np
from .__base import EncMethod


def __get_substrings(text, size):
    substrings = []
    for i in range(0, len(text), size):
        substrings.append(text[i : i + size])
    return substrings


def process_data(data: str, matrix):
    subs = __get_substrings(data, len(matrix))
    sub_vectors = [[ord(i) - 65 for i in block] for block in subs]
    res_vectors = [[i % 26 for i in np.matmul(matrix, block)] for block in sub_vectors]
    res_chars = ["".join([chr(i + 65) for i in block]) for block in res_vectors]
    return "".join(res_chars)


def mod_inverse(a, m):
    """
    Calculate the modular multiplicative inverse of 'a' modulo 'm'.
    """
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None  # Inverse does not exist


def matrix_inverse_mod26(matrix):
    det = int(round(np.linalg.det(matrix)))
    det_inverse = mod_inverse(det, 26)
    if det_inverse is None:
        raise np.linalg.LinAlgError
    adjugate = np.round(np.linalg.inv(matrix) * det).astype(int)
    inverse_mod26 = (adjugate * det_inverse) % 26
    return inverse_mod26


class Hill(EncMethod):
    def __init__(self, key: str) -> None:
        try:
            csv = self.__parse_csv(key)
        except ValueError:
            raise ValueError("Invalid key. Matrix does not follow csv format.")
        if not all([len(row) == len(csv) for row in csv]):
            raise ValueError("Invalid key. Matrix must be square.")
        if len(csv) < 2:
            raise ValueError("Invalid key. Matrix must be at least 2x2.")
        if np.linalg.det(csv) == 0:
            raise ValueError("Invalid key. Matrix is not invertible.")
        if not all([all([isinstance(num, int) for num in row]) for row in csv]):
            raise ValueError("Invalid key. Matrix must contain integers.")
        self.key = csv
        super().__init__()

    def __parse_csv(self, csv: str) -> list[list[int]]:
        return [[int(num) for num in row.split(",")] for row in csv.split("\n")]

    def encrypt(self, data: str) -> str:
        data = data.upper()
        while len(data) % len(self.key) != 0:
            data += "X"
        return process_data(data, np.array(self.key))

    def decrypt(self, data: str) -> str:
        data = data.upper()
        if len(data) % len(self.key) != 0:
            raise ValueError("Invalid cipher text.")
        try:
            return process_data(data, matrix_inverse_mod26(np.array(self.key)))
        except np.linalg.LinAlgError:
            raise ValueError("Invalid key. Matrix is not invertible.")
