# Exercise - 1

a = 3
b = 4

print(a + b)

print(a - b)

print(a * b)

print(a % b)

print(a / b)

print(a**b)

print(a // b)


# Exercise -2

name = "Sundhara Krishna"
familyName = "SKrishna"
countryName = "India"
occupation = "Foss Dev by Night and Doing Many stuffs by the day"

print(name, familyName, countryName, occupation)

# Exercise - 3

print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 - 4j))

# Exercise - 4
# NOTE: Difference Euclidean Distance in simple python

import math


def euclidean_distance(point1, point2):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(point1, point2)))


point1 = (1, 2)
point2 = (4, 6)
distance = euclidean_distance(point1, point2)
print(distance)
