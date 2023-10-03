from src.methods import Vigenere


def test_encrypt():
    method = Vigenere("MRJQJCGSGIZVR")
    res = method.encrypt("CASHNOTNEEDED")
    assert res == "ORBXWQZFKMCZU"


def test_decrypt():
    method = Vigenere("MRJQJCGSGIZVR")
    res = method.decrypt("ORBXWQZFKMCZU")
    assert res == "CASHNOTNEEDED"


def test_not_a_mode():
    try:
        _ = Vigenere("MRJQJCGSGIZVR", "not a mode")
        raise AssertionError("Mode must be either 'auto' or 'repeat'.")
    except ValueError as e:
        assert str(e) == "Invalid mode. Mode must be 'auto' or 'repeat'."
