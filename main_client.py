import comm.client

c = comm.client.Client()
c.start(input("Host IP: "))

while True:
    c.step()
