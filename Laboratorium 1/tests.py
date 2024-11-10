import unittest

from main import TemperatureConverter

class TestTemperatureConverter(unittest.TestCase):

    def setUp(self):
        self.converter = TemperatureConverter()

    # Testy dla metody celsius_to_fahrenheit
    def test_celsius_to_fahrenheit_freezing_point(self):
        self.assertAlmostEqual(self.converter.celsius_to_fahrenheit(0), 32)  # Blisko 32

    def test_celsius_to_fahrenheit_boiling_point(self):
        self.assertEqual(self.converter.celsius_to_fahrenheit(100), 212)  # Dokładnie 212

    def test_celsius_to_fahrenheit_below_freezing(self):
        result = self.converter.celsius_to_fahrenheit(-40)
        self.assertEqual(result, -40)  # Sprawdzamy, czy -40°C to -40°F

    def test_celsius_to_fahrenheit_positive(self):
        result = self.converter.celsius_to_fahrenheit(25)
        self.assertAlmostEqual(result, 77)
        self.assertGreater(result, 32)  # Powinno być większe od punktu zamarzania

    def test_celsius_to_fahrenheit_negative(self):
        result = self.converter.celsius_to_fahrenheit(-10)
        self.assertAlmostEqual(result, 14)
        self.assertLess(result, 32)  # Powinno być mniejsze od punktu zamarzania

    # Testy dla metody fahrenheit_to_celsius
    def test_fahrenheit_to_celsius_freezing_point(self):
        self.assertEqual(self.converter.fahrenheit_to_celsius(32), 0)  # Dokładnie 0

    def test_fahrenheit_to_celsius_boiling_point(self):
        result = self.converter.fahrenheit_to_celsius(212)
        self.assertAlmostEqual(result, 100)
        self.assertGreater(result, 0)  # Powinno być większe od zera

    def test_fahrenheit_to_celsius_below_freezing(self):
        result = self.converter.fahrenheit_to_celsius(-40)
        self.assertEqual(result, -40)  # Sprawdzamy, czy -40°F to -40°C

    def test_fahrenheit_to_celsius_positive(self):
        result = self.converter.fahrenheit_to_celsius(77)
        self.assertAlmostEqual(result, 25)
        self.assertGreater(result, 0)  # Powinno być dodatnie

    def test_fahrenheit_to_celsius_negative(self):
        result = self.converter.fahrenheit_to_celsius(14)
        self.assertAlmostEqual(result, -10)
        self.assertLess(result, 0)  # Powinno być ujemne

if __name__ == '__main__':
    unittest.main()
