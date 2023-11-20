# class Snowfall:
#     def __init__(self, snowflakes):
#         self.snowflakes = snowflakes
#
#     def __add__(self, n):
#         return self.snowflakes + n
#
#     def __sub__(self, n):
#         return self.snowflakes - n
#
#     def __mul__(self, n):
#         return self.snowflakes * n
#
#     def __truediv__(self, n):
#         return self.snowflakes // n
#
#     def make_snow(self, snowflakes_in_row):
#         rows = self.snowflakes // snowflakes_in_row
#         result = ""
#         for _ in range(rows):
#             result += '*' * snowflakes_in_row + '\n'
#         return result
#
# # Пример использования:
# snowfall1 = Snowfall(20)
# snowfall2 = snowfall1 + 10  # Увеличение на 10 снежинок
# snowfall3 = snowfall2 - 5   # Уменьшение на 5 снежинок
# snowfall4 = snowfall3 * 3   # Умножение на 3
# snowfall5 = snowfall4 / 2   # Деление на 2
#
# print(snowfall5.snowflakes)  # Вывод: 45
#
# snowfall = Snowfall(15)
# snow_pattern = snowfall.make_snow(5)
# print(snow_pattern)
#
# class SnowFlake:
#     def __init__(self, side_length):
#         if side_length % 2 == 0:
#             raise ValueError("Side length should be an odd number.")
#         self.side_length = side_length
#         self.matrix_size = side_length + 2  # Размер матрицы с учетом рамки
#
#         # Создаем матрицу снежинки и заполняем ее дефисами
#         self.matrix = [['-' for _ in range(self.matrix_size)] for _ in range(self.matrix_size)]
#         self.initialize_snowflake()
#
#     def initialize_snowflake(self):
#         # Заполняем центральный квадрат звездочками
#         for i in range(self.side_length):
#             for j in range(self.side_length):
#                 self.matrix[i + 1][j + 1] = '*'
#
#     def thaw(self, steps):
#         for _ in range(steps):
#             # Убираем крайние звездочки со всех сторон
#             for i in range(self.matrix_size):
#                 self.matrix[i][0] = self.matrix[i][-1] = '-'
#                 self.matrix[0][i] = self.matrix[-1][i] = '-'
#
#     def freeze(self, n):
#         # Увеличиваем сторону квадрата
#         self.side_length += 2 * n
#         self.matrix_size = self.side_length + 2
#
#         # Создаем новую матрицу с учетом новой стороны квадрата
#         new_matrix = [['-' for _ in range(self.matrix_size)] for _ in range(self.matrix_size)]
#
#         # Копируем звездочки из старой матрицы в новую
#         for i in range(1, min(self.matrix_size - 1, len(self.matrix))):
#             for j in range(1, min(self.matrix_size - 1, len(self.matrix[i]))):
#                 new_matrix[i][j] = self.matrix[i][j]
#
#         self.matrix = new_matrix
#
#         # Добавляем звездочки в нужных местах
#         self.initialize_snowflake()
#
#     def thicken(self):
#         for i in range(1, self.matrix_size - 1):
#             # К каждой линии звездочек добавляем параллельные с обеих сторон
#             self.matrix[i].insert(0, '*')
#             self.matrix[i].append('*')
#
#     def show(self):
#         for row in self.matrix:
#             print(' '.join(row))
#
# # Пример использования
# snowflake = SnowFlake(3)
# snowflake.show()
# print()
#
# snowflake.thaw(1)
# snowflake.show()
# print()
#
# snowflake.freeze(2)
# snowflake.show()
# print()
#
# snowflake.thicken()
# snowflake.show()

#
# class Robot:
#     def __init__(self, x=0, y=0):
#         # Инициализация начальных координат
#         self.x = max(0, min(x, 100))  # Ограничиваем координаты от 0 до 100
#         self.y = max(0, min(y, 100))
#         self.path_history = [(self.x, self.y)]  # История перемещений
#
#     def move(self, commands):
#         for command in commands:
#             if command == 'N' and self.y < 100:
#                 self.y += 1
#             elif command == 'S' and self.y > 0:
#                 self.y -= 1
#             elif command == 'E' and self.x < 100:
#                 self.x += 1
#             elif command == 'W' and self.x > 0:
#                 self.x -= 1
#
#
#             self.path_history.append((self.x, self.y))
#
#
#         return (self.x, self.y)
#
#     def path(self):
#
#         return self.path_history
#
#
# robot = Robot(5, 9)
# print(robot.move('SEWW'))  # Перемещаемся вверх, вверх, вправо, влево, вниз
# print(robot.path())


class Talking:
    def __init__(self, name):
        self.name = name
        self.yes_count = 0
        self.no_count = 0
        self.yes_first = True

    def to_answer(self):
        if self.yes_first:
            self.yes_first = False
            self.yes_count += 1
            return "moore-moore"
        else:
            self.yes_first = True
            self.no_count += 1
            return "meow-meow"

    def number_yes(self):
        return self.yes_count

    def number_no(self):
        return self.no_count


tk = Talking('Pyssy')
print(tk.to_answer())
print(tk.to_answer())
print(tk.to_answer())
print(f'{tk.name} says "yes" {tk.number_yes()} times, "no" {tk.number_no()} times')
