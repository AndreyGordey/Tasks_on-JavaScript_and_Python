def print_board(board):
    """Выводит игровое поле."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board, player):
    """Проверяет, есть ли победитель."""
    # Проверка строк, столбцов и диагоналей
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(row[col] == player for row in board):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def is_full(board):
    """Проверяет, заполнено ли поле."""
    return all(cell != " " for row in board for cell in row)


def tic_tac_toe():
    """Основная функция игры."""
    # Инициализация пустого игрового поля
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0

    print("Добро пожаловать в игру Крестики-Нолики!")
    print_board(board)

    while True:
        print(f"Ход игрока {players[current_player]}")

        # Получение хода игрока
        try:
            row = int(input("Введите номер строки (0, 1, 2): "))
            col = int(input("Введите номер столбца (0, 1, 2): "))
        except ValueError:
            print("Пожалуйста, введите корректные числа.")
            continue

        # Проверка корректности ввода
        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Некорректный ввод. Попробуйте снова.")
            continue

        if board[row][col] != " ":
            print("Эта клетка уже занята. Попробуйте снова.")
            continue

        # Сделать ход
        board[row][col] = players[current_player]
        print_board(board)

        # Проверка на победу
        if check_winner(board, players[current_player]):
            print(f"Игрок {players[current_player]} победил!")
            break

        # Проверка на ничью
        if is_full(board):
            print("Ничья! Игровое поле заполнено.")
            break

        # Смена игрока
        current_player = 1 - current_player


# Запуск игры
if __name__ == "__main__":
    tic_tac_toe()
