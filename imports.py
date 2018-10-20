#!/usr/bin/env python

__author__ = "Rafael García Cuéllar"
__email__ = "r.gc@hotmail.es"
__copyright__ = "Copyright (c) 2018 Rafael García Cuéllar"
__license__ = "MIT"

from threading import Thread, Condition, Lock, Condition, RLock, Semaphore
import threading   
import multiprocessing
import concurrent.futures
import subprocess
import sched    
import queue
import asyncio