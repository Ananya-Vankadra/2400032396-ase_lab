import unittest

from booking import calculate_ticket_price

class TestBooking(unittest.TestCase):

    def test_calculate_ticket_price(self):
        self.assertEqual(calculate_ticket_price(150, 2), 300)

    def test_invalid_ticket_count(self):
        with self.assertRaises(ValueError):
            calculate_ticket_price(150, 0)


if __name__ == "__main__":
    unittest.main()
