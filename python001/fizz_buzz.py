
def main():
    print("input integer")

    try:
        number = int(input())
    except:
        print("not integer")
        exit(1)

    for i in range(number + 1):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 5 == 0:
            print("fizz")
        elif i % 3 == 0:
            print("buzz")
        else:
            print(i)

if __name__ == '__main__':
    main()
