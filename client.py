import socket

def run_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    for i in range(1, 101):
        received_message = client_socket.recv(1024).decode()
        print('Отримано:', received_message)

    client_socket.close()

if __name__ == '__main__':
    run_client()
