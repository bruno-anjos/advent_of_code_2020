package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

const (
	inputFilename = "input.txt"
)

var (
	numbersMap map[int64]interface{}
)

func main() {
	mapInput()

	partOne()
	partTwo()
}

func partOne() {
	var (
		solv1, solv2, remaining int64
	)

	for attempt1 := range numbersMap {
		remaining = 2020 - attempt1
		if _, ok := numbersMap[remaining]; ok {
			fmt.Printf("Found: %d + %d = 2020\n", attempt1, remaining)
			solv1 = attempt1
			solv2 = remaining
			break
		}
	}

	fmt.Printf("Result: %d\n", solv1*solv2)
}

func partTwo() {
	var (
		solv1, solv2, solv3, remaining int64
	)
out:
	for attempt1 := range numbersMap {
		for attempt2 := range numbersMap {
			remaining = 2020 - (attempt1 + attempt2)
			if _, ok := numbersMap[remaining]; ok {
				fmt.Printf("Found: %d + %d + %d = 2020\n", attempt1, attempt2, remaining)
				solv1 = attempt1
				solv2 = attempt2
				solv3 = remaining
				break out
			}
		}
	}

	fmt.Printf("Result: %d\n", solv1*solv2*solv3)
}

func mapInput() {
	data, err := ioutil.ReadFile(inputFilename)
	if err != nil {
		panic(err)
	}

	numbersMap = map[int64]interface{}{}

	numberStrings := strings.Split(string(data), "\n")
	for _, numberString := range numberStrings {
		number, err := strconv.ParseInt(strings.TrimSpace(numberString), 10, 0)
		if err != nil {
			panic(err)
		}

		numbersMap[number] = nil
	}
}
