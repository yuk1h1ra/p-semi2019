
def main():
    print("input integer")
    try:
        number = int(input())
    except:
        print("not integer")
        exit(1)

    for i in range(2, number):
        if number % i == 0:
            print(str(number) + " is not prime")
            exit(0)

    print(str(number) + " is prime")

if __name__ == '__main__':
    main()
