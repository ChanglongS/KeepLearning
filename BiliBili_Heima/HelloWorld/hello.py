import json

from pyecharts import charts, options, globals

print("Hello World!")

import socket
import select


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = ('192.168.212.105', 2000)
    s.bind(addr)
    s.listen(5)
    epoll = select.epoll()
    epoll.register(s.fileno(), select.EPOLLIN)
    client_list = []
    while True:
        events = epoll.poll(-1)
        for fp, event in events:
            if fp == s.fileno():
                new_client, client_addr = s.accept()
                client_list.append(new_client)
                epoll.register(new_client.fileno(), select.EPOLLIN)
            else:
                remove_client = None
                for client in client_list:
                    if fp == client.fileno():
                        data = client.recv(1024)
                        if data:
                            for send_client in client_list:
                                if send_client is client:
                                    pass
                                else:
                                    send_client.send(data)
                        else:
                            remove_client = client
                if remove_client:
                    client_list.remove(remove_client)
                    epoll.unregister(remove_client.fileno())
                    remove_client.close()


if __name__ == '__main__':
    main()
