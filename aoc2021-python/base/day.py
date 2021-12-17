class Day:
    problem_all = 0
    problem_one_number = 1
    problem_two_number = 2

    def __init__(self, day):
        self.day = day

    def problem_one(self, data):
        raise NotImplemented(f"day {self.day} problem {self.problem_one_number}; not implemented ")

    def problem_two(self, data):
        raise NotImplemented(f"day {self.day} problem {self.problem_two_number}; not implemented ")
