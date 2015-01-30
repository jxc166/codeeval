__author__ = 'jiawei'

'''
to find all possible positions for the next move of the knight on the empty chessboard.
input
g2
a1
d6
e5
b1

output (sorted in alphanumeric order)
e1 e3 f4 h4
b3 c2
b5 b7 c4 c8 e4 e8 f5 f7
c4 c6 d3 d7 f3 f7 g4 g6
a3 c3 d2
'''

import sys

ln = {'a', 1, 'b', 2}

test_cases = open(sys.argv[1], 'r')
for test in test_cases:

    x, y = test[:2]
    x = ord(x)
    y = int(y)


    m =[ None ]*8
    m[0] = (x-2, y-1)
    m[1] = (x-2, y+1)
    m[2] = (x-1, y-2)
    m[3] = (x-1, y+2)
    m[4] = (x+1, y-2)
    m[5] = (x+1, y+2)
    m[6] = (x+2, y-1)
    m[7] = (x+2, y+1)

    out = []
    for a, b in m:
        if a < ord('a') or a > ord('h'):
            continue
        if b < 1 or b > 8:
            continue

        out.append('{a}{b}'.format(a=chr(a),b=b))

    print(' '.join(out))

test_cases.close()