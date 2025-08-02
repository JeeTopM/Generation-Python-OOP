"""
Класс Knight ♞

Реализуйте класс Knight, описывающий шахматного коня.
При создании экземпляра класс должен принимать три аргумента в следующем порядке:
    horizontal — координата коня по горизонтальной оси, представленная латинской буквой от a до h
    vertical — координата коня по вертикальной оси, представленная целым числом от 1 до 8 включительно
    color — цвет коня (black или white)
Экземпляр класса Knight должен иметь три атрибута:
    horizontal — координата коня на шахматной доске по горизонтальной оси
    vertical — координата коня на шахматной доске по вертикальной оси
    color — цвет коня
"""


class Knight:
    def __init__(self, horizontal, vertical, color):
        self.horizontal = horizontal
        self.vertical = vertical
        self.color = color

    def get_char(self):
        """метод, возвращающий символ N"""
        return "N"

    def can_move(self, horizontal, vertical):
        """метод, принимающий в качестве аргументов координаты клетки
        по горизонтальной и по вертикальной осям и возвращающий True,
        если конь может переместиться на клетку с данными координатами,
        или False в противном случае"""
        current_x = ord(self.horizontal) - ord("a")
        current_y = 8 - self.vertical

        target_x = ord(horizontal) - ord("a")
        target_y = 8 - vertical

        dx = abs(target_x - current_x)
        dy = abs(target_y - current_y)

        return (dx == 2 and dy == 1) or (dx == 1 and dy == 2)

    def move_to(self, horizontal, vertical):
        """метод, принимающий в качестве аргументов координаты клетки по
        горизонтальной и по вертикальной осям и заменяющий текущие координаты
        коня на переданные. Если конь из текущей клетки не может переместиться
        на клетку с указанными координатами, его координаты должны остаться неизменными
        """
        if self.can_move(horizontal, vertical):
            self.horizontal = horizontal
            self.vertical = vertical

    def draw_board(self):
        """метод, печатающий шахматное поле, отмечающий на этом поле коня и клетки,
        на которые может переместиться конь. Пустые клетки должны быть отображены
        символом ., конь — символом N, клетки, на которые может переместиться конь,
        — символом *"""
        board = [["." for _ in range(8)] for _ in range(8)]
        knight_x = ord(self.horizontal) - ord("a")
        knight_y = 8 - self.vertical

        board[knight_y][knight_x] = self.get_char()

        for i in range(8):
            for j in range(8):
                target_h = chr(ord("a") + j)
                target_v = 8 - i
                if (i != knight_y or j != knight_x) and self.can_move(
                    target_h, target_v
                ):
                    board[i][j] = "*"

        for row in board:
            print("".join(row))


# 1
knight = Knight("a", 2, "white")
print(knight.color, knight.get_char())  # white N
print(knight.horizontal, knight.vertical)  # c 3


# 2
knight = Knight("c", 3, "white")
print(knight.horizontal, knight.vertical)  # c 3
print(knight.can_move("e", 5))  # False
print(knight.can_move("e", 4))  # True
knight.move_to("e", 4)
print(knight.horizontal, knight.vertical)  #  e 4

# 3
knight = Knight("c", 3, "white")
knight.draw_board()
"""
........
........
........
.*.*....
*...*...
..N.....
*...*...
.*.*....
"""
