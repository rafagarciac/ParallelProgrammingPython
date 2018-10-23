#!/usr/bin/env python

"""
    Artesanal example Pipe without Pipe class.
"""

__author__ = "Rafael García Cuéllar"
__email__ = "r.gc@hotmail.es"
__copyright__ = "Copyright (c) 2018 Rafael García Cuéllar"
__license__ = "MIT"

from concurrent.futures import ProcessPoolExecutor
import time
import random

def worker(arg):
    time.sleep(random.random())
    return arg

def pipeline(future):
    pools[1].submit(worker, future.result()).add_done_callback(printer)

def printer(future):
    pools[2].submit(worker, future.result()).add_done_callback(spout)

def spout(future):
    print(future.result())

def instanceProcessPool():
        pools = []
        for i in range(3):
            pool = ProcessPoolExecutor(2) 
            pools.append(pool)
        return pools

def shutdownPools(pools):
    for pool in pools:
        pool.shutdown()    

def runThreadsInPipeline(pools):
    for pool in pools:
        pool.submit(worker, random.random()).add_done_callback(pipeline) 

if __name__ == "__main__":
    __spec__ = None                 # Fix multiprocessing in Spyder's IPython
    
    pools = instanceProcessPool()   # pool = ProcessPoolExecutor([max_workers])
    runThreadsInPipeline(pools)     # pools[0].submit(worker, random.random()).add_done_callback(pipeline) 
    shutdownPools(pools)            # pool.shutdown()