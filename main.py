# создается класс
class Fraction:
    # создается конструктор класса для доступа к отдельным полям
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    # создается метод для вывода дроби
    def display(self):
        return f'{self.numerator}/{self.denominator}'

    # создается метод для сложения двух дробей
    def sum_fractions(self, fraction2):
        new_numerator = self.numerator * fraction2.denominator + fraction2.numerator * self.denominator
        new_denominator = self.denominator * fraction2.denominator
        return new_numerator / new_denominator

    # создается метод для вычитания двух дробей
    def sub_fractions(self, fraction2):
        new_numerator = self.numerator * fraction2.denominator - fraction2.numerator * self.denominator
        new_denominator = self.denominator * fraction2.denominator
        return new_numerator / new_denominator

    # создается метод для умножения двух дробей
    def multiply_fractions(self, fraction2):
        new_numerator = self.numerator * fraction2.numerator
        new_denominator = self.denominator * fraction2.denominator
        return new_numerator / new_denominator

    # создается метод для деления двух дробей
    def divide_fraction(self, fraction2):
        new_numerator = self.numerator * fraction2.denominator
        new_denominator = self.denominator * fraction2.numerator
        return new_numerator / new_denominator

# создается класс для перевода температуры
class TemperatureConverter:
    # создается статичный метод для перевода температуры из цельсия в фаренгейт
    @staticmethod
    def celsius_to_fahrenheit(temperature):
        fahrenheit = (temperature * 1.8) + 32
        return f'Температура по фаренгейту: {round(fahrenheit, 1)}'

    # создается статичный метод для перевода температуры из фаренгейта в цельсий
    @staticmethod
    def fahrenheit_to_celsius(temperature):
        celsius = 5 / 9 * (temperature - 32)
        return f'Температура по цельсии: {round(celsius, 2)}'

# создается класс для перевода метрической системы
class MetricSystemConversion:
    # создается статичный метод для перевода из км. в мили
    @staticmethod
    def km_to_miles(km):
        miles = float(km) * 0.621371
        return f'In {km} km -> {miles} mi'

    # создается статичный метод для перевода из миль в км.
    @staticmethod
    def miles_to_km(miles):
        km = float(miles) * 1.60934
        return f'In {miles} mi -> {km} km'

    # создается статичный метод для перевода из литров в галоны
    @staticmethod
    def liters_to_halons(liters):
        halons = liters / 3.785
        return f'In {liters} l -> {halons} gl'

    # создается статичный метод для перевода температуры из галонов в литры
    @staticmethod
    def halons_to_liters(halons):
        liters = float(halons) * 3.785
        return f'{halons} gl -> {liters} l'


