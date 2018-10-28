
def main():
    a = list(range(10))
    print("question a")
    print(a)
    print("")

    code = ("ISL", "GBR", "ITA", "EGY", "JPN")
    name = ("アイスランド", "イギリス", "イタリア", "エジプト", "日本")

    dict = {}
    for i in range(5):
        dict[code[i]] = name[i]
    print("question b")
    print(dict)

if __name__ == '__main__':
    main()
