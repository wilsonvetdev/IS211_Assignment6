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

    def test_convertKtoC(self):
        fromUnit = 'K'
        toUnit = 'C'
        value = 500
        expected = 773.15
        actual = conversion_refactored.convert(fromUnit, toUnit, value)

        self.assertAlmostEqual(actual, expected, places=2, msg="Celsius to Fahrenheit conversion failed")
    
    def test_convertMtoY(self):
        fromUnit = 'm'
        toUnit = 'yr'
        value = 5
        expected = 5.4680
        actual = conversion_refactored.convert(fromUnit, toUnit, value)

        self.assertAlmostEqual(actual, expected, places = 4, msg="Meter to yard conversion failed")
    
    def test_convertYardToMeter(self):
        fromUnit = 'yr'
        toUnit = 'm'
        value = 20
        expected = 18.2881
        actual = conversion_refactored.convert(fromUnit, toUnit, value)

        self.assertAlmostEqual(actual, expected, places=2, msg="Yard to meter conversion failed")
    
    def test_convertMeterToMiles(self):
        fromUnit = 'm'
        toUnit = 'ml'
        value = 2000
        expected = 1.242742
        actual = conversion_refactored.convert(fromUnit, toUnit, value)

        self.assertAlmostEqual(actual, expected, places=2, msg="Meter to miles conversion failed")

    def test_conversionUnits(self):
        '''Conversions not possible between these two units'''
        arguments = ['ml', 'C', '500']
        self.assertRaises(conversion_refactored.ConversionNotPossible, conversion_refactored.convert, *arguments)


if __name__ == '__main__':
    unittest.main()
