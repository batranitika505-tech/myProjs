#!/bin/python

import sys

def saveThePrisoner(n, m, s):
    # Complete this function
    if n < m:
        m %= n
        #print m
        if m == 0:
            m = n
    last_id = s+m-1
    if last_id <= n:
        return last_id
    else:
        remaining_sweets = m-(n-s+1)
        return remaining_sweets


t = int(raw_input().strip())
for a0 in xrange(t):
    n, m, s = raw_input().strip().split(' ')
    n, m, s = [int(n), int(m), int(s)]
    result = saveThePrisoner(n, m, s)
    print(result)

