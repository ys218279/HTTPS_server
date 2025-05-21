from httpServer  import create_socket,bind_socket,accept_connection,handle_client

def start_server():
    sock = create_socket()
    bind_socket(sock, "127.0.0.1", 8080)
    while True:
        client_socket = accept_connection(sock)
        handle_client(client_socket)

start_server()