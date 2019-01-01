import sys
from collections import Counter


class Task1c:
    def __init__(self):
        self.x = ""

    @staticmethod
    def find_last_words_count():
        a = (1, [1, 2])
        print(a)
        b = (1, [1, 2])
        print(b)
        a[1] = b
        print(a)


if __name__ == '__main__':
    my_task = Task1c()
    print("This is task 1c:")
    print("Enter the word combination:")
    my_task.x = input()
    my_task.find_last_words_count()
    input()
    sys.exit(1)

