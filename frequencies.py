"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for i in items:
        i = str(i)
        if(i in frequencies.keys()):
            frequencies[i] +=1

        else:
            frequencies[i] = 1
    # Your code goes here
    return frequencies
