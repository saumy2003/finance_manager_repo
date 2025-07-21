# tests/test_auth.py

import unittest
from auth import hash_password

class TestAuth(unittest.TestCase):

    def test_hash_password_consistency(self):
        password = "secure123"
        hashed1 = hash_password(password)
        hashed2 = hash_password(password)
        self.assertEqual(hashed1, hashed2)

    def test_hash_password_uniqueness(self):
        self.assertNotEqual(hash_password("pass1"), hash_password("pass2"))

if __name__ == '__main__':
    unittest.main()
