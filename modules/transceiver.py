from modules import TX, RX
class Transceiver:
    def __init__(self) -> None:
        self.tx=TX.TX()
        self.rx=RX.RX()
        self.address=""
        self.port=4466
    def set(self, addr:str, port:int):
        self.address=addr
        self.port=port
    
    def up(self) -> bool:
        return self.rx.bind(self.port, self.address)

    def resive(self) -> bytes:
        return self.rx.lisen()

    def down(self) -> bool:
        return self.rx.close()
    
    def send(self, data:bytes) -> bool:
        return self.tx.send(msg=data,port=self.port)