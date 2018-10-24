from multiprocessing.connection import Listener
from array import array

address = ('localhost', 6000)     # family is deduced to be 'AF_INET'

with Listener(address, authkey=b'default_password') as listener:
    with listener.accept() as conn:
        while True:
            # Send 
            print('connection accepted from', listener.last_accepted)
            string = input('Write something to the Client: \n')
            conn.send(string)

            # Read
            print(conn.recv())