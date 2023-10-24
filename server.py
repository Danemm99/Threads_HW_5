import socket
import time

def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    print('Очікування підключення...')
    client_socket, client_address = server_socket.accept()
    print('Підключено до', client_address)

    for i in range(1, 101):
        message = f'Повідомлення {i}'
        client_socket.send(message.encode())
        time.sleep(1)

    client_socket.close()
    server_socket.close()

if __name__ == '__main__':
    run_server()
