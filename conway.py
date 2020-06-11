from random import choice as rand
from time import sleep
from sys import argv as sys_args


class Conway:
    __grid = list()
    __size = tuple()
    __time: float

    def __init__(self, rows: int, columns: int, time: float):
        self.__size = (rows, columns)
        self.__seed_grid()
        self.__time = time

    def __seed_grid(self):
        for row in range(self.__size[0]):
            new_row = list()
            for column in range(self.__size[1]):
                new_row.append(rand([True, False]))
            self.__grid.append(new_row)

    @staticmethod
    def __clear_console():
        print()

    def __print_grid(self):
        for row in self.__grid:
            row_print = ""
            for col in row:
                if col:
                    row_print += "* "
                else:
                    row_print += "  "
            print(row_print)

    def __is_alive(self, count: int, x: int, y: int) -> int:
        try:
            if self.__grid[x][y]:
                return count + 1
            else:
                return count
        except:
            return count

    def __alive_count(self, x: int, y: int) -> int:
        count = 0
        count = self.__is_alive(count, x - 1, y - 1)
        count = self.__is_alive(count, x, y - 1)
        count = self.__is_alive(count, x + 1, y - 1)
        count = self.__is_alive(count, x - 1, y)
        count = self.__is_alive(count, x + 1, y)
        count = self.__is_alive(count, x - 1, y + 1)
        count = self.__is_alive(count, x, y + 1)
        count = self.__is_alive(count, x + 1, y + 1)
        return count

    # Any live cell with fewer than two live neighbours dies, as if by underpopulation.
    # Any live cell with two or three live neighbours lives on to the next generation.
    # Any live cell with more than three live neighbours dies, as if by overpopulation.
    # Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
    def __tick(self):
        new_state = list()
        for rowIndex in range(len(self.__grid)):
            row = list()
            for colIndex in range(len(self.__grid[0])):
                cell = self.__grid[rowIndex][colIndex]
                neighbor_alive_count = self.__alive_count(rowIndex, colIndex)
                if cell is True and neighbor_alive_count < 2:
                    row.append(False)
                elif cell is True and (neighbor_alive_count == 2 or neighbor_alive_count == 3):
                    row.append(True)
                elif cell is True and neighbor_alive_count > 3:
                    row.append(False)
                elif cell is False and neighbor_alive_count == 3:
                    row.append(True)
                else:
                    row.append(cell)
            new_state.append(row)
        if self.__grid == new_state:
            exit(0)
        self.__grid = new_state
        Conway.__clear_console()
        self.__print_grid()

    @staticmethod
    def play(rows: int = 5, cols: int = 5, time: float = 0.5):
        game = Conway(rows, cols, time)
        while True:
            game.__tick()
            sleep(game.__time)


if len(sys_args) != 4:
    print('conway.py <rows> <columns> <timout>')
    exit(1)
Conway.play(int(sys_args[1]), int(sys_args[2]), float(sys_args[3]))