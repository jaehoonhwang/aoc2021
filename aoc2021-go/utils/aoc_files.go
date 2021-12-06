package utils

import (
	"bufio"
	"os"
)

const (
	EXMAPLE_FILE_NAME string = "example.txt"
	PROBLEM_FILE_NAME string = "problem.txt"
)

func ReadAocFile(file_path *string) ([]string, error) {
	lines := make([]string, 0)
	file, err := os.Open(*file_path)
	if err != nil {
		return lines, err
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	if err := scanner.Err(); err != nil {
		return lines, err
	}

	return lines, nil
}
