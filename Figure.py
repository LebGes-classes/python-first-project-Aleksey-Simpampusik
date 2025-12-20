from abc import *


class Chess_Figure(ABC):
    """Абстрактный класс для описания шахматной фигуры."""

    def __init__(self, row: int = None, col: int = None, color: str = "NA") -> None:
        """Конструктор класса.
        
        Args:
            row: Номер строки фигуры.
            col: Номер столбца фигуры.
            color:  Цвет фигуры.

        """

        self.__row = row
        self.__col = col
        self.__color = color

    def set_col(self, col: int) -> None:
        """Сеттер позиции фигуры.
        
        Args:
            col: Новый номер столбца фигуры.

        """

        self.__col = col
    
    def set_row(self, row: int) -> None:
        """Сеттер позиции фигуры.
        
        Args:
            row: Новый номер строки фигуры.

        """

        self.__row = row

    def set_position(self, color) -> None:
        """Сеттер позиции фигуры.
        
        Args:
            color: Цвет фигуры.

        """

        self.__color = color

    def get_row(self) -> str:
        """Геттер строки фигуры.
        
        Returns:
            Номер строки.

        """ 

        return self.__row
    
    def get_col(self) -> str:
        """Геттер Столбца фигуры.
        
        Returns:
            Столбец строки.

        """ 

        return self.__col
    
    def get_color(self) -> str:
        """Геттер цвета фигуры.
        
        Returns:
            Цвет фигуры.

        """ 

        return self.__color

    @abstractmethod
    def get_name_of_figure():
        """Абстрактный метод для получения названия фигуры."""

        pass

    @abstractmethod
    def where_can_move():
        """Абстрактный метод для определения тогоЮ куда может ходить фигура."""

        pass


class Pawn(Chess_Figure):
        """Класс фигуры пешка."""

        __name_of_figure = "Pawn"

        def get_name_of_figure(self) -> str:
            """Метод для получения названия фигуры."""

            return self.__name_of_figure
        
        def where_can_move(self, new_row: int = None, new_col: int = None) -> bool:
            """Метод для определения того, куда может ходить пешка.
            
            Args:
                new_raw: Новая строка для хода
                new_col: Новый столбец для хода

            Returns:
                flag_new position_is_correct: в зависимости от выполнения условий True или False.

            """
            
            flag_new_position_is_correct = False

            if self.get_color() == "White":
                start_row = 2 # стартовая строка для белой пешки вторая
                direction_of_move = 1 #белые пешки ходят вперед поля
                
            if self.get_color() == "Black":
                start_row = 7 # стартовая строка для черной пешки вторая
                direction_of_move = -1 #черные пешки ходят в обратную сторону поля

            if self.get_row() + direction_of_move == new_row and self.get_col() == new_col:
                flag_new_position_is_correct = True

            if self.get_row() + direction_of_move == new_row and abs(self.get_col() - new_col) == 1:
                flag_new_position_is_correct = True

            if self.get_row() == start_row and (self.get_row() + direction_of_move * 2 == new_row) and self.get_col() == new_col:
                flag_new_position_is_correct = True
            
            return flag_new_position_is_correct
        

class Knight(Chess_Figure):
        """Класс фигуры конь."""

        __name_of_figure = "Knight"

        def get_name_of_figure(self) -> str:
            """Метод для получения названия фигуры."""

            return self.__name_of_figure
        
        def where_can_move(self, new_row: int = None, new_col: int = None) -> bool:
            """Метод для определения того, куда может ходить конь.
            
            Args:
                new_raw: Новая строка для хода
                new_col: Новый столбец для хода

            Returns:
                flag_new position_is_correct: в зависимости от выполнения условий True или False.

            """
            
            flag_new_position_is_correct = False

            if self.get_row() + 1 == new_row and self.get_col() + 2 == new_col:
                flag_new_position_is_correct = True
            elif self.get_row() + 2 == new_row and self.get_col() + 1 == new_col:
                flag_new_position_is_correct = True
            elif self.get_row() + 2 == new_row and self.get_col() -1 == new_col:
                flag_new_position_is_correct = True
            elif self.get_row() + 1 == new_row and self.get_col() -2 == new_col:
                flag_new_position_is_correct = True
            elif self.get_row() - 1 == new_row and self.get_col() + 2 == new_col:
                flag_new_position_is_correct = True
            elif self.get_row() - 2 == new_row and self.get_col() + 1 == new_col:
                flag_new_position_is_correct = True
            elif self.get_row() - 2 == new_row and self.get_col() - 1 == new_col:
                flag_new_position_is_correct = True
            elif self.get_row() - 1 == new_row and self.get_col() - 2 == new_col:
                flag_new_position_is_correct = True
                
            return flag_new_position_is_correct


class Bishop(Chess_Figure):
        """Класс фигуры Слон."""

        __name_of_figure = "Bishop"

        def get_name_of_figure(self) -> str:
            """Метод для получения названия фигуры."""

            return self.__name_of_figure
        
        def where_can_move(self, new_row: int = None, new_col: int = None) -> bool:
            """Метод для определения того, куда может ходить cлон.
            
            Args:
                new_raw: Новая строка для хода
                new_col: Новый столбец для хода

            Returns:
                flag_new position_is_correct: в зависимости от выполнения условий True или False.

            """
            
            flag_new_position_is_correct = False

            if abs(self.get_row() - new_row) == abs(self.get_col() - new_col):
                flag_new_position_is_correct = True
            
            return flag_new_position_is_correct
    

class Rook(Chess_Figure):
        """Класс фигуры ладья."""

        __name_of_figure = "Rook"

        def get_name_of_figure(self) -> str:
            """Метод для получения названия фигуры."""

            return self.__name_of_figure
        
        def where_can_move(self, new_row: int = None, new_col: int = None) -> bool:
            """Метод для определения того, куда может ходить ладья.
            
            Args:
                new_raw: Новая строка для хода
                new_col: Новый столбец для хода

            Returns:
                flag_new position_is_correct: в зависимости от выполнения условий True или False.

            """
            
            flag_new_position_is_correct = True

            if self.get_col() != new_col and self.get_row() != new_row:
                flag_new_position_is_correct = False
                
            return flag_new_position_is_correct
    

class Queen(Chess_Figure):
        """Класс фигуры ферзь."""

        __name_of_figure = "Queen"

        def get_name_of_figure(self) -> str:
            """Метод для получения названия фигуры."""

            return self.__name_of_figure
        
        def where_can_move(self, new_row: int = None, new_col: int = None) -> bool:
            """Метод для определения того, куда может ходить ферзь.
            
            Args:
                new_raw: Новая строка для хода
                new_col: Новый столбец для хода

            Returns:
                flag_new position_is_correct: в зависимости от выполнения условий True или False.

            """
            
            flag_new_position_is_correct = True

            if abs(self.get_row() - new_row) == abs(self.get_col() - new_col):
                flag_new_position_is_correct = True
            elif not(self.get_row() != new_row and self.get_col() != new_col):
                flag_new_position_is_correct = True
            else:
                flag_new_position_is_correct = False
                
            return flag_new_position_is_correct
        

class King(Chess_Figure):
        """Класс фигуры король."""

        __name_of_figure = "King"

        def get_name_of_figure(self) -> str:
            """Метод для получения названия фигуры."""

            return self.__name_of_figure
        
        def where_can_move(self, new_row: int = None, new_col: int = None) -> bool:
            """Метод для определения того, куда может ходить ферзь.
            
            Args:
                new_raw: Новая строка для хода
                new_col: Новый столбец для хода

            Returns:
                flag_new position_is_correct: в зависимости от выполнения условий True или False.

            """
            
            flag_new_position_is_correct = False

            if self.get_row() + 1 == new_row and self.get_col == new_col:
                flag_new_position_is_correct = True
            elif self.get_row() + 1 == new_row and self.get_col() + 1 == new_col:
                flag_new_position_is_correct = True
            elif self.get_col() + 1 == new_col and self.get_row() == new_row:
                flag_new_position_is_correct = True
            elif self.get_col() + 1 == new_col and self.get_row() - 1 == new_row:
                flag_new_position_is_correct = True
            elif self.get_row() - 1 == new_row and self.get_col == new_col:
                flag_new_position_is_correct = True
            elif self.get_row() - 1 == new_row and self.get_col() - 1 == new_col:
                flag_new_position_is_correct = True
            elif self.get_col() - 1 == new_col and self.get_row() == new_row:
                flag_new_position_is_correct = True
            elif self.get_row() + 1 == new_row and self.get_col() - 1 == new_col:
                flag_new_position_is_correct = True
                
            return flag_new_position_is_correct
        