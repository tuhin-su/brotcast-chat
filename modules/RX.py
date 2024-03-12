from socket import socket, AF_INET, SOCK_DGRAM, IPPROTO_UDP, SOL_SOCKET, SO_BROADCAST
class RX:
    def __init__(self) -> None:
        self.RX = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)
        self.RX.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
        self.port = 4444
        self.addr = ""

    def bind(self, port:int=4444, addr:str="") -> bool:
        self.addr=addr
        self.port=port
        try:
            self.RX.bind((self.addr, self.port))
            return True
        except:
             return False
    
    def lisen(self) -> bytes:
            data, _ = self.RX.recvfrom(1024)
            return data

    def close(self) -> bool:
        try:
            self.RX.close()
            return True
        except:
             return False