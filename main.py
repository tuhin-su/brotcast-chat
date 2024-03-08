from modules.UI import UI
from modules.transceiver import Transceiver
from modules.functions import *
from modules.storage import Storage
from threading import Thread
from json import loads, dumps

class BTchat:
    def __init__(self) -> None:
        self.ui=UI()
        self.ui.set(self)
        self.trans=Transceiver()
        self.storage=Storage()
        self.id=None

    def send(self, data):
        print("calling the send function")

    def run(self):
        self.ui.create_window()
        self.ui.set(self)
        self.ui.run()

if __name__=="__main__":
    core=BTchat()
    core.run()