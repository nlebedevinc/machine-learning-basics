import sys
from collections import Counter


class Task1c:
    def __init__(self):
        self.x = ""

    def find_last_words_count(self):
        a = (1, [1, 2])
        print(a)
        b = self.x
        # print(b)
        extra = (b,)
        z = a + extra
        print(z)


if __name__ == '__main__':
    my_task = Task1c()
    print("This is task 1c:")
    print("Enter the word combination:")
    my_task.x = input()
    my_task.find_last_words_count()
    input()
    sys.exit(1)

