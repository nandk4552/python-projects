import socket

hostn = socket.gethostname()
ipad = socket.gethostbyname(hostn)

print("IP Address = "+ipad)