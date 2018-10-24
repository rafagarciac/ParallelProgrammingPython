from multiprocessing.connection import Client
from array import array

address = ('localhost', 6000)

with Client(address, authkey=b'default_password') as conn:
    while True:
        # Read
        print(conn.recv())                  # => [2.25, None, 'junk', float]

        # Send
        string = input('Write something to the Listener (Server): \n')
        conn.send(string)