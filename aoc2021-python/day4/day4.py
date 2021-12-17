from base.day import Day
from utils.file_reader import read_file

class Day4(Day):
    data_source = {
        "example": "day4/data/example.txt",
        "problem": "day4/data/problem.txt",
    }

    def __init__(self, day):
        super().__init__(day)
        self.path = ""

    def problem_one(self, data):
        self.path = self.data_source[data]
        number_draw, boards = self.prettify_data()
        draws = []
        winning_board = None
        for draw in number_draw:
            draws.append(draw)
            for board in boards:
                if self.check_board(board, draws):
                    winning_board = board
                    break
            if winning_board: break

        return self.calculate(winning_board, draws)

    def problem_two(self, data):
        self.path = self.data_source[data]
        number_draw, boards = self.prettify_data()
        draws = []
        count = len(boards)
        skip_list = []
        last = None
        for draw in number_draw:
            draws.append(draw)
            for i, board in enumerate(boards):
                if i not in skip_list and self.check_board(board, draws):
                    skip_list.append(i)
                if len(skip_list) == count:
                    last = board
                    break
            if last: break

        return self.calculate(last, draws)

    def calculate(self, board, marks):
        print(f"board: {board}")
        print(f"marks: {marks}")
        winning_number = marks[-1]
        remaining_number = sum([sum([x for x in row if x not in marks]) for row in board])
        print(f"winning_number: {winning_number} & remaining_number: {remaining_number}")
        return winning_number * remaining_number

    def check_board(self, board, numbers):
        def horizontal(row):
            for number in board[row]:
                if number not in numbers: return False
            return True
        def vertical(column):
            for row in range(5):
                number = board[row][column]
                if number not in numbers: return False
            return True
        def slash():
            for i in range(5):
                number = board[i][i]
                if number not in numbers: return False
            return True
        def back_slash():
            for i in range(5):
                number = board[i][4-i]
                if number not in numbers: return False
            return True

        for i in range(5):
            if horizontal(i): return True
            if vertical(i): return True

        return False # slash() or back_slash()

    def prettify_data(self):
        lines = read_file(self.path)
        number_draw = [int(x) for x in lines[0].split(",")]
        boards = []
        current = []
        for line in lines[2:]:
            line = line.rstrip()
            if line == "":
                boards.append(current)
                current = []
            else:
                current.append([int(x) for x in line.split()])
        boards.append(current)
        return number_draw, boards


