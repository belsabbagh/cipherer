from .__base import EncMethod
from string import ascii_uppercase as ALPHABET

class Playfair(EncMethod):
    def __init__(self, key: str) -> None:
        self.key = key
        self.__generate_matrix()
        super().__init__()

    def __char_generator(self) -> str:
        mat_str = self.key
        for c in ALPHABET:
            if len(mat_str) == 25:
                break
            if c in mat_str or c == "J":
                continue
            mat_str += c
        return mat_str

    def __generate_matrix(self) -> dict[str, tuple[int, int]]:
        self.matrix = {}
        mat_chars = self.__char_generator()
        for i in range(5):
            for j in range(5):
                char = mat_chars[i * 5 + j]
                self.matrix[char] = (i, j)
        return self.matrix

    def __make_pairs(self, data: str) -> list[str]:
        pairs = []
        for i in range(0, len(data), 2):
            pair = data[i : i + 2]
            if len(pair) == 1:
                pair += "X"
            if pair[0] == pair[1]:
                pair = pair[0] + "X"
            pairs.append(pair)
        return pairs

    def __get_char(self, pos: tuple[int, int]) -> str:
        return list(filter(lambda x: self.matrix[x] == pos, self.matrix))[0]

    def __process_pair(self, pair: str, reverse=False) -> str:
        d = -1 if reverse else 1
        x1, y1 = self.matrix[pair[0]]
        x2, y2 = self.matrix[pair[1]]

        if x1 == x2:
            return self.__get_char((x1, (y1 + d) % 5)) + self.__get_char(
                (x2, (y2 + d) % 5)
            )
        if y1 == y2:
            return self.__get_char(((x1 + d) % 5, y1)) + self.__get_char(
                ((x2 + d) % 5, y2)
            )
        return self.__get_char((x1, y2)) + self.__get_char((x2, y1))

    def encrypt(self, data: str) -> str:
        data = data.replace("J", "I")
        pairs = self.__make_pairs(data)
        enc_pairs = [self.__process_pair(pair) for pair in pairs]
        return "".join(enc_pairs)

    def decrypt(self, data: str) -> str:
        pairs = self.__make_pairs(data)
        dec_pairs = [self.__process_pair(pair, True) for pair in pairs]
        return "".join(dec_pairs)
