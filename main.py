import server
import client
from threading import Thread

if __name__ == '__main__':
    # Запускаємо сервер та клієнт в окремих потоках
    server_thread = Thread(target=server.run_server)
    client_thread = Thread(target=client.run_client)

    server_thread.start()
    client_thread.start()

    server_thread.join()
    client_thread.join()
