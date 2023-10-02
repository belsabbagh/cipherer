from .__base import EncMethod


class Vigenere(EncMethod):
    def __init__(self, key: str) -> None:
        self.key = key
        super().__init__()

    def __pad_key(self, data_len: int) -> str:
        key = self.key
        for i in range(data_len - len(self.key)):
            key += key[i % len(key)]
        return "".join(key)

    def __make_key(self, data_len: int) -> str:
        key = self.key
        if len(key) > data_len:
            return key[:data_len]
        if len(key) <= data_len:
            return self.__pad_key(data_len)

    def encrypt(self, data: str) -> str:
        key = self.__make_key(len(data))
        cipher_text = []
        for i in range(len(data)):
            x = (ord(data[i]) + ord(key[i])) % 26
            x += ord("A")
            cipher_text.append(chr(x))
        return "".join(cipher_text)

    def decrypt(self, data: str) -> str:
        key = self.__make_key(len(data))
        plain_text = []
        for i in range(len(data)):
            x = (ord(data[i]) - ord(key[i]) + 26) % 26
            x += ord("A")
            plain_text.append(chr(x))
        return "".join(plain_text)
