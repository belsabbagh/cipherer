from src.methods import Vigenere


def test_encrypt():
    method = Vigenere("MRJQJCGSGIZVR")
    res = method.encrypt("CASHNOTNEEDED")
    assert res == "ORBXWQZFKMCZU"


def test_decrypt():
    method = Vigenere("MRJQJCGSGIZVR")
    res = method.decrypt("ORBXWQZFKMCZU")
    assert res == "CASHNOTNEEDED"
