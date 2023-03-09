from unittest import TestCase, mock, main
from io import StringIO

# This import line is not needed in Colab
from ATM import pin, pin_check, withdrawal, view_balance, user_selection


class TestWithdraw(TestCase):

    def test_withdraw_valid_amount(self):
        with mock.patch("builtins.input", side_effect=["30"]):
            updated_balance = withdrawal(starting_balance=100)
            self.assertEqual(updated_balance, 70)


    def test_withdraw_negative_amount(self):
        with mock.patch("builtins.input", side_effect=["-20"]):
            with self.assertRaises(ValueError):
                withdrawal(starting_balance=300)

    def test_withdraw_non_numeric_amount(self):
        with mock.patch("builtins.input", side_effect=["hello"]):
            with self.assertRaises(ValueError):
                withdrawal(starting_balance=400)


class TestDisplayBalance(TestCase):

    def test_display_integer_amount(self):
        with mock.patch("sys.stdout", new=StringIO()) as output:
            view_balance(123)
            printed_line = output.getvalue().strip()
            self.assertEqual(printed_line, "You have £123.00 in your account.")

    def test_display_float_amount(self):
        with mock.patch("sys.stdout", new=StringIO()) as output:
            view_balance(123.45)
            printed_line = output.getvalue().strip()
            self.assertEqual(printed_line, "You have £123.45 in your account.")


if __name__ == '__main__':
    main()
