#!/bin/python

import sys

initial_val = 3
t = int(raw_input().strip())
rem = 3
while t > rem:
    t = t-rem
    rem *= 2

print(rem-t+1)