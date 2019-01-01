try:
    x1 = float(input())
    y1 = float(input())
    x2 = float(input())
    y2 = float(input())
    print("Unsuccessful typification")
except ValueError as e:
    print("Unsuccessful typification: __ ", e)
except ZeroDivisionError:
    print("Trying to devide by zero")
except Exception:
    print("Common exception")
def distance(x1, y1, x2, y2):
    return (((x2-x1)**2 + (y2-y1)**2) ** 0.5)
print (distance(x1, y1, x2, y2))