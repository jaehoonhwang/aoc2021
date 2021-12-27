from base.day import Day
from utils.file_reader import read_file


class Day7(Day):
    FILE_DELIMITER = ","
    data_source = {
        "example": "day7/data/example.txt",
        "problem": "day7/data/problem.txt",
    }

    def __init__(self, day):
        super().__init__(day)
        self.path = ""

    def problem_one(self, data):
        self.path = self.data_source[data]
        numbers = self.prettify_data()
        mm, mx = min(numbers), max(numbers)
        local_minima = float('inf')
        for target in range(mm, mx+1):
            local_minima = min(local_minima, self.calculate(numbers, target))
        return local_minima

    def problem_two(self, data):
        self.path = self.data_source[data]
        numbers = self.prettify_data()
        numbers = self.prettify_data()
        mm, mx = min(numbers), max(numbers)
        local_minima = float('inf')
        for target in range(mm, mx+1):
            local_minima = min(local_minima, self.calculate_complex(numbers, target))
        return local_minima

    def calculate(self, numbers, target_number):
        return sum([abs(target_number - number) for number in numbers])

    def calculate_complex(self, numbers, target_number):
        def calculate_difference(num1, num2):
            difference = abs(num2 - num1)
            return (difference * (difference+1)) // 2
        return sum([calculate_difference(number, target_number) for number in numbers])

    def prettify_data(self):
        lines = read_file(self.path)
        return [int(x) for x in lines[0].split(self.FILE_DELIMITER)]
