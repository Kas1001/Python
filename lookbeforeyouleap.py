# Process File: Look Before You Leap (LBYL)

import os

p = 'C:/Users'

if os.path.exists(p):
    print(f'Directory {p} exists!')
else:
    print(f'No such directory as {p}.')