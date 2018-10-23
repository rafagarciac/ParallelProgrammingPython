#!/usr/bin/env python

"""
    My Dates Utilities
    - getDiferencialDate: Return the Date between the startTime and actual time.
    - getSeconds:         Return the Seconds between the startTime and actual time.
    - getMiliseconds:     Return the MiliSeconds between the startTime and actual time.
    - getMicroseconds:    Return the Microseconds between the startTime and actual time.
"""

__author__ = "Rafael García Cuéllar"
__email__ = "r.gc@hotmail.es"
__copyright__ = "Copyright (c) 2018 Rafael García Cuéllar"
__license__ = "MIT"

from datetime import datetime, date
import threading

def getMicroseconds(startTime):
    return str((datetime.now() - startTime).total_seconds() ) + " microsec."

def getMiliseconds(startTime):
    return str((datetime.now() - startTime).total_seconds() * 1000) + " milisec."

def getSeconds(startTime):
    return str((datetime.now() - startTime).total_seconds() * 1_000_000) + " sec."

def getDiferencialDate(startTime):
    return str((datetime.now() - startTime))

def getMetaDetails():
    print('\n--- M E T A    D E T A I L S ---')
    print("- TIMEOUT_MAX:      The maximum value allowed for the timeout parameter of blocking functions: %s" % (str(threading.TIMEOUT_MAX)))
    print("- stack_size():     Thread stack size used when creating new threads: %s" % (str(threading.stack_size())))
    print("- enumerate():      List of all Thread currently alive: %s" % (str(list(threading.enumerate()))))
    print("- active_count():   Number of threads currently alive: %s" % (str(threading.active_count())))
    print("- current_thread(): Current Name Thread Object: %s" % (str(threading.current_thread().getName())))
    print("- get_ident():      Current Thread identifier: %s" % (str(threading.get_ident())))
    print("- main_thread():    Main thread Object: %s" % (str(threading.main_thread().getName())))
    print("- settrace():       Set trace __main__: %s\n" % (str(threading.settrace('__main__'))))
