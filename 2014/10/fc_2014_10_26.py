#!/usr/bin/env python
#imports go here
import random
from collections import defaultdict, deque
import heapq

#
# Free Coding session for 2014-10-26
# Written by Matt Warren
#

DIMENSIONS = 10

def print_matrix(matrix):
    for row in matrix:
        print row

matrix = [[0 for x in xrange(DIMENSIONS)] for x in xrange(DIMENSIONS)]
bad_matrix = [[0]*DIMENSIONS]*DIMENSIONS  # links to the same objects

bad_matrix[0][0] = 2
print bad_matrix

# create identity matrix
for i in xrange(10):
    for j in xrange(10):
        if i == j:
            matrix[i][j] = 1

#print identity matrix
print_matrix(matrix)

# create random matrix
for i in xrange(DIMENSIONS):
    for j in xrange(DIMENSIONS):
        matrix[i][j] = random.randint(0,100)

print_matrix(matrix)


# create a random graph

verticies = [c for c in 'abcdefghijk']
G = defaultdict(dict)

# create random edge weights
for v in verticies:
    for v2 in verticies:
        if random.randint(0,100) < 50:
            # graph is 50% connected on avg
            weight = random.randint(1,20)
            G[v][v2] = weight
print G

def shortest_path(G, start, end):
    q = [(0, start, deque())]
    visited = set()
    while True:
        (cost, v1, path) = heapq.heappop(q)
        if v1 not in visited:
            visited.add(v1)
            if v1 == end:
                path.append(v1)
                return list(path), cost
            path = deque(path) # create a copy of the path
            path.append(v1)
            for (v2, cost2) in G[v1].iteritems():
                if v2 not in visited:
                    heapq.heappush(q, (cost+cost2, v2, path))

print shortest_path(G, 'a', 'k')
