#!/usr/bin/env python3
# imports go here
from collections import namedtuple
import sys
#
# Free Coding session for 2015-03-18
# Written by Matt Warren
#


def my_coroutine():
    while True:
        received = yield
        print('Received:', received)

it = my_coroutine()
next(it)

it.send('First')
it.send('Second')


ALIVE = '*'
EMPTY = '-'

Query = namedtuple('Query', ('y', 'x'))


def count_neighbours(y, x):
    n_ = yield Query(y + 1, x + 0)
    ne = yield Query(y + 1, x + 1)
    e_ = yield Query(y + 0, x + 1)
    se = yield Query(y - 1, x + 1)
    s_ = yield Query(y - 1, x + 0)
    sw = yield Query(y - 1, x - 1)
    w_ = yield Query(y + 0, x - 0)
    nw = yield Query(y + 1, x - 1)

    neighbour_states = [n_, ne, e_, se, s_, sw, w_, nw]
    count = 0
    for state in neighbour_states:
        if state == ALIVE:
            count += 1
    return count

Transition = namedtuple('Transition', ('y', 'x', 'state'))


def game_logic(state, neighbours):
    if state == ALIVE:
        if neighbours < 2:
            return EMPTY
        elif neighbours > 3:
            return EMPTY
    else:
        if neighbours == 3:
            return ALIVE
    return state


def step_cell(y, x):
    state = yield Query(y, x)
    neighbours = yield from count_neighbours(y, x)
    next_state = game_logic(state, neighbours)
    yield Transition(y, x, next_state)

TICK = object()


def simulate(height, width):
    while True:
        for y in range(height):
            for x in range(width):
                yield from step_cell(y, x)
        yield TICK


class Grid(object):
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.rows = []
        for _ in range(self.height):
            self.rows.append([EMPTY] * self.width)

    def __str__(self):
        g = ''
        for x in range(self.width):
            for y in range(self.height):
                g += self.rows[y][x]
            g += '\n'
        return g

    def query(self, y, x):
        return self.rows[y % self.height][x % self.width]

    def assign(self, y, x, state):
        print('assign')
        self.rows[y % self.height][x % self.width] = state


def live_a_generation(grid, sim):
    progeny = Grid(grid.height, grid.width)
    item = next(sim)
    while item is not TICK:
        if isinstance(item, Query):
            state = grid.query(item.y, item.x)
            item = sim.send(state)
        else:
            progeny.assign(item.y, item.x, item.state)
            item = next(sim)
    return progeny

grid = Grid(5, 9)
grid.assign(0, 3, ALIVE)
grid.assign(0, 4, ALIVE)
grid.assign(1, 4, ALIVE)
grid.assign(2, 4, ALIVE)
grid.assign(2, 3, ALIVE)
print(grid)

sim = simulate(grid.height, grid.width)
live_a_generation(grid, sim)
live_a_generation(grid, sim)
live_a_generation(grid, sim)
live_a_generation(grid, sim)
live_a_generation(grid, sim)
live_a_generation(grid, sim)
live_a_generation(grid, sim)
live_a_generation(grid, sim)
print(grid)
