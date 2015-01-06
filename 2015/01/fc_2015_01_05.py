#!/usr/bin/env python3
# imports go here
from pathlib import Path

#
# Free Coding session for 2015-01-05
# Written by Matt Warren
#


p = Path('.')

for x in p.iterdir():
    print(x)

for x in p.glob('2015/**/*.py'):
    print(x)

# division overload for directories
new_path = p / '2015' / '01'
if new_path.exists():
    print(new_path)
    for x in new_path.iterdir():
        print(x)

f = new_path / 'fc_2015_01_05.py'
print(f.parts)
assert(f.name == 'fc_2015_01_05.py')
assert(f.suffix == '.py')
assert(f.stem == 'fc_2015_01_05')

with f.open() as f:
    f.readline()
