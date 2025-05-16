import socket

def create_server(server_ip,port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((server_ip, port))
    return server

def find_client(server):
    pass