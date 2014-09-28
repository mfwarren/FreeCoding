#!/usr/bin/env python

#100 doors task on rosetta code

'''
Problem: You have 100 doors in a row that are all initially closed. You make 100
 passes by the doors. The first time through, you visit every door and toggle
 the door (if the door is closed, you open it; if it is open, you close it). The
  second time you only visit every 2nd door (door #2, #4, #6, ...). The third time,
   every 3rd door (door #3, #6, #9, ...), etc, until you only visit the 100th door.

Question: What state are the doors in after the last pass? Which are open, which are closed?
'''

#obvious solution
doors = [False] * 100  # False is closed
for i in xrange(100):
  for j in xrange(i, 100, i+1):
    doors[j] = not doors[j]
  if doors[i]:
    print i+1

#notice that it is all the perfect squares
for i in xrange(1,101):
  x = i ** 0.5
  if x == int(x):
    print i

# as a list comprehension
def myprint(s):
  #can't have statement in list comprehension
  print s
[myprint(i) for i in xrange(1, 101) if (i**0.5).is_integer()]

# same but without print as a function
print '\n'.join([str(i) for i in xrange(1, 101) if (i**0.5).is_integer()])
