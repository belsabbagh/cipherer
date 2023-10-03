from .__base import EncMethod
from typing import Literal


class Vigenere(EncMethod):
    def __init__(self, key: str, mode: Literal["auto", "repeat"] = "repeat") -> None:
        if mode not in ["auto", "repeat"]:
            raise ValueError("Invalid mode. Mode must be 'auto' or 'repeat'.")
        self.key = key
        self.mode = mode
        super().__init__()

    def __pad_key(self, data_len: int) -> str:
        key = self.key
        for i in range(data_len - len(self.key)):
            key += key[i % len(key)]
        return "".join(key)

    def __make_key(self, data: str) -> str:
        data_len = len(data)
        key = self.key
        if self.mode == "auto":
            return (self.key + data)[:data_len]
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
