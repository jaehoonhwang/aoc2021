package main

import (
	"flag"
	"fmt"

  "github.com/jaehoonhwang/aoc2021/utils"
  "github.com/jaehoonhwang/aoc2021/day3"
)

var dayFlag = flag.Int("day", 3, "aoc day")
var problemFlag = flag.Int("problem", 3, "problem 1 or 2, 3 is all, default 3")
var typeFlag = flag.Int("type", 3, "example 1, actual_problem 2, all 3, default 3")

func main() {
	flag.Parse()
	aocProblem := utils.Problem{
		Day:          utils.ProblemDay(*dayFlag),
		Number:       utils.ProblemNumber(*problemFlag),
		Problem_type: utils.ProblemType(*typeFlag),
	}

	utils.ValidateProblem(&aocProblem)
  fmt.Println("AocProblem: ", utils.Problem(aocProblem))

  fmt.Println(day3.Problem1("day3/data/"+utils.EXMAPLE_FILE_NAME))
  fmt.Println(day3.Problem1("day3/data/"+utils.PROBLEM_FILE_NAME))
  fmt.Println(day3.Problem2("day3/data/"+utils.EXMAPLE_FILE_NAME))
  fmt.Println(day3.Problem2("day3/data/"+utils.PROBLEM_FILE_NAME))
}
