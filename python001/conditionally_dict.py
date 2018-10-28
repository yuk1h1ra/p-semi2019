
def main():
    list = ['apricot', 'strawberry', 'fig', 'orange', 'persimmon', 'cantaloupe', 'kiwifruits', 'guava', 'cranberry',
             'grapefruit', 'cherry', 'pomegranate', 'watermelon', 'plum', 'gooseberry', 'dragon fruits', 'pear',
             'pineapple', 'passion fruit', 'banana', 'papaya', 'grape', 'blackberry', 'blueberry', 'mango', 'melon',
             'peach', 'raspberry', 'apple', 'lychee', 'lime', 'lemon', ]

    list.sort()

    fruits_dict = {}

    initial = ""
    for fruits in list:
        if fruits[0] == initial:
            fruits_dict[initial].append(fruits)
        else:
            initial = fruits[0]
            fruits_dict[initial] = [fruits]

    print(fruits_dict)

        

if __name__ == '__main__':
    main()
