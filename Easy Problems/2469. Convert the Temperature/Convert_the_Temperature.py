class Solution(object):
    def convertTemperature(self, celsius):
        kelvin = celsius + 273.15
        fahrenheit = (celsius * 1.80) + 32.00
        formatted_kelvin = "{:.5f}".format(kelvin)
        formatted_fahrenheit = "{:.5f}".format(fahrenheit)
        return [float(formatted_kelvin), float(formatted_fahrenheit)]