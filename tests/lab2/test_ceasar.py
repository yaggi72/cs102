import unittest
from src.lab2.caesar import encrypt_caesar
from src.lab2.caesar import decrypt_caesar


class Test(unittest.TestCase):
    def test_encryption(self):
        assert encrypt_caesar('Menya zovut Moriatie... I da.. da da', 5) == 'Rjsdf etazy Rtwnfynj... N if.. if if'
        assert encrypt_caesar('') == ''
        assert encrypt_caesar('123A') == '123D'
        assert encrypt_caesar('123123123', 256) == 'Ошибка. Сдвиг больше 27.'

    def test_decryption(self):
        assert decrypt_caesar('Rjsdf etazy Rtwnfynj... N if.. if if', 5) == 'Menya zovut Moriatie... I da.. da da'
        assert decrypt_caesar('') == ''
        assert decrypt_caesar('123D') == '123A'
        assert decrypt_caesar('123123123', 256) == 'Ошибка. Сдвиг больше 27.'