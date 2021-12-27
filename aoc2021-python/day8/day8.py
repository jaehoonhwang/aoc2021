from base.day import Day
from utils.file_reader import read_file


class Day8(Day):
    data_source = {
        "example": "day8/data/example.txt",
        "problem": "day8/data/problem.txt",
    }

    def __init__(self, day):
        super().__init__(day)
        self.path = ""

    def problem_one(self, data):
        self.path = self.data_source[data]

    def problem_two(self, data):
        self.path = self.data_source[data]

    def calculate(self, board, marks):
        pass

    def prettify_data(self):
        lines = read_file(self.path)
        return lines
