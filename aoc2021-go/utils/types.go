package utils

import (
	"fmt"
)

const (
	DAY_BOUND_MIN = 3
	DAY_BOUND_MAX = 5
)

type ProblemDay int8
type ProblemNumber int8
type ProblemType int8

type Solution interface {
	example() string
	problem() string
}

const (
	TypeDefault ProblemType = iota
	TypeExample
	TypeActual
	TypeAll
)

type Problem struct {
	Day          ProblemDay
	Number       ProblemNumber
	Problem_type ProblemType
}

func ValidateProblem(aocProblem *Problem) error {
	if DAY_BOUND_MIN > aocProblem.Day || aocProblem.Day > DAY_BOUND_MAX {
		return fmt.Errorf("Day, %d, has to be between %d <= day <= %d",
			aocProblem.Day, DAY_BOUND_MIN, DAY_BOUND_MAX)
	}

	if TypeDefault >= aocProblem.Problem_type || aocProblem.Problem_type > TypeAll {
		return fmt.Errorf("Type, %d, has to be between %d < type <= %d",
			aocProblem.Problem_type, TypeDefault, TypeAll)
	}

	return nil
}

func (p Problem) String() string {
	return fmt.Sprintf("Day: %d, Number; %d, Type: %d", p.Day, p.Number, p.Problem_type)
}
