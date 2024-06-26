import comm.server

s = comm.server.Server()
s.start()

while True:
    s.step()
