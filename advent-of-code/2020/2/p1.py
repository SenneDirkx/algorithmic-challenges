class Password:
    def __init__(self, splitted_input):
        self.low = int(splitted_input[0][0][0])
        self.high = int(splitted_input[0][0][1])
        self.char = splitted_input[0][1]
        self.password = splitted_input[1]
    
    def is_valid(self):
        count = 0
        for char in self.password:
            if char == self.char:
                count += 1
        
        return self.low <= count and count <= self.high

def main():
    passwords = []

    with open('./input.txt') as inputfile:
        for line in inputfile:
            line = line.strip().split(": ")
            line[0] = line[0].split(" ")
            line[0][0] = line[0][0].split("-")
            passwords.append(Password(line))

    result = 0

    for password in passwords:
        if password.is_valid():
            result += 1

    return result

print(main())