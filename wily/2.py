#!/usr/bin/env python

def example2(limit):
    """ print positive integers less than limit """
    list_integers = range(limit)
    for i in list_integers:
        print(i)


if __name__ == '__main__':
	example2(10)
