#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0: 
        print([])
        return
    elif length == 1: 
        print([0])
        return

    test = [0,1]

    for x in range (0, length-2):
        test.append(test[x+1]+test[x])

    print(test)


print_fibonacci(9)