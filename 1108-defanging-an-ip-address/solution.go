package main

func main() {
	defangIPaddr("1.1.1.1")
}

func defangIPaddr(address string) string {
	newAddress := ""
	for i := 0; i < len(address); i++ {
		if string(address[i]) == "." {
			newAddress = newAddress + "[.]"
		} else {
			newAddress = newAddress + string(address[i])
		}
	}
	return newAddress
}

// Runtime: 0 ms (faster than 100% of online Go submissions)
// Memory Usage: 1.9 MB (less than 100% of online Go submissions)
