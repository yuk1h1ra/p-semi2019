import random
import numpy as np

def main():
    numbers = []
    for _ in range(1000):
        num = random.randint(1, 6)
        numbers.append(num)
    numbers = np.array(numbers)

    average = np.mean(numbers)

    center = np.median(numbers)

    count = np.bincount(numbers)
    mode = np.argmax(count)

    std = np.std(numbers)

    print("平均：" + str(average))
    print("中央値：" + str(center))
    print("最頻値：" + str(mode))
    print("標準偏差：" + str(std))

if __name__ == '__main__':
    main()
