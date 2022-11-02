class Temperature:
    def __init__(self, celsius):
        self.__celsius = celsius

    def to_celsius(self):
        return self.__celsius

    def to_fahrenheit(self):
        fahrenheit = (self.__celsius * 1.8) + 32
        return fahrenheit

    def to_kelvin(self):
        kelvin = self.__celsius + 273.15
        return kelvin

    def set_temperature(self, celsius):
        if celsius >= 273.14:
            self.__celsius = celsius
        else:
            print("no")

    def __str__(self):
        return "Celsius: " + str(self.to_celsius()) \
               + "\nFahrenheit: " + str(self.to_fahrenheit()) \
               + "\nKelvin: " + str(self.to_kelvin())



