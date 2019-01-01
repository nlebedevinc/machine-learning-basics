import sys
import sklearn

filepath = "out.txt"

the_list = [["Nikolay", "Lebedev"], ["James", "Bond"], ["Harry", "Potter"]]

with open(filepath, 'w') as file_handler:
    for i, item in enumerate(the_list):
        file_handler.write("{}\n".format(str(i  + 1) + ") " + item[1] + " " + item[0]))

lines = [line.rstrip('\n') for line in open("input.txt")]

for line in lines:
    try:
        words = line.split()
        buf = list(words[1])
        print (words[0] + " " + buf[0])
    except UnboundLocalError:
        print("Smth wrong")