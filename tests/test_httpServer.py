from http_server.httpServer import create_server, find_client, build_http_response
import pytest, socket

server_ip = "127.0.0.1"
port = 8000
server = create_server(server_ip,port)
client_ip = "127.0.0.1"
client_port = 8000

def test_create_server():
    assert server.getsockname() == ('127.0.0.1', 8000)

def test_build_http_response_contains_status_line_and_body():
    content = "Hello, Youness!"
    response = build_http_response(content)
    response_text = response.decode("utf-8")

    assert response_text.startswith("HTTP/1.1 200 OK")
    assert "Content-Type: text/html" in response_text
    assert content in response_text

def test_build_http_response_has_correct_content_length():
    content = "Short test"
    response = build_http_response(content)
    body = f"<html><body>{content}</body></html>"
    content_length_line = f"Content-Length: {len(body)}"

    assert content_length_line in response.decode("utf-8")