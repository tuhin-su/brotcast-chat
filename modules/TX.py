from socket import socket, AF_INET, SOCK_DGRAM, IPPROTO_UDP, SOL_SOCKET, SO_BROADCAST
class TX:
    def __init__(self) -> None:
        self.TX = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)
        self.TX.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
        self.port = 4454

    def send(self, msg: bytes) -> bool:
        self.TX.sendto(msg, ('<broadcast>', self.port))
        return True
