from base.day import Day
from utils.file_reader import read_file

class Day5(Day):
    data_source = {
        "example": "day5/data/example.txt",
        "problem": "day5/data/problem.txt",
    }

    def __init__(self, day):
        super().__init__(day)
        self.path = ""

    def problem_one(self, data):
        self.path = self.data_source[data]
        coords = self.prettify_data()
        marks = {}
        for start, end in coords:
            if self.is_diagonal(start, end):
                # we don't care about diagonal for now :eyes:
                continue
            self.mark_vertical(marks, start, end)
            self.mark_horizontal(marks, start, end)

        return self.calculate(marks)

    def problem_two(self, data):
        self.path = self.data_source[data]
        coords = self.prettify_data()
        marks = {}
        for start, end in coords:
            self.mark_diagonal(marks, start, end)
            self.mark_vertical(marks, start, end)
            self.mark_horizontal(marks, start, end)

        return self.calculate(marks)

    def is_diagonal(self, start, end):
        if start[0] - end[0] != 0 and start[1] - end[1] != 0:
            return True
        return False

    def mark_diagonal(self, marks, start, end):
        start_x, start_y = start
        end_x, end_y = end

        if end_x - start_x == 0:
            return
        if end_y - start_y == 0:
            return
        dx = 1 if end_x - start_x > 0 else -1
        dy = 1 if end_y - start_y > 0 else -1

        current_x, current_y = start_x, start_y
        for _ in range(abs(end_x - start_x)+1):
            if current_x not in marks:
                marks[current_x] = {}
            marks[current_x][current_y] = marks[current_x].get(current_y, 0) + 1
            current_x += dx
            current_y += dy

    def mark_horizontal(self, marks, start, end):
        start_x, start_y = start
        end_x, end_y = end

        if end_y - start_y != 0:
            return

        starting_x = min(start_x, end_x)
        ending_x = max(start_x, end_x)
        for x in range(starting_x, ending_x+1):
            if x not in marks:
                marks[x] = {}
            marks[x][start_y] = marks[x].get(start_y, 0) + 1

    def mark_vertical(self, marks, start, end):
        start_x, start_y = start
        end_x, end_y = end

        if end_x - start_x != 0:
            return

        starting_y = min(start_y, end_y)
        ending_y = max(start_y, end_y)
        for y in range(starting_y, ending_y+1):
            if start_x not in marks:
                marks[start_x] = {}
            marks[start_x][y] = marks[start_x].get(y, 0) + 1


    def calculate(self, marks):
        count = 0
        for k, v in marks.items():
            for _, vv in marks[k].items():
                if vv > 1: count += 1
        return count

    def prettify_data(self):
        lines = read_file(self.path)
        ret = []
        for line in lines:
            l, r = line.split(" -> ")
            left = tuple([int(x) for x in l.split(",")])
            right = tuple([int(x) for x in r.split(",")])
            ret.append([left, right])
        return ret



