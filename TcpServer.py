'''
@author: chen
'''
# -*- coding: utf-8 -*-
from socketserver import TCPServer, StreamRequestHandler, ForkingMixIn, ThreadingMixIn
class TServer(ThreadingMixIn, TCPServer):
    print('TServer')

class FServer(ForkingMixIn, TCPServer):
    print('FServer')

class Handler(StreamRequestHandler):
    def handle(self):
        addr = self.request.getpeername()
        print('conn from', addr)
        self.wfile.write(('thank' + addr[0]).encode())
        
def simpel():
    server = TCPServer(('', 1234), Handler)
    server.serve_forever()

def fork():
    server = FServer(('', 1234), Handler)
    server.serve_forever()
    
def thread():
    server = TServer(('', 1234), Handler)
    server.serve_forever()


if __name__ == '__main__':thread()
