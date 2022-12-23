class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

inp_num1 = input("Введите число 1: ")
inp_num2 = input("Введите число 2: ")

try:
    inp_1 = int(inp_num1)
    inp_2 = int(inp_num2)
    if inp_2 == 0:
        raise OwnError("Делить на ноль нельзя!")
except ValueError:
    print("Вы ввели не число")
except OwnError as err:
    print(err)
else:
    print(f"Все хорошо. Ваше число: {inp_1 / inp_2}")