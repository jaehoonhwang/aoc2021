from absl import app, flags
from base.day import Day

from day4.day4 import Day4
from day5.day5 import Day5
from day6.day6 import Day6
from day7.day7 import Day7
from day8.day8 import Day8

FLAGS = flags.FLAGS
flags.DEFINE_integer("day", 7, "aoc2021 day", lower_bound=4, upper_bound=7)
flags.DEFINE_integer("problem", 0, "problem", lower_bound=0, upper_bound=2)
flags.DEFINE_string("data", "problem", "example or problem")

problems = {
    4: Day4(4),
    5: Day5(5),
    6: Day6(6),
    7: Day7(7),
    8: Day8(8),
}


def main(argv):
    del argv
    day = FLAGS.day
    problem = FLAGS.problem
    data = FLAGS.data
    if data not in ["example", "problem"]:
        raise NotImplementedError(f"can't use {data} in --data")

    print(f"AOC 2021; Day {day} - data: {data}")

    current = problems[day]

    if problem == Day.problem_one or problem == Day.problem_all:
        print(f"AOC 2021; Day {day} : Problem {Day.problem_one_number}")
        print(f"answer {current.problem_one(data)}")
    if problem == Day.problem_two or problem == Day.problem_all:
        print(f"AOC 2021; Day {day} : Problem {Day.problem_two_number}")
        print(f"answer {current.problem_two(data)}")


if __name__ == "__main__":
    app.run(main)
