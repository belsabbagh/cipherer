from src.methods import Playfair


def test_encrypt():
    method = Playfair("MONARCHY")
    res = method.encrypt("INSTRUMENTS")
    assert res == "GATLMZCLRQXA"


def test_decrypt():
    method = Playfair("MONARCHY")
    res = method.decrypt("GATLMZCLRQXA")
    assert res == "INSTRUMENTSX"


def test_key_not_alpha():
    try:
        _ = Playfair("MONARCHY1")
        raise AssertionError("Key must be alphabetic.")
    except ValueError as e:
        assert str(e) == "Invalid key. Key must only contain letters."
