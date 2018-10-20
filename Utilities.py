#!/usr/bin/env python

"""
    My Utilities
    - startTime: Inicialize the time datetime.now()
"""

__author__ = "Rafael García Cuéllar"
__email__ = "r.gc@hotmail.es"
__copyright__ = "Copyright (c) 2018 Rafael García Cuéllar"
__license__ = "MIT"

from datetime import datetime, date

def getMicroseconds(startTime):
    return str((datetime.now() - startTime).total_seconds() ) + " microsec."

def getMiliseconds(startTime):
    return str((datetime.now() - startTime).total_seconds() * 1000) + " milisec."

def getSeconds(startTime):
    return str((datetime.now() - startTime).total_seconds() * 1_000_000) + " sec."

def getDiferencialDate(startTime):
    return str((datetime.now() - startTime))
