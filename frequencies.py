"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

list = ['a', 'a', 'b', 'b', 'b', 'c']

def frequencies(items):
    frequencies = {}
    for i in items:
        current = str(i)
        if(current in frequencies.keys()):
            frequencies[current] +=1

        else:
            frequencies[current] = 1
    # Your code goes here
    return frequencies

