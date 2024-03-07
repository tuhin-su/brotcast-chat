from socket import socket, AF_INET, SOCK_DGRAM, IPPROTO_UDP, SOL_SOCKET, SO_BROADCAST
class RX:
    def __init__(self) -> None:
        self.RX = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)
        self.RX.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
        self.port = 4454
        self.addr = ""
        self.ui = None

    def set(self, ui) -> None:
        self.ui = ui

    def bind(self):
        self.RX.bind((self.addr, self.port))
        while True:
            data, _ = self.RX.recvfrom(1024)
            self.ui.recive_msg(data)
