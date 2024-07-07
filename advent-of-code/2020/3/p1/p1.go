package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"strings"
)

func main() {
	data := readFile()
	splittedData := parseData(data)
	result := solution(splittedData, 3, 1)
	fmt.Println(result)
}

func readFile() string {
	data, err := ioutil.ReadFile("../input.txt")
	if err != nil {
		log.Panicf("failed reading data from file: %s", err)
	}
	return string(data)
}

func parseData(data string) []string {
	return strings.SplitN(data, "\n", -1)
}

func solution(data []string, rightStep int, bottomStep int) int {
	horizontalPosition := rightStep
	verticalPosition := bottomStep
	height := len(data)
	width := len(data[0])
	treeCount := 0

	for verticalPosition < height {
		if data[verticalPosition][horizontalPosition] == '#' {
			treeCount++
		}
		horizontalPosition += rightStep
		if horizontalPosition >= width {
			horizontalPosition -= width
		}
		verticalPosition += bottomStep
	}
	return treeCount
}
