class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


class Cell:
    def __init__(self, quantity):
        self.quantity = quantity

    def __str__(self):
        return f'{self.quantity}'

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        try:
            if self.quantity < other.quantity:
                raise OwnError("Результат меньше 0")
        except ValueError:
            print("Вы ввели не число")
        except OwnError as err:
            return err
        else:
            return self.quantity - other.quantity

    def __mul__(self, other):
        return Cell(self.quantity * other.quantity)

    def __truediv__(self, other):
        return Cell(self.quantity / other.quantity)


c = Cell(1)
o = Cell(2)
print(c + o)
print(c - o)
print(c * o)
print(c / o)