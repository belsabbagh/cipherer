from src.methods import Caesar


def test_encrypt():
    method = Caesar(3)
    res = method.encrypt("abc")
    assert res == "def"


def test_decrypt():
    method = Caesar(3)
    res = method.decrypt("def")
    assert res == "abc"
