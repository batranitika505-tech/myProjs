#!/bin/python3

import sys
from math import *

t = int(input().strip())
s = int(log2((t-1)//3+1))
a,b=3*(2**s-1)+1,3*2**s
print(a+b-t)