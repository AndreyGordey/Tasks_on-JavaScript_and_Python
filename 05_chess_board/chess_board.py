import sys
def create_chess_board():
    board = ""
    for row in range(8):
        for col in range(8):
            # Определяем, что добавить: '#' или ' '
            if (row + col) % 2 == 0:
                board += " "
            else:
                board += "#"
        board += "\n"  # Переход на новую строку после каждой строки доски
    return board

# Создание и вывод шахматной доски
chess_board = create_chess_board()
print(chess_board)

