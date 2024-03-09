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
        try:
            self.rx.bind(self.port, self.address)
            return True
        except:
            return False

    def resive(self) -> bytes:
        return self.rx.lisen()

    def down(self) -> bool:
        try:
            self.rx.close()
            return True
        except:
            return False
    
    def send(self, data:bytes) -> bool:
        try:
            self.tx.send(msg=data,port=self.port)
            return True
        except:
            return False