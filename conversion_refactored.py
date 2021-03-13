import conversion

def convert(fromUnit, toUnit, value):
    """
    Convert
    """
    if fromUnit == "C" and toUnit == "K":
        # do Celsius to Kelving
        kelvin = 273.15 + value
        return kelvin
    elif fromUnit == "C" and toUnit == "F":
        # do Celsius to Fahrenheit
        fahrenheit = (value * 1.8) + 32
        return fahrenheit
    elif fromUnit == "K" and toUnit == "F":
        return conversion.convertKelvinToFahrenheit(value)
    elif fromUnit == "m" and toUnit == "yr":
        # do meter to yards conversion
        return conversion.convertMeterToYard(value)
