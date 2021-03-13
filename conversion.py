def convertCelsiusToKelvin(celsius):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Kelvins"""
    kelvin = 273.15 + celsius
    
    return kelvin


def convertCelsiusToFahrenheit(celsius):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Fahrenheit"""
    fahrenheit = (celsius * 1.8) + 32
    
    return fahrenheit


def convertKelvinToCelsius(kelvin):
    """
    Converts celsius to kelvin
    """
    celsius = kelvin - 273.15
    return celsius


def convertKelvinToFahrenheit(kelvin):
    """
    Converts Celsius to Fahrenheit
    """
    celsius = convertKelvinToCelsius(kelvin)
    fahrenheit = convertCelsiusToFahrenheit(celsius)
    return fahrenheit


def convertFahrenheitToKelvin(fahrenheit):
    """
    Converts celsius to kelvin
    """
    celsius = convertFahrenheitToCelsius(fahrenheit)
    kelvin = convertCelsiusToKelvin(celsius)
    return kelvin


def convertFahrenheitToCelsius(fahrenheit):
    """
    Converts Celsius to Fahrenheit
    """

    celsius = (fahrenheit - 32) / 1.8
    return celsius


def plus2(number):
    """Returns number + 2"""
    return number + 2


def convertMeterToYard(meter):
    """
    Converts meter to yard
    """

    yard = meter * 1.09361
    return yard

