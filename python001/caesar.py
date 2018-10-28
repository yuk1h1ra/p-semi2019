def caesar(string):
    sentence = string
    for i in range(26):
        new_char = ""
        for char in sentence:
            if char == ' ':
                new_char += char
            else:
                if char == "Z":
                    new_char += "A"
                elif char == "z":
                    new_char += "a"
                else:
                    new_char += chr(ord(char) + 1)
        sentence = new_char
        print(str(i+1) + ": " + new_char)



def main():
    a = "jrypbzr vfy yno"
    b = "Nghfb Vabzngn"
    c = "Znkxk oy grcgey romnz hknotj znk iruajy"

    caesar(a)
    caesar(b)
    caesar(c)


if __name__ == '__main__':
    main()
