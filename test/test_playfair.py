from src.methods import Playfair


def test_encrypt():
    method = Playfair("MONARCHY")
    res = method.encrypt("INSTRUMENTS")
    assert res == "GATLMZCLRQXA"


def test_decrypt():
    method = Playfair("MONARCHY")
    res = method.decrypt("GATLMZCLRQXA")
    assert res == "INSTRUMENTSX"
