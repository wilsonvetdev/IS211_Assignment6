import conversion

class ConversionNotPossible(ValueError):
    pass

def convert(fromUnit, toUnit, value):
    """
    Convert
    """

    distance_array = ["yr", "m", "ml"]
    temp_array = ["C", "K", "F"]

    if fromUnit in distance_array and toUnit in temp_array:
        raise ConversionNotPossible
    if fromUnit in temp_array and toUnit in distance_array:
        raise ConversionNotPossible

    if fromUnit == "C" and toUnit == "K":
        # do Celsius to Kelvin
        kelvin = 273.15 + value
        return kelvin
    elif fromUnit == "C" and toUnit == "F":
        # do Celsius to Fahrenheit
        fahrenheit = (value * 1.8) + 32
        return fahrenheit
    elif fromUnit == "K" and toUnit == "C":
        celsius = value - 273.15
        return celsius
    elif fromUnit == "K" and toUnit == "F":
        celsius = value - 273.15
        fahrenheit = (celsius * 1.8) + 32
        return fahrenheit
    elif fromUnit == "m" and toUnit == "yr":
        # do meter to yards conversion
        yard = value * 1.09361
        return yard
    elif fromUnit == "yr" and toUnit == "m":
        # do yards to meter conversion
        return value / 1.09361
    elif fromUnit == "m" and toUnit == "ml":
        # do mile to meter conversion
        return value * 0.000621371192

