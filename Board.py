from Figure import (
    Bishop,
    King,
    Knight,
    Pawn,
    Queen,
    Rook,
)


class Board():
    """Класс, определяющий поле для игры в шахматы."""

    def __init__(self) -> None:
        """Конструктор класса."""

        self.__current_player_color = "White"

        self.__white_king_row = 1
        self.__white_king_col = 4
        self.__black_king_row = 8
        self.__black_king_col = 4

        self.__board = dict()

        for row in range(1,9):
            self.__board[row] = dict()

            for col in range(1,9):
                self.__board[row][col] = None
        
        for col in range(1,9):
            self.__board[2][col] = Pawn(2, col, 'White')
            self.__board[7][col] = Pawn(7, col, 'Black')

        self.__board[1][1] = Rook(1, 1, 'White')
        self.__board[1][2] = Knight(1, 2, 'White')
        self.__board[1][3] = Bishop(1, 3, 'White')
        self.__board[1][4] = King(1, 4, 'White')
        self.__board[1][5] = Queen(1, 5, 'White')
        self.__board[1][6] = Bishop(1, 6, 'White')
        self.__board[1][7] = Knight(1, 7, 'White')
        self.__board[1][8] = Rook(1, 8, 'White')

        self.__board[8][1] = Rook(8, 1, 'Black')
        self.__board[8][2] = Knight(8, 2, 'Black')
        self.__board[8][3] = Bishop(8, 3, 'Black')
        self.__board[8][4] = King(8, 4, 'Black')
        self.__board[8][5] = Queen(8, 5, 'Black')
        self.__board[8][6] = Bishop(8, 6, 'Black')
        self.__board[8][7] = Knight(8, 7, 'Black')
        self.__board[8][8] = Rook(8, 8, 'Black')  
    
    def set_current_player_color(self, color: str) -> None:
        """Сеттер цвета текущего игрока.
        
        Args:
            color: Новый цвет игрока.
        
        """

        self.__current_player_color = color
    
    def get_current_player_color(self):
        """Геттер цвета текущего игрока.
        
        Returns:
            Текущий цвет игрока

        """

        return self.__current_player_color
        
    def print_board(self) -> None:
        """Выводит поле в текстовом виде в консоль."""

        print('     --- --- --- --- --- --- --- ---')

        for row in range(8, 0, -1):
            print(' ', row, end = ' ')

            if row%2==0:
                current_color_of_tyle = "White"
            else:
                current_color_of_tyle = "Black"
            
            for col in range(1, 9):
                position_figure = self.__board[row][col]

                symbol_of_figure = None

                if position_figure == None:
                    if current_color_of_tyle == "White":
                        print('\033[0m|\033[47m ', '', end = ' ')

                        current_color_of_tyle = "Black"
                    
                    elif current_color_of_tyle == "Black":
                        print('\033[0m|\033[40m ', '', end = ' ')

                        current_color_of_tyle = "White"
                else:
                    name_of_figure = position_figure.get_name_of_figure()
        
                    color_of_figure = position_figure.get_color()

                    if name_of_figure == "Pawn":
                        symbol_of_figure = "P"

                    if name_of_figure == "Knight":
                        symbol_of_figure = "K"

                    if name_of_figure == "Bishop":
                        symbol_of_figure = "B"

                    if name_of_figure == "Rook":
                        symbol_of_figure = "R"

                    if name_of_figure == "Queen":
                        symbol_of_figure = "Q"

                    if name_of_figure == "King":
                        symbol_of_figure = "K"

                    if current_color_of_tyle == "White":
                        if color_of_figure == "White":
                            if name_of_figure == "King":
                                print('\033[0m|\033[47m', '\033[37m\033[47m\033[1m\033[4m{}'.format(symbol_of_figure), end = '\033[0m\033[47m ')
                                print('\033[0m\033[47m', end = '')
                            else:
                                print('\033[0m|\033[47m', '\033[37m\033[47m{}'.format(symbol_of_figure), end = ' ')
                        else:
                            if name_of_figure == "King":
                                print('\033[0m|\033[47m', '\033[30m\033[47m\033[1m\033[4m{}'.format(symbol_of_figure), end = '\033[0m\033[47m ')
                                print('\033[0m\033[47m', end = '')
                            else:
                                print('\033[0m|\033[47m', '\033[30m\033[47m{}'.format(symbol_of_figure), end = ' ')
                            
                        current_color_of_tyle = "Black"
                    
                    elif current_color_of_tyle == "Black":
                        if color_of_figure == "White":
                            if name_of_figure == "King":
                                print('\033[40m|', '\033[37m\033[40m\033[1m\033[4m{}'.format(symbol_of_figure), end = '\033[0m\033[40m ')
                                print('\033[0m', end = '')
                            else:
                                print('\033[40m|', '\033[37m\033[40m{}'.format(symbol_of_figure), end = ' ')
                        else:
                            if name_of_figure == "King":
                                print('\033[40m|', '\033[30m\033[40m\033[1m\033[4m{}'.format(symbol_of_figure), end = '\033[0m\033[40m ')
                                print('\033[0m', end = '')
                            else:
                                print('\033[40m|', '\033[30m\033[40m{}'.format(symbol_of_figure), end = ' ')
                            
                        current_color_of_tyle = "White"
                        

            print('\033[0m|')
            print('\033[0m     --- --- --- --- --- --- --- ---')
        
        print('   ', end = '')
        for col in range(1, 9):
            print('   ', end = '')
            print(col, end = '')
        print('\n')

    def switch_color_of_current_player(self) -> None:
        """Метод, меняющий цвет хода игрока."""

        if self.get_current_player_color() == "White":
            self.set_current_player_color("Black")
        elif self.get_current_player_color() == "Black":
            self.set_current_player_color("White")

    def check_position(self, row: int, col: int) -> bool:
        """Метод, который проверяет правильность введенных координат.
        
        Args:
            row: Номер строки.
            col: Номер столбца.
        
            Returns:
                True или False в зависимости от выпонения условия.

        """

        return (1 <= row <= 8) and (1 <= col <= 8)

    def direction_of_move(self, current, new):
        """Метод для определения в какую сторону дивжется фигура.
        
        Args:
            current: Нынешнее положение.
            new: Новое положение.
        
        Returns:
            1, если в увеличение координат, -1, если в уменьшение координат.
        
        """

        return 1 if abs(new - current) == (new - current) else -1
    
    def is_under_atack(self, selected_row: int, selected_col: int, color: str) -> bool:
        """Метод, определяющий, находится ли данная ячейка под атакой фигуры цыета color.
        
        Args:
            selected_row: Номер строки.
            selected_col: Номер столбца.
            color: Цвет фигур.
        
        Returns:
            True или False.

        """
        
        is_atacked = False

        for row in range(1, 9):
            for col in range(1, 9):
                if self.__board[row][col] is not None:
                    figure = self.__board[row][col]
                    
                    if figure.get_color() == color:
                        if figure.where_can_move(selected_row, selected_col):
                            if figure.get_name_of_figure() == "Pawn":
                                if col != selected_col:
                                    is_atacked = True
                            elif figure.get_name_of_figure() == "Rook":
                                if row == selected_row:
                                    flag_no_figures = True

                                    for i in range(col, selected_col, self.direction_of_move(col, selected_col)):
                                        if self.__board[row][i] is not None:
                                            flag_no_figures = False
                                    if flag_no_figures == True:
                                        is_atacked = True
                                if col == selected_col:
                                    flag_no_figures = True
                                    for i in range(row, selected_row, self.direction_of_move(row, selected_row)):
                                        if self.__board[i][col] is not None:
                                            flag_no_figures = False
                                    if flag_no_figures is True:
                                        is_atacked = True
                            elif figure.get_name_of_figure() == "Bishop":
                                flag_no_figures = True

                                direction_cols = self.direction_of_move(col, selected_col)
                                direction_rows = self.direction_of_move(row, selected_row)

                                for i in range(1, abs(selected_col - col)):
                                    if self.__board[row+i*direction_rows][col+i*direction_cols] is not None and (row+i*direction_rows != selected_row) and (col+i*direction_cols != selected_col):
                                        flag_no_figures = False
                                    
                                if flag_no_figures is True:
                                    is_atacked = True
                            elif figure.get_name_of_figure() == "Queen":
                                if col != selected_col and row != selected_row:
                                    flag_no_figures = True

                                    direction_cols = self.direction_of_move(col, selected_col)
                                    direction_rows = self.direction_of_move(row, selected_row)

                                    for i in range(1, abs(selected_col - col)):
                                        if self.__board[row+i*direction_rows][col+i*direction_cols] is not None and (row+i*direction_rows != selected_row) and (col+i*direction_cols != selected_col):
                                            flag_no_figures = False
                                    
                                    if flag_no_figures is True:
                                        is_atacked = True
                                else:
                                    if row == selected_row:
                                        flag_no_figures = True

                                        for i in range(col, selected_col, self.direction_of_move(col, selected_col)):
                                            if self.__board[row][i] is not None:
                                                flag_no_figures = False
                                        if flag_no_figures == True:
                                            is_atacked = True
                                    if col == selected_col:
                                        flag_no_figures = True
                                        for i in range(row, selected_row, self.direction_of_move(row, selected_row)):
                                            if self.__board[i][col] is not None:
                                                flag_no_figures = False
                                        if flag_no_figures is True:
                                            is_atacked = True
                            else:
                                is_atacked = True

        
        return is_atacked
    
    def Check(self, row_of_king, col_of_king, color) -> bool:
        """Метод, определяющий, находится ли король под шахом.
        
        Args:
            row_of_king: Строка короля.
            col_of_king: Столбец короля.
            color: Цвет короля.

        Returns:
            True или False.

        """

        if color == "White":
            check = self.is_under_atack(row_of_king, col_of_king, "Black")
        else:
            check = self.is_under_atack(row_of_king, col_of_king, "White")
        
        return check
    
    def move_figure(self, current_row: int, current_col: int, new_row: int, new_col: int) -> bool:
        """Метод для перемещения фигуры по доске.
        
        Args:
            current_row: Нынешняя строка фигуры.
            current_col: Нынешний столбец фигуры.
            new_row: Новая строка фигуры.
            new_col: Новый столбец фигуры.

        Returns:
        
        """

        flag_moved_correctly = True

        selected_cell = self.__board[current_row][current_col]
        new_cell = self.__board[new_row][new_col]

        if self.check_position(new_row, new_col) is False:
            flag_moved_correctly = False
        elif current_col == new_col and current_row == new_row:
            flag_moved_correctly = False
        elif selected_cell is None:
            flag_moved_correctly = False
        elif selected_cell.get_color() != self.__current_player_color:
            flag_moved_correctly = False
        elif selected_cell.where_can_move(new_row, new_col) is False:
            flag_moved_correctly = False
        elif self.get_current_player_color() == "White" and self.Check(self.__white_king_row, self.__white_king_col, "White") and selected_cell.get_name_of_figure() != "King":
            flag_moved_correctly = False
        elif self.get_current_player_color() == "Black" and self.Check(self.__black_king_row, self.__black_king_col, "Blcak") and selected_cell.get_name_of_figure() != "King":
            flag_moved_correctly = False
        else:
            if selected_cell.get_name_of_figure() == "Pawn":
                if new_col != current_col:
                    if new_cell is None:
                        flag_moved_correctly = False
                    else:
                        self.__board[current_row][current_col] = None

                        selected_cell.set_row(new_row)
                        selected_cell.set_col(new_col)

                        if selected_cell.get_color() == "White":
                            if new_row == 8:
                                flag_new_figure_input = False
                                
                                while not(flag_new_figure_input):
                                    new_figure = input("\nВыберете фигуру, которую хотите поставить: \nФерзь - Queen\nКонь - Knight\nCлон - Bishop\nЛадья - Rook\n")

                                    if new_figure == "Queen" or new_figure == "Knight" or new_figure == "Rook" or new_figure == "Bishop":
                                        flag_new_figure_input = True

                                    if flag_new_figure_input is False:
                                        print("Некоректное название фигуры")

                                if new_figure == "Queen":
                                    self.__board[new_row][new_col] = Queen(new_row, new_col, "White")

                                if new_figure == "Knight":
                                    self.__board[new_row][new_col] = Knight(new_row, new_col, "White")

                                if new_figure == "Rook":
                                    self.__board[new_row][new_col] = Rook(new_row, new_col, "White")

                                if new_figure == "Bishop":
                                    self.__board[new_row][new_col] = Bishop(new_row, new_col, "White")
                        elif selected_cell.get_color() == "Black":
                            if new_row == 1:
                                flag_new_figure_input = False
                                
                                while not(flag_new_figure_input):
                                    new_figure = input("\nВыберете фигуру, которую хотите поставить: \nФерзь - Queen\nКонь - Knight\nCлон - Bishop\nЛадья - Rook\n")

                                    if new_figure == "Queen" or new_figure == "Knight" or new_figure == "Rook" or new_figure == "Bishop":
                                        flag_new_figure_input = True

                                    if flag_new_figure_input is False:
                                        print("Некоректное название фигуры")

                                if new_figure == "Queen":
                                    self.__board[new_row][new_col] = Queen(new_row, new_col, "Black")

                                if new_figure == "Knight":
                                    self.__board[new_row][new_col] = Knight(new_row, new_col, "Black")

                                if new_figure == "Rook":
                                    self.__board[new_row][new_col] = Rook(new_row, new_col, "Black")

                                if new_figure == "Bishop":
                                    self.__board[new_row][new_col] = Bishop(new_row, new_col, "Black")
                        else:
                            self.__board[new_row][new_col] = selected_cell

                        self.switch_color_of_current_player()
                else:
                    if new_cell is None:
                        self.__board[current_row][current_col] = None

                        selected_cell.set_row(new_row)
                        selected_cell.set_col(new_col)

                        self.__board[new_row][new_col] = selected_cell

                        self.switch_color_of_current_player()
                    else:
                        flag_moved_correctly = False
            elif selected_cell.get_name_of_figure() == "Knight":
                if new_cell is not None:
                    if new_cell.get_color() == self.get_current_player_color():
                        flag_moved_correctly = False
                    else:
                        self.__board[current_row][current_col] = None

                        selected_cell.set_row(new_row)
                        selected_cell.set_col(new_col)

                        self.__board[new_row][new_col] = selected_cell

                        self.switch_color_of_current_player()
                else:
                    self.__board[current_row][current_col] = None

                    selected_cell.set_row(new_row)
                    selected_cell.set_col(new_col)

                    self.__board[new_row][new_col] = selected_cell

                    self.switch_color_of_current_player()
            elif selected_cell.get_name_of_figure() == "Rook":
                if new_cell is not None:
                    if new_cell.get_color() == self.get_current_player_color():
                        flag_moved_correctly = False
                    else:
                        if current_col != new_col:
                            flag_no_figures_on_cols = True

                            for col in range (current_col, new_col, self.direction_of_move(current_col, new_col)):
                                if col == current_col:
                                    pass
                                elif self.__board[current_row][col] is not None:
                                    flag_no_figures_on_cols = False
                                
                            if flag_no_figures_on_cols is False:
                                flag_moved_correctly = False
                            else:
                                self.__board[current_row][current_col] = None

                                selected_cell.set_row(new_row)
                                selected_cell.set_col(new_col)

                                self.__board[new_row][new_col] = selected_cell
                
                                self.switch_color_of_current_player()

                        if current_row != new_row:
                            flag_no_figures_on_cols = True
                            
                            for row in range (current_row, new_row, self.direction_of_move(current_row, new_row)):
                                if row == current_col:
                                    pass
                                elif self.__board[row][current_col] is not None:
                                    flag_no_figures_on_cols = False
                                
                            if flag_no_figures_on_cols is False:
                                flag_moved_correctly = False
                            else:
                                self.__board[current_row][current_col] = None

                                selected_cell.set_row(new_row)
                                selected_cell.set_col(new_col)

                                self.__board[new_row][new_col] = selected_cell
                
                                self.switch_color_of_current_player()
                else:
                    if current_col != new_col:
                        flag_no_figures_on_cols = True

                        for col in range (current_col, new_col, self.direction_of_move(current_col, new_col)):
                            if col == current_col:
                                    pass
                            elif self.__board[current_row][col] is not None:
                                flag_no_figures_on_cols = False
                                
                        if flag_no_figures_on_cols is False:
                            flag_moved_correctly = False
                        else:
                            self.__board[current_row][current_col] = None

                            selected_cell.set_row(new_row)
                            selected_cell.set_col(new_col)

                            self.__board[new_row][new_col] = selected_cell
                
                            self.switch_color_of_current_player()

                    if current_row != new_row:
                        flag_no_figures_on_cols = True

                        for row in range (current_row, new_row, self.direction_of_move(current_row, new_row)):
                            if row == current_col:
                                    pass
                            elif self.__board[row][current_col] is not None:
                                flag_no_figures_on_cols = False
                                
                        if flag_no_figures_on_cols is False:
                            flag_moved_correctly = False
                        else:
                            self.__board[current_row][current_col] = None

                            selected_cell.set_row(new_row)
                            selected_cell.set_col(new_col)

                            self.__board[new_row][new_col] = selected_cell
                
                            self.switch_color_of_current_player()
            
            elif selected_cell.get_name_of_figure() == "Bishop":
                direction_cols = self.direction_of_move(current_col, new_col)
                direction_rows = self.direction_of_move(current_row, new_row)

                if new_cell is not None:
                    if new_cell.get_color() == self.get_current_player_color():
                        flag_moved_correctly = False
                    else:
                        flag_no_figures_on_cells = True

                        for bias in range(1, abs(current_col-new_col)):
                            if self.__board[current_row + bias * direction_rows][current_col + bias * direction_cols] is not None:
                                flag_no_figures_on_cells = False
                        
                        if flag_no_figures_on_cells is False:
                            flag_moved_correctly = False
                        else:
                            self.__board[current_row][current_col] = None

                            selected_cell.set_row(new_row)
                            selected_cell.set_col(new_col)

                            self.__board[new_row][new_col] = selected_cell
                
                            self.switch_color_of_current_player()
                else:
                    flag_no_figures_on_cells = True

                    for bias in range(1, abs(current_col-new_col)):
                        if self.__board[current_row + bias * direction_rows][current_col + bias * direction_cols] is not None:
                            flag_no_figures_on_cells = False
                        
                    if flag_no_figures_on_cells is False:
                        flag_moved_correctly = False
                    else:
                        self.__board[current_row][current_col] = None

                        selected_cell.set_row(new_row)
                        selected_cell.set_col(new_col)

                        self.__board[new_row][new_col] = selected_cell
                
                        self.switch_color_of_current_player()
            elif selected_cell.get_name_of_figure() == "Queen":
                
                if current_col != new_col and current_row != new_row:
                    direction_cols = self.direction_of_move(current_col, new_col)
                    direction_rows = self.direction_of_move(current_row, new_row)

                    if new_cell is not None:
                        if new_cell.get_color() == self.get_current_player_color():
                            flag_moved_correctly = False
                        else:
                            flag_no_figures_on_cells = True

                            for bias in range(1, abs(current_col-new_col)):
                                if self.__board[current_row + bias * direction_rows][current_col + bias * direction_cols] is not None:
                                    flag_no_figures_on_cells = False
                        
                            if flag_no_figures_on_cells is False:
                                flag_moved_correctly = False
                            else:
                                self.__board[current_row][current_col] = None

                                selected_cell.set_row(new_row)
                                selected_cell.set_col(new_col)

                                self.__board[new_row][new_col] = selected_cell
                
                                self.switch_color_of_current_player()
                    else:
                        flag_no_figures_on_cells = True

                        for bias in range(1, abs(current_col-new_col)):
                            if self.__board[current_row + bias * direction_rows][current_col + bias * direction_cols] is not None:
                                flag_no_figures_on_cells = False
                        
                        if flag_no_figures_on_cells is False:
                            flag_moved_correctly = False
                        else:
                            self.__board[current_row][current_col] = None

                            selected_cell.set_row(new_row)
                            selected_cell.set_col(new_col)

                            self.__board[new_row][new_col] = selected_cell
                
                            self.switch_color_of_current_player()
                else:
                    if new_cell is not None:
                        if new_cell.get_color() == self.get_current_player_color():
                            flag_moved_correctly = False
                        else:
                            if current_col != new_col:
                                flag_no_figures_on_cols = True

                                for col in range (current_col, new_col, self.direction_of_move(current_col, new_col)):
                                    if col == current_col:
                                        pass
                                    elif self.__board[current_row][col] is not None:
                                        flag_no_figures_on_cols = False
                                
                                if flag_no_figures_on_cols is False:
                                    flag_moved_correctly = False
                                else:
                                    self.__board[current_row][current_col] = None

                                    selected_cell.set_row(new_row)
                                    selected_cell.set_col(new_col)

                                    self.__board[new_row][new_col] = selected_cell
                
                                    self.switch_color_of_current_player()

                            if current_row != new_row:
                                flag_no_figures_on_cols = True
                            
                                for row in range (current_row, new_row, self.direction_of_move(current_row, new_row)):
                                    if row == current_col:
                                        pass
                                    elif self.__board[row][current_col] is not None:
                                        flag_no_figures_on_cols = False
                                
                                if flag_no_figures_on_cols is False:
                                    flag_moved_correctly = False
                                else:
                                    self.__board[current_row][current_col] = None

                                    selected_cell.set_row(new_row)
                                    selected_cell.set_col(new_col)

                                    self.__board[new_row][new_col] = selected_cell
                
                                    self.switch_color_of_current_player()
                    else:
                        if current_col != new_col:
                            flag_no_figures_on_cols = True

                            for col in range (current_col, new_col, self.direction_of_move(current_col, new_col)):
                                if col == current_col:
                                    pass
                                elif self.__board[current_row][col] is not None:
                                    flag_no_figures_on_cols = False
                                
                            if flag_no_figures_on_cols is False:
                                flag_moved_correctly = False
                            else:
                                self.__board[current_row][current_col] = None

                                selected_cell.set_row(new_row)
                                selected_cell.set_col(new_col)

                                self.__board[new_row][new_col] = selected_cell
                
                                self.switch_color_of_current_player()

                        if current_row != new_row:
                            flag_no_figures_on_cols = True

                            for row in range (current_row, new_row, self.direction_of_move(current_row, new_row)):
                                if row == current_col:
                                    pass
                                elif self.__board[row][current_col] is not None:
                                    flag_no_figures_on_cols = False
                                
                            if flag_no_figures_on_cols is False:
                                flag_moved_correctly = False
                            else:
                                self.__board[current_row][current_col] = None

                                selected_cell.set_row(new_row)
                                selected_cell.set_col(new_col)

                                self.__board[new_row][new_col] = selected_cell
                
                                self.switch_color_of_current_player()
            elif selected_cell.selected_cell.get_name_of_figure() == "King":
                if self.get_current_player_color() == "White":
                    opponent_color = "Black"
                else:
                    opponent_color = "White"
                if new_cell is not None:
                    if new_cell.get_color() == self.get_current_player_color():
                        flag_moved_correctly = False
                    else:
                        if self.is_under_atack(new_row, new_col, opponent_color):
                            flag_moved_correctly = False
                        else:
                            self.__board[current_row][current_col] = None

                            selected_cell.set_row(new_row)
                            selected_cell.set_col(new_col)

                            self.__board[new_row][new_col] = selected_cell

                            self.switch_color_of_current_player()
                else:
                    if self.is_under_atack(new_row, new_col, opponent_color):
                        flag_moved_correctly = False
                    else:
                        self.__board[current_row][current_col] = None

                        selected_cell.set_row(new_row)
                        selected_cell.set_col(new_col)

                        self.__board[new_row][new_col] = selected_cell

                        self.switch_color_of_current_player()



        return flag_moved_correctly
