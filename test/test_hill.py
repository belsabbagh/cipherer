from src.methods import Hill

def test_encrypt():
    method = Hill("9,4\n5,7")
    res = method.encrypt("meetmeattheusualplaceattenratherthaneightoclockx")
    assert res == 'ukixukydromeiwszxwiokunukhxhroajroanqyebtlkjegad'.upper()

def test_decrypt():
    method = Hill("9,4\n5,7")
    res = method.decrypt("ukixukydromeiwszxwiokunukhxhroajroanqyebtlkjegad")
    assert res == 'meetmeattheusualplaceattenratherthaneightoclockx'.upper()