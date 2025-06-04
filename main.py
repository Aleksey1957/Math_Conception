class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def display(self):
        return f'{self.numerator}/{self.denominator}'

    def sum_fractions(self, fraction2):
        new_numerator = self.numerator * fraction2.denominator + fraction2.numerator * self.denominator
        new_denominator = self.denominator * fraction2.denominator
        return new_numerator, new_denominator

    def sub_fractions(self, fraction2):
        new_numerator = self.numerator * fraction2.denominator - fraction2.numerator * self.denominator
        new_denominator = self.denominator * fraction2.denominator
        return new_numerator, new_denominator

    def multiply_fractions(self, fraction2):
        new_numerator = self.numerator * fraction2.numerator
        new_denominator = self.denominator * fraction2.denominator
        return Fraction(new_numerator, new_denominator)

    def divide_fraction(self, fraction2):
        new_numerator = self.numerator * fraction2.denominator
        new_denominator = self.denominator * fraction2.numerator
        return Fraction(new_numerator, new_denominator)

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(temperature):
        fahrenheit = (temperature * 1.8) + 32
        return f'Температура по фаренгейту: {round(fahrenheit, 1)}'

    @staticmethod
    def fahrenheit_to_celsius(temperature):
        celsius = 5 / 9 * (temperature - 32)
        return f'Температура по цельсии: {round(celsius, 2)}'

class MetricSystemConversion:
    @staticmethod
    def km_to_miles(km):
        miles = float(km) * 0.621371
        return f'In {km} km -> {miles} mi'

    @staticmethod
    def miles_to_km(miles):
        km = float(miles) * 1.60934
        return f'In {miles} mi -> {km} km'

    @staticmethod
    def liters_to_halons(liters):
        halons = liters / 3.785
        return f'In {liters} l -> {halons} gl'

    @staticmethod
    def halons_to_liters(halons):
        liters = float(halons) * 3.785
        return f'{halons} gl -> {liters} l'





    


