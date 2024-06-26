Basics:
    "server.py" contains a class of the same name, 'Server'.

    'Server' contains a function called 'step()', which runs one server tick.

    Each tick:
        The server receives a frame. ('receive_frame()')
        The server creates movement instructions. ('process_movement()')
        The server sends movement instructions back to the client. ('send_movement()')

(P.S. Client is a complete disaster mess good luck)