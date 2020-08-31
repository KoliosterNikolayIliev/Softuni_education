

from project.Account import Account

import unittest
import types


class AccountTests(unittest.TestCase):
    def setUp(self):
        self.account = Account("Joro", 50)
        self.account_two = Account("Pesho", 100)

    def test_validate_transaction_valid(self):
        result = Account.validate_transaction(self.account, 50)
        self.assertEqual(result, "New balance: 100")

    def test_add_transaction(self):
        self.assertEqual(len(self.account._transactions), 0)
        self.account.add_transaction(20)
        self.assertEqual(len(self.account._transactions), 1)
        self.assertEqual(self.account.balance, 70)

    def test_validate_transaction_invalid(self):
        with self.assertRaises(ValueError) as exception:
            Account.validate_transaction(self.account, -51)

    def test_str_method(self):
        self.assertEqual(str(self.account), "Account of Joro with starting amount: 50")

    def test_repr_method(self):
        self.assertEqual(repr(self.account), "Account(Joro, 50)")

    def test_add_transaction_invalid_type(self):
        with self.assertRaises(ValueError) as exception:
            self.account.add_transaction(5.6)

    def test_get_item(self):
        self.account.add_transaction(20)
        self.assertEqual(self.account[0], 20)

    def test_raise_error_index(self):
        with self.assertRaises(IndexError) as exception:
            self.assertEqual(self.account[0], 20)

    def test_not_equal(self):
        self.assertNotEqual(self.account, self.account_two)

    def test_less_than(self):
        self.assertLess(self.account, self.account_two)

    def test_greater_than(self):
        self.assertGreater(self.account_two, self.account)
        self.assertTrue(self.account_two > self.account)

    def test_add(self):
        result = self.account + self.account_two
        self.assertEqual(result.balance, 150)

    def test_len_account(self):
        self.account.add_transaction(20)
        self.account.add_transaction(50)
        self.assertEqual(len(self.account), 2)

    def test_ge(self):
        account_three = Account("Toshko", 50)
        self.assertEqual(self.account, account_three)

    def test_greater_or_equal(self):
        account_three = Account("Misho", 50)
        self.assertGreaterEqual(account_three, self.account)

    def test_validate_static_method(self):
        self.assertTrue(isinstance(self.account.validate_transaction, types.FunctionType))

    def test_custom_reverse(self):
        self.account.add_transaction(50)
        self.account.add_transaction(150)
        result = list(reversed(self.account))
        self.assertEqual(result, [150, 50])


if __name__ == "__main__":
    unittest.main()
