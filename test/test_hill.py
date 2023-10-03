from src.methods import Hill

def test_encrypt():
    method = Hill("9,4\n5,7")
    res = method.encrypt("meetmeattheusualplaceattenratherthaneightoclockx")
    assert res == 'ukixukydromeiwszxwiokunukhxhroajroanqyebtlkjegad'.upper()

def test_decrypt():
    method = Hill("9,4\n5,7")
    res = method.decrypt("ukixukydromeiwszxwiokunukhxhroajroanqyebtlkjegad")
    assert res == 'meetmeattheusualplaceattenratherthaneightoclockx'.upper()
    
def test_key_not_square_error():
    try:
        method = Hill("9,45,7")
        res = method.encrypt("meetmeattheusualplaceattenratherthaneightoclock")
        assert res == 'ukixukydromeiwszxwiokunukhxhroajroanqyebtlkjegad'.upper()
    except ValueError as e:
        assert str(e) == "Invalid key. Matrix must be square."
    
def test_key_not_invertible():
    try:
        _ = Hill("2,4\n1,2")
        assert False
    except ValueError as e:
        assert str(e) == "Invalid key. Matrix is not invertible."
        
