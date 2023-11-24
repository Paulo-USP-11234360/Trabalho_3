from scripts.senha import check_password

def test_verificar_senha():
    assert check_password("senha_correta") is True
    assert check_password("senha_incorreta") is False
