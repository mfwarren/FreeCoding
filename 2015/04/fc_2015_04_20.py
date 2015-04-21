#!/usr/bin/env python3
# imports go here

#
# Free Coding session for 2015-04-20
# Written by Matt Warren
#


x = 4

a = [1,2,3,4,5,6,7,8,9]
for i in range(a.count(x)):
    a.pop(a.index(x))

print(a)


a = [1, 2, 3, 4, 4, 5, 6, 1, 4]
b = [v for v in a if v != x]
print(b)

b = list(set(a))
print(b)

b = a.pop(0)
print(b)
print(a)

del a[0]
print(a)

b = a[1:]
print(b)



del a[4]

n = 2
a = [1, 2, 3, 4, 5, 6]
c = [v for i, v in enumerate(a) if i != n - 1]


c = [v if v != 3 else None for v in a]

b = sorted(a, key=lambda x: -x)
print(b)
b = sorted(a, reverse=True)
print(b)

a.sort()
print(a)

b = sum(a)
print(b)
a.append(22)
print(sum(a))

def square(x):
    return x**2

b = list(map(square, a))
print(b)
print(a)
