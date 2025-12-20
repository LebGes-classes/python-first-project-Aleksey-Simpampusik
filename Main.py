from Board import (
    Board,
)

from Menu import (
    Menu,
)


menu = Menu()

def run() -> None:
    new_board = Board()
    
    is_running = True

    while is_running:
        new_board.print_board()

        if new_board.get_current_player_color() == "White":
            print("\nХод белых")
        else:
            print("\nХод черных")

        menu.print_main_menu()
        
        command_chosen_correctly = False

        while not(command_chosen_correctly):
            try:
                choise_command = int(input('Введите выбор команды: '))
            except:
                print("Некорректно заданная команда ")

            if 0<=choise_command<2:
                command_chosen_correctly = True
            else:
                print("Некорректно заданная команда ")

        is_running = menu.main_menu(choise_command, new_board)


run()
