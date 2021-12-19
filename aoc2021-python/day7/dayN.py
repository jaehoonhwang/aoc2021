from base.day import Day
from utils.file_reader import read_file

class Day7(Day):
    data_source = {
        "example": "dayN/data/example.txt",
        "problem": "dayN/data/problem.txt",
    }

    def __init__(self, day):
        super().__init__(day)
        self.path = ""

    def problem_one(self, data):
        self.path = data_source[data]

    def problem_two(self, data):
        self.path = data_source[data]

    def calculate(self, board, marks):
        pass

    def prettify_data(self):
        lines = read_file(self.path)
        return lines

