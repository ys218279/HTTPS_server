import socket

def create_socket():
    return socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def bind_socket(sock, host, port):
    sock.bind((host, port))
    sock.listen(1)
    print(f"Listening on {host}:{port}")

def accept_connection(server_socket):
    client_socket, addr = server_socket.accept()
    print(f"Accepted connection from {addr}")
    return client_socket

def build_http_response(content):
    body = f"<html><body>{content}</body></html>"
    response = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: text/html\r\n"
        f"Content-Length: {len(body)}\r\n"
        "\r\n" +
        body
    )
    print(response)
    return response.encode("utf-8")

def handle_client(client_socket):
    request = client_socket.recv(1024).decode("utf-8")
    print("Request:", request)
    print("=================")
    header = request.split(' ')[0]
    
    if "GET" == header:
        response = build_http_response("This is a GET request")
    elif "POST" == header:
        response = build_http_response("This is a POST request")
    else:
        response = build_http_response("IDK wtf this is")
    client_socket.sendall(response)
    client_socket.close()
