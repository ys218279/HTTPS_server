from http_server.httpServer import create_socket, accept_connection,bind_socket,build_http_response
import pycurl
import pytest, socket

@pytest.fixture
def server():
    sock = create_socket()
    bind_socket(sock, "127.0.0.1", 8000)
    return sock
def test_create_socket(server):
    assert server.getsockname() == ("127.0.0.1", 8000)

def test_http_build_response():
    http_response = build_http_response("This is a response")
    assert http_response.decode().endswith("<html><body>This is a response</body></html>")