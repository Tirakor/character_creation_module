from math import sqrt

message = '''
          Добро пожаловать в самую лучшую программу для вычисления
          квадратного корня из заданного числа
          '''
print(message)


def CalculateSquareRoot(number):
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number):
    """
    Проверяет - не отрицательное ли число?
     И вычмсляет его квадратный корень
     """
    if your_number <= 0:
        return
    your_number_sqrt = CalculateSquareRoot(your_number)
    print(f'Мы вычислили квадратный корень из введённого вами числа.'
          f' Это будет: {your_number_sqrt}')


print(message)
calc(25.5)
