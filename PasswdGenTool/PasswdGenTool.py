import random


class PasswdGenTool:
    def __init__(self, characters):
        self.chars = characters

    def gen(self, long=16):
        str = ""
        for x in range(long):
            str += random.choice(self.chars)
        return str


if __name__ == "__main__":
    chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
             "s", "t", "u", "v", "w", "x", "y", "z",
             "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
             "S", "T", "U", "V", "W", "X", "Y", "Z",
             "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    # chars.extend(["-", "_", "@", "!", "#", "$", "%", "&", "(", ")", "[", "]", "{", "}"])

    # chars.extend(["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "-", "="])

    calc = PasswdGenTool(chars)

    for x in range(1):
        print(calc.gen(16))
