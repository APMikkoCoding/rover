import io
import socket
import struct
from PIL import Image
import matplotlib.pyplot as pl



server_socket = socket.socket()
server_socket.bind(('10.189.77.105', 12534))
server_socket.listen(0)

connection = server_socket.accept()[0].makefile('rb')
try:
    img = None
    while True:
        image_len = struct.unpack('<L', connection.read(struct.calcsize('<L')))[0]
        if not image_len:
            break

        image_stream = io.BytesIO()
        image_stream.write(connection.read(image_len))

        image_stream.seek(0)
        image = Image.open(image_stream)

        if img is None:
            img = pl.imshow(image)
        else:
            img.set_data(image)

        pl.pause(0.01)
        pl.draw()

        print('Image is %dx%d' % image.size)
        image.verify()
        print('Image is verified')
finally:
    connection.close()
    server_socket.close()
