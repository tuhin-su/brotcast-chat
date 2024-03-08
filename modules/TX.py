from socket import socket, AF_INET, SOCK_DGRAM, IPPROTO_UDP, SOL_SOCKET, SO_BROADCAST
class TX:
    def __init__(self) -> None:
        self.TX = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)
        self.TX.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

    def send(self, msg:bytes, addr:str='<broadcast>', port:int=4466) -> bool:
        try:
            self.TX.sendto(msg, (addr, port))
            return True
        except:
            return False
