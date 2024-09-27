class calculator:
    """A class that represents a calculator
    Attributes:
        numbers (list): A list of numbers
        
        Methods:
        __add__(self, other): A method that adds a number to the list
        __mul__(self, other): A method that multiplies a number to the list
        __sub__(self, other): A method that subtracts a number from the list
        __truediv__(self, other): A method that divides a number to the list
        __str__(self): A method that returns the list of numbers as a string"""

    def __init__(self, numbers):
        self.numbers = numbers

    def __add__(self, other):
        """A method that adds a number to the list"""
        self.numbers = [x + other for x in self.numbers]  # Mevcut nesneyi güncelle
        print(self.numbers)

    def __mul__(self, other):
        """A method that multiplies a number to the list"""
        self.numbers = [x * other for x in self.numbers]
        print(self.numbers)

    def __sub__(self, other):
        """A method that subtracts a number from the list"""
        self.numbers = [x - other for x in self.numbers]  # Mevcut nesneyi güncelle
        print(self.numbers)

    def __truediv__(self, other):
        """A method that divides a number to the list"""
        if other == 0:
            raise ValueError("You can't divide by zero")
        self.numbers = [x / other for x in self.numbers]  # Mevcut nesneyi güncelle
        print(self.numbers)

    def __str__(self):
        return str(self.numbers)