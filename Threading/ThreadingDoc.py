#!/usr/bin/env python

"""
    Simple how-to-code-class for show all methods & functions
    of the Threading module.
"""

__author__ = "Rafael García Cuéllar"
__email__ = "r.gc@hotmail.es"
__copyright__ = "Copyright (c) 2018 Rafael García Cuéllar"
__license__ = "MIT"

import threading
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
from Utilities import getMetaDetails

# This module defines the following functions:  
def doTarget():
    total = 0
    for i in range(1_000):
        for j in range(1_000):
            total += i * (j + j)
    print("Total: %s" % str(total))

if __name__ == '__main__':
    # Thread-Local Data
    print('############################## T H R E A D   L O C A L    D A T A ###############################')
    mydata = threading.local()
    mydata.x = 1; mydata.y = 3
    print(f'Local Thread Data (x): {mydata.x}')

    print('\n################################## T H R E A D   O B J E C T S #################################')
    t1 = threading.Thread(group=None, target=doTarget(), daemon=None, name="Thread 1")
    t1.setDaemon(False)
    t1.start()  # t1.run()
    print('Is alive? %s' % t1.is_alive())
    print('Is Daemon? %s' % t1.isDaemon())
    getMetaDetails()
    t1.join(timeout=None)
    t1._stop()

    print('\n#################################### L O C K   O B J E C T S  ##################################')
    lock = threading.Lock()
    print('Thread status lock: %s' % lock.acquire())
    print('Thread status lock: %s' % lock.acquire(False))
    print('Thread status lock: %s' % lock.release())

    print('\n################################## R L O C K   O B J E C T S  ##################################')
    rlock = threading.RLock()
    print('Thread status rlock: %s' % rlock.acquire())
    print('Thread status rlock: %s' % rlock.acquire(False)) # Never stops always will be True - Recursive
    print('Thread status rlock: %s' % rlock.release())
    
    print('\n############################# C O N D I T I O N    O B J E C T S  ##############################')
    condition = threading.Condition(lock=None)
    print('Condition Blocking: %s ' % condition.acquire(blocking=True))
    # Producer-Consumer Example
    # condition.wait()
    # condition.wait_for(predicate, timeout=None)
    # condition.notify()
    # condition.notify_all()

    print('\n######################################  S E M A P H O R E  ######################################')
    semaphore = threading.Semaphore(value=10)
    boundedSemaphore = threading.BoundedSemaphore(value=5)
    print('Semaphore status semaphore: %s' % semaphore.acquire())
    print('Semaphore status semaphore: %s' % semaphore.acquire(False)) 
    print('Semaphore status semaphore: %s' % semaphore.release())

    print('\n###################################  E V E N T  O B J E C T S  ###################################')
    event = threading.Event()
    print('Internal Flag status: %s' % event.is_set())
    event.set()
    print('Internal Flag status: %s' % event.is_set())
    event.clear()
    print('Internal Flag status: %s' % event.is_set())
    # event.wait(timeout=None)

    print('\n###################################  T I M E R  O B J E C T S  ###################################')
    t = threading.Timer(30.0, doTarget, args=None, kwargs=None)
    # t.start()
    t.cancel()     # stop the timer's action if it's still waiting

    print('\n################################  B A R R I E R  O B J E C T S ##################################')
    barrier = threading.Barrier(2, action=None, timeout=5)
    barrier.reset()
    print('The number of threads required to pass the barrier.: %s' % str(barrier.parties))
    print('The number of threads currently waiting in the barrier: %s' % str(barrier.n_waiting))
    print('Barrier broken state: %s' % str(barrier.broken))
    barrier.abort()
    print('Barrier broken state: %s' % str(barrier.broken))

    # def server():
    #     start_server()
    #     b.wait()
    #     while True:
    #         connection = accept_connection()
    #         process_server_connection(connection)

    # def client():
    #     b.wait()
    #     while True:
    #         connection = make_connection()
    #         process_client_connection(connection)

    """ TIP:
        Using locks, conditions, and semaphores in the with statement
    """
    
