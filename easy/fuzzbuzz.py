__author__ = 'jxc166'


'''
Your program should accept a file as its first argument. The file contains multiple separated lines; each line contains
 3 numbers that are space delimited. The first number is the first divider (X), the second number is the second divider
 (Y), and the third number is how far you should count (N). You may assume that the input file is formatted correctly
 and the numbers are valid positive integers.

input
3 5 10
2 7 15

output
1 2 F 4 B F 7 8 F B
1 F 3 F 5 F B F 9 F 11 F 13 FB 15

'''

import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases: # test stands for one line
    x, y, n = (int(i) for i in test.split(' '))

    out = []
    for i in range(1, n+1):
        if not i%x:
            el = 'FB' if not i%y else 'F'
        else:
            el = 'B' if not i%y else str(i)
        out.append(el)

    print(' '.join(out))

test_cases.close()