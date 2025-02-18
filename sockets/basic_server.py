import socket

s = socket.socket()
print("Socket successfully created")

port = 40674
s.bind(('', port))
print("Socket bound to port %d" % port)

s.listen(5)
print("Socket is listening")

while True:
    c, addr = s.accept()
    print("Got connection from", addr)
    c.send("Thank you for connecting.".encode())
    c.close()