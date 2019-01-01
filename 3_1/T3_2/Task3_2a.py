import sys
from collections import Counter


class Task2a:
    def __init__(self):
        self.x = ""


if __name__ == '__main__':
    my_task = Task2a()
    print("This is task 2a:")
    print(len(set(input().split()) & set(input().split())))
    input()
    sys.exit(1)

