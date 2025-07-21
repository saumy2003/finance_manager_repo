# tests/test_transactions.py

import unittest
from database import get_connection

class TestTransactions(unittest.TestCase):

    def test_transaction_table_exists(self):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='transactions'")
            table = cursor.fetchone()
            self.assertIsNotNone(table)

if __name__ == '__main__':
    unittest.main()
