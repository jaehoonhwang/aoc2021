package day3

import (
	"fmt"
	"github.com/jaehoonhwang/aoc2021/utils"
	"strconv"
)

func get_occurences(index int, binaries []string, take_maximum bool) []string {
	count := 0
	for _, bin := range binaries {
		if string(bin[index]) == "1" {
			count += 1
		} else {
			count -= 1
		}
	}

	target := "0"

	if count > 0 {
		if take_maximum {
			target = "1"
		}
	} else if count < 0 {
		if !take_maximum {
			target = "1"
		}
	} else {
		if take_maximum {
			target = "1"
		}
	}

	new_binaries := []string{}

	for _, bin := range binaries {
		if string(bin[index]) == target {
			new_binaries = append(new_binaries, string(bin))
		}
	}

	return new_binaries
}

/**
 * Binary Diagnostic
 * Find most common and least common (gamma, episilon)
 */

func Problem1(file_path string) string {
	/** return multiplication of gamma and episilon
	 */
	lines, err := parse_files(&file_path)
	if err != nil {
		panic(err)
	}
	binaries := make(map[int]int)

	for _, line := range lines {
		for index, ch := range line {
			_, present := binaries[index]
			if !present {
				binaries[index] = 0
			}
			if string(ch) == "1" {
				binaries[index] += 1
			} else {
				binaries[index] -= 1
			}
		}
	}

	gamma := ""
	episilon := ""

	for index := 0; index < len(binaries); index++ {
		value, _ := binaries[index]
		if value > 0 {
			gamma += "1"
			episilon += "0"
		} else {
			gamma += "0"
			episilon += "1"
		}
	}
	gamma_int, err := strconv.ParseInt(gamma, 2, 64)
	episilon_int, err := strconv.ParseInt(episilon, 2, 64)
	final_value := gamma_int * episilon_int

	return fmt.Sprintf("%d", final_value)
}

func Problem2(file_path string) string {
	/**
	 * Bit criteria:
	 */
	lines, err := parse_files(&file_path)
	if err != nil {
		panic(err)
	}
  co2s := lines
  o2s := lines

	index := 0
	for len(co2s) > 1 {
		co2s = get_occurences(index, co2s, true)
		index += 1
	}

	ind := 0
	for len(o2s) > 1 {
		o2s = get_occurences(ind, o2s, false)
		ind += 1
	}

  fmt.Printf("co2 %v o2 %v\n", co2s, o2s)

	co2_int, err := strconv.ParseInt(co2s[0], 2, 64)
  if err != nil {
    panic(err)
  }
	o2_int, err := strconv.ParseInt(o2s[0], 2, 64)
  if err != nil {
    panic(err)
  }
  fmt.Printf("yeet yeet %d %d\n", co2_int, o2_int)

	return fmt.Sprintf("%d", co2_int * o2_int)
}

func parse_files(file_path *string) ([]string, error) {
	lines, err := utils.ReadAocFile(file_path)
	if err != nil {
		return nil, err
	}
	return lines, nil
}
