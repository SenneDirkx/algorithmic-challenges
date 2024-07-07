package main

import (
	"fmt"
)

func main() {
	// test
	fmt.Printf(toLowerCase("Hello There!") + "\n")
}

func toLowerCase(str string) string {
	str2 := ""

	for _, char := range str {
		if int(char) < 91 && int(char) >= 65 {
			str2 = str2 + string(int(char)+32)
		} else {
			str2 = str2 + string(char)
		}
	}

	return str2
}

// Runtime: 0 ms (faster than 100% of online Go submissions)
// Memory Usage: 1.9 MB (less than 40% of online Go submissions)
