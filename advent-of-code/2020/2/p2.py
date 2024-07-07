class Password:
    def __init__(self, splitted_input):
        self.low = int(splitted_input[0][0][0])
        self.high = int(splitted_input[0][0][1])
        self.char = splitted_input[0][1]
        self.password = splitted_input[1]
    
    def is_valid(self):
        return not (self.password[self.low-1] == self.char and self.password[self.high-1] == self.char) and not (self.password[self.low-1] != self.char and self.password[self.high-1] != self.char)

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