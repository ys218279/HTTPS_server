from http_server.httpServer import create_server, find_client
import pytest, socket

server_ip = "127.0.0.1"
port = 8000
server = create_server(server_ip,port)
client_ip = "127.0.0.1"
client_port = 8000

def test_create_server():
    assert server.getsockname() == ('127.0.0.1', 8000)

def test_find_client():
    
    assert find_client(server) == f"Accepted connection from {client_address[0]}:{client_address[1]}"