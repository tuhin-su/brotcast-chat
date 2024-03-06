from socket import socket, AF_INET, SOCK_DGRAM, IPPROTO_UDP, SOL_SOCKET, SO_REUSEPORT, SO_BROADCAST
import threading
from json import dumps, loads

class RX:
    def __init__(self) -> None:
        self.RX = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)
        self.RX.setsockopt(SOL_SOCKET, SO_REUSEPORT, 1)
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
            self.ui.show(loads(data.decode()))


class TX:
    def __init__(self) -> None:
        self.TX = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)
        self.TX.setsockopt(SOL_SOCKET, SO_REUSEPORT, 1)
        self.TX.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
        self.port = 4454

    def send(self, msg: bytes) -> None:
        self.TX.sendto(msg, ('<broadcast>', self.port))


class UI:
    def __init__(self, tx: TX) -> None:
        self.tx = tx

    @staticmethod
    def show(msg: list):
        print("\n{} : {}\n".format(msg[0], msg[1]))

    def run(self):
        name = ''
        while name == '':
            name = input("What is your name: ")

        while True:
            msg = ''
            while msg == '':
                msg = input()

            msg = dumps([name, msg]).encode()
            self.tx.send(msg=msg)


class CoreSystem:
    def __init__(self) -> None:
        self.tx = TX()
        self.rx = RX()
        self.ui = UI(self.tx)
        self.rx.set(ui=self.ui)
        self.t1 = None
        self.t2 = None

    def run(self) -> None:
        self.t1 = threading.Thread(target=self.rx.bind)
        self.t2 = threading.Thread(target=self.ui.run)
        self.t1.start()
        self.t2.start()


if __name__ == '__main__':
    core = CoreSystem()
    core.run()
