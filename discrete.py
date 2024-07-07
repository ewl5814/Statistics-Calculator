import sys
import math

def main() -> None:
    num = input("Enter num: ")

    func(int(num))

def func(num: int):
    print("+")
    if (num > 100):
        print(str(num - 10))
        return num - 10
    else:
        print(str(num + 11))
        return func(func(num + 11))








if __name__ == '__main__':
    main()
