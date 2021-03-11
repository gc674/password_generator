import unittest
import encrypt
import os


class testencrypt(unittest.TestCase):
    key = "cheia.tst"

    def test_genkey(self):
        encrypt.gen_key(self.key)
        actual = os.path.exists("cheia.tst")
        expected = os.path.exists(self.key)
        self.assertEqual(actual, expected)

    def test_loadkey(self):
        actual = encrypt.read_key(self.key)
        expected = encrypt.load_key(self.key)
        self.assertEqual(actual, expected)


    def test_decrypt(self):
        actual = "oraoraora".encode()
        expected = encrypt.decriptare(actual, self.key)
        self.assertEqual(actual, expected)
