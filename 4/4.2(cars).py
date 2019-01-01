import numpy as np


DEFAULT_CAR_TYPES = {
    "Легковой": 0,
    "Пассажирский": 1,
    "Грузовой": 2,
}

CAR_TYPE_NUMBER = {
    0: "Легковой",
    1: "Пассажирский",
    2: "Грузовой",
}


def nonlin(x, deriv=False):
    return x * (1 - x) if deriv else 1 / (1 + np.exp(-x))


# reading data
all_cars_data = []
with open("cars_learn.txt", "r") as file:
    for i in file:
        splat_car_data = i.split(",")
        car_data = dict()
        car_data["Name"] = splat_car_data[0]
        car_data["Weight"] = float(splat_car_data[1])
        car_data["Engine"] = float(splat_car_data[2])
        car_data["Passengers"] = float(splat_car_data[3])
        car_data["Capacity"] = float(splat_car_data[4][:-1])
        all_cars_data.append(car_data)

all_cars_classification = []
with open("cars_expected_result.txt", "r") as file:
    for i in file:
        splat_car_result = i.split("-")
        car_data = dict()
        car_data["Name"] = splat_car_result[0]
        car_data["Class"] = splat_car_result[1][:-1]
        all_cars_classification.append(car_data)

# parsing data into arrays
x = np.array(tuple(all_cars_data[0].values())[1:])

for i in range(1, len(all_cars_data)):
    x = np.vstack([x, tuple(all_cars_data[i].values())[1:]])

y = np.array(DEFAULT_CAR_TYPES[all_cars_classification[0]["Class"]])

for i in range(1, len(all_cars_classification)):
    y = np.vstack([y, DEFAULT_CAR_TYPES[all_cars_classification[i]["Class"]]])

y = y / 2
x = x / 300

np.random.seed(1)

# случайно инициализируем веса, в среднем - 0
syn0 = 2 * np.random.random((4, 16)) - 1
syn1 = 2 * np.random.random((16, 7)) - 1
syn2 = 2 * np.random.random((7, 1)) - 1


for i in range(50000):
    l0 = x
    l1 = nonlin(np.dot(l0, syn0))
    l2 = nonlin(np.dot(l1, syn1))
    l3 = nonlin(np.dot(l2, syn2))
    l3_error = y - l3
    l3_delta = l3_error * nonlin(l3, deriv=True)
    l2_error = np.dot(l3_delta, syn2.T)
    l2_delta = l2_error * nonlin(l2, deriv=True)
    l1_error = np.dot(l2_delta, syn1.T)
    l1_delta = l1_error * nonlin(l1, deriv=True)
    syn0 += np.dot(l0.T, l1_delta)
    syn1 += np.dot(l1.T, l2_delta)
    syn2 += np.dot(l2.T, l3_delta)
    if i % 10000 == 0:
        print("Error:", str(np.mean(np.abs(l1_error))))

# reading data
all_cars_data = []
with open("car_test_data.txt", "r") as file:
    for i in file:
        splat_car_data = i.split(",")
        car_data = dict()
        car_data["Name"] = splat_car_data[0]
        car_data["Weight"] = float(splat_car_data[1])
        car_data["Engine"] = float(splat_car_data[2])
        car_data["Passengers"] = float(splat_car_data[3])
        car_data["Capacity"] = float(splat_car_data[4][:-1])
        all_cars_data.append(car_data)

all_cars_classification = []
with open("car_test_result.txt", "r") as file:
    for i in file:
        splat_car_result = i.split("-")
        car_data = dict()
        car_data["Name"] = splat_car_result[0]
        car_data["Class"] = splat_car_result[1][:-1]
        all_cars_classification.append(car_data)

x = np.array(tuple(all_cars_data[0].values())[1:])

for i in range(1, len(all_cars_data)):
    x = np.vstack([x, tuple(all_cars_data[i].values())[1:]])

y = np.array(DEFAULT_CAR_TYPES[all_cars_classification[0]["Class"]])

for i in range(1, len(all_cars_classification)):
    y = np.vstack([y, DEFAULT_CAR_TYPES[all_cars_classification[i]["Class"]]])

y = y / 2
x = x / 300

l0 = x
l1 = nonlin(np.dot(l0, syn0)) / 2
l2 = nonlin(np.dot(l1, syn1)) / 2
l3 = nonlin(np.dot(l2, syn2)) / 2
l3 = l3 * 2

result = []
for i in l3:
    a = round(np.asscalar(i * 2))
    result.append(a)

for i in range(len(all_cars_data)):
    print(all_cars_data[i]["Name"], "-", CAR_TYPE_NUMBER[result[i]])