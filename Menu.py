from Board import (
    Board,
)


class Menu:
    """Класс меню шахмат."""

    def print_main_menu(self) -> None:
        """Вывод пунктов главного пользовательского меню."""

        print(
            '\n0: Выход из игры\n'
            '1: Сделать ход\n'
        )

    def main_menu(self, choice: int, board: Board):
        """Главное пользовательское меню.

        Args:
            choise: Выбор пользователя.

        Returns:
            is_running: Продолжается ли работа программы.

        """

        is_running = True

        match choice:
            case 0:
                is_running = False
            case 1:
                flag_move_is_made = False

                while not(flag_move_is_made):
                    try:
                        start_row, start_col, new_row, new_col = input("\nВведите координаты фигуры, которой хотите сходить и координаты клетки, куда хотите сходить").split()

                        start_row, start_col, new_row, new_col = int(start_row), int(start_col), int(new_row), int(new_col)
                    except:
                        print("\nНеправильно введенные координаты.")

                    flag_move_is_made = board.move_figure(start_row, start_col, new_row, new_col)

                    if flag_move_is_made is False:
                        print("Неправильно введенные координаты.")
        
        return is_running
