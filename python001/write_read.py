import random 

def main():

    file = open("log.txt", 'w')
    for i in range(1000):
        num = random.randint(-1, 1000)
        file.write(str(num) + "\n")
    file.close()

    file = open("log.txt", 'r')
    string = file.readline()

    while string:
        num = int(string)
        if num % 2 == 0:
            print(str(num) + " is even")
        else:
            print(str(num) + " is odd")
        string = file.readline()

if __name__ == '__main__':
    main()
