#!/bin/python3

import sys

FOUND = 1
NOTFOUND = 0
FAILED = -1

t = int(input().strip())
for a0 in range(t):
    R,C = input().strip().split(' ')
    R,C = [int(R),int(C)]
    G = []

    for G_i in range(R):
       G_t = str(input().strip())
       G.append(G_t)
    r,c = input().strip().split(' ')
    r,c = [int(r),int(c)]
    P = []

    for P_i in range(r):
       P_t = str(input().strip())
       P.append(P_t)

    for row in range(R-r+1):
        found = NOTFOUND # to stop warning below
        for col in range(C-c+1):
            pattern_x, pattern_y = [0,0]
            found = NOTFOUND
            for row_idx in range(r):
                for col_idx in range(c):
                    if G[row+row_idx][col+col_idx] != P[row_idx][col_idx]:
                        found = FAILED
                        break
                if found == FAILED:
                    break
            else: # only run if for loop wasn't broken
                found = FOUND
                print("YES")
                break
        if found == FOUND:
            break
    else:
        print("NO")
