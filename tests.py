import unittest

from main import TemperatureConverter

class TestTemperatureConverter(unittest.TestCase):

    def setUp(self):
        self.converter = TemperatureConverter()

    # Testy dla metody celsius_to_fahrenheit
    def test_celsius_to_fahrenheit_freezing_point(self):
        self.assertAlmostEqual(self.converter.celsius_to_fahrenheit(0), 32)

    def test_celsius_to_fahrenheit_boiling_point(self):
        self.assertAlmostEqual(self.converter.celsius_to_fahrenheit(100), 212)

    def test_celsius_to_fahrenheit_below_freezing(self):
        self.assertAlmostEqual(self.converter.celsius_to_fahrenheit(-40), -40)

    def test_celsius_to_fahrenheit_positive(self):
        self.assertAlmostEqual(self.converter.celsius_to_fahrenheit(25), 77)

    def test_celsius_to_fahrenheit_negative(self):
        self.assertAlmostEqual(self.converter.celsius_to_fahrenheit(-10), 14)

    # Testy dla metody fahrenheit_to_celsius
    def test_fahrenheit_to_celsius_freezing_point(self):
        self.assertAlmostEqual(self.converter.fahrenheit_to_celsius(32), 0)

    def test_fahrenheit_to_celsius_boiling_point(self):
        self.assertAlmostEqual(self.converter.fahrenheit_to_celsius(212), 100)

    def test_fahrenheit_to_celsius_below_freezing(self):
        self.assertAlmostEqual(self.converter.fahrenheit_to_celsius(-40), -40)

    def test_fahrenheit_to_celsius_positive(self):
        self.assertAlmostEqual(self.converter.fahrenheit_to_celsius(77), 25)

    def test_fahrenheit_to_celsius_negative(self):
        self.assertAlmostEqual(self.converter.fahrenheit_to_celsius(14), -10)

if __name__ == '__main__':
    unittest.main()
