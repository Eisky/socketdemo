import _socket
import Queue
import select
import sys


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(5)
