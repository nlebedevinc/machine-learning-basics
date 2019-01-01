import sys
from collections import Counter


class Task1b:
    def __init__(self):
        self.x = 0

    def find_last_words_count(self):
        a = (1, [1, 2])
        print(a)
        b = [1, 2, 3]
        print(b)
        extra = (b,)
        z = a + extra
        print(z)


if __name__ == '__main__':
    my_task = Task1b()
    print("This is task 1b:")
    # print("Enter the word combination:")
    # my_task.x = int(input())
    my_task.find_last_words_count()
    input()
    sys.exit(1)

