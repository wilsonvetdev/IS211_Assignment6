import unittest
import conversion
import conversion_refactored

class ConversionFunctions(unittest.TestCase):

    def test_convertCelsiusToKelvin(self):
        celsius = 300
        expected = 573.15
        actual = conversion.convertCelsiusToKelvin(celsius)

        self.assertAlmostEqual(actual, expected, places=2, msg="Celsius to Kelvin conversion failed")

    def test_convertCelsiusToFahrenheit(self):
        celsius = 300
        expected = 572
        actual = conversion.convertCelsiusToFahrenheit(celsius)

        self.assertEqual(actual, expected, msg="Celsius to Fahrenheit conversion failed")

    def test_plus2(self):
        number = 5
        expected = 7
        actual = conversion.plus2(number)

        self.assertEqual(actual, expected, "Numbers don't match...")

    def test_convertCtoK(self):
        fromUnit = 'C'
        toUnit = 'K'
        value = 300
        expected = 573.15
        actual = conversion_refactored.convert(fromUnit, toUnit, value)

        self.assertAlmostEqual(actual, expected, places=2, msg="Celsius to Kelvin conversion failed")

    def test_convertCtoF(self):
        fromUnit = 'C'
        toUnit = 'F'
        value = 300
        expected = 572
        actual = conversion_refactored.convert(fromUnit, toUnit, value)

        self.assertAlmostEqual(actual, expected, places=2, msg="Celsius to Fahrenheit conversion failed")
    
    def test_convertMtoY(self):
        fromUnit = 'm'
        toUnit = 'yr'
        value = 5
        expected = 5.4680
        actual = conversion_refactored.convert(fromUnit, toUnit, value)

        self.assertAlmostEqual(actual, expected, places = 4, msg="Meter to yard conversion failed")

    def test_convertMeterToYard(self):
        meter = 5
        expected = 5.4680 
        actual = conversion.convertMeterToYard(meter)

        self.assertAlmostEqual(actual, expected, places=4, msg="Meter to yard conversion failed")


if __name__ == '__main__':
    unittest.main()
