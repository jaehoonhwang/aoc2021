from base.day import Day
from utils.file_reader import read_file

class Day6(Day):
    data_source = {
        "example": "day6/data/example.txt",
        "problem": "day6/data/problem.txt",
    }

    NEW = 8
    REVIVE = 6

    def __init__(self, day):
        super().__init__(day)
        self.path = ""

    def problem_one(self, data):
        self.path = self.data_source[data]
        sequences = self.mapperify(self.prettify_data())
        for _ in range(80):
            sequences = self.simulate(sequences)

        return self.calculate(sequences)

    def problem_two(self, data):
        self.path = self.data_source[data]
        sequences = self.mapperify(self.prettify_data())
        for _ in range(256):
            sequences = self.simulate(sequences)

        return self.calculate(sequences)

    def calculate(self, mappers):
        return sum([value for _, value in mappers.items()])

    def mapperify(self, sequences):
        ret = {}
        for number in sequences:
            ret[number] = ret.get(number, 0) + 1
        return ret

    def simulate(self, mapper):
        for life in range(self.NEW+1):
            mapper[life-1] = mapper.get(life, 0)

        mapper[self.NEW] = mapper.get(-1, 0)
        mapper[self.REVIVE] += mapper.get(-1, 0)

        del mapper[-1]
        return mapper

    def prettify_data(self):
        lines = read_file(self.path)
        sequences = [int (x) for x in lines[0].split(",")]

        return sequences

