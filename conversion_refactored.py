import conversion

class ConversionNotPossible(ValueError):
    pass

def convert(fromUnit, toUnit, value):
    """
    Convert
    """

    distance_array = ["yr", "m", "ml"]
    temp_array = ["C", "K", "F"]



    if fromUnit == "C" and toUnit == "K":
        # do Celsius to Kelvin
        return conversion.convertCelsiusToKelvin(value)
    elif fromUnit == "C" and toUnit == "F":
        # do Celsius to Fahrenheit
        return conversion.convertCelsiusToFahrenheit(value)
    elif fromUnit == "K" and toUnit == "C":
        return conversion.convertCelsiusToKelvin(value)
    elif fromUnit == "K" and toUnit == "F":
        return conversion.convertKelvinToFahrenheit(value)
    elif fromUnit == "m" and toUnit == "yr":
        # do meter to yards conversion
        return conversion.convertMeterToYard(value)
    elif fromUnit == "yr" and toUnit == "m":
        # do meter to yards conversion
        return value / 1.09361
    elif fromUnit == "m" and toUnit == "ml":
        # do meter to yards conversion
        return value * 0.000621371192

