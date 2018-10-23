#!/usr/bin/env python

"""
    Simply Python programm to compare the Sequential Mapping & Parallel Map.
    Using the multiprocessing module.
    Return the time in miliseconds that took each operation. 
"""

__author__ = "Rafael García Cuéllar"
__email__ = "r.gc@hotmail.es"
__copyright__ = "Copyright (c) 2018 Rafael García Cuéllar"
__license__ = "MIT"

from Utilities import getMicroseconds, getMiliseconds, getSeconds, getDiferencialDate
from multiprocessing import Pool
from datetime import datetime, date
import timeit

# Necessary Function for the ParallelMapping // Doesn't accept the lambda expression like Sequential Mapping 
def f(x):
    return x**2

# Sequential Map
def sequentialMapping(listed):
    return map(lambda x: x**2, listed)
    
def parallelMapping(listed):
    pool = Pool()
    return pool.map(f, listed)

if __name__ == '__main__':
    numberList = [x for x in range(10_000_000)]
# Sequential Mapping
    startTime = datetime.now() 
    sequentialMapping(numberList)
    print("Sequential Mapping: " +
        str(
            round(
                    (timeit.timeit('sequentialMapping(numberList)','from __main__ import sequentialMapping, numberList') * 10_000), 2
                )
            ) + ' milisec.'
        )

# Parallel Mapping
    startTime = datetime.now() 
    parallelMapping(numberList)
    print("Parallel Mapping: " + getMiliseconds(startTime))
    print()