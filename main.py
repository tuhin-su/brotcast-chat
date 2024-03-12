from modules.UI import UI
from modules.transceiver import Transceiver
from modules.functions import *
from modules.storage import DataBase, DataBaseHandaler
from modules.config import config
from threading import Thread

class BTchat:
    def __init__(self) -> None:
        self.conf=config()
        self.ui=UI()
        self.ui.set(self)
        self.trans=Transceiver()
        self.db=DataBase(conf=self.conf)
        self.storage=DataBaseHandaler(db=self.db, conf=self.conf)
        self.id=None
        self.active_gid=None
        self.active=True
        self.thread=Thread(target=self.set)
        

    def send(self, data):
        self.active_gid="llb"
        if self.active_gid != None and self.id != None:
            data=fillterWord(["bac","bccd"], data)
            data=MsgFormater(id=self.id, gid=self.active_gid, data=data)
            if self.trans.send(data) and self.ui.active:
                data=MsgLoader(data=data)
                self.ui.add_msg(data=data)


    def set(self):
        self.trans.up()
        while self.active:
            data=self.trans.resive()
            data=MsgLoader(data=data)
            if data['id'] != self.id and self.ui.active:
                self.ui.add_msg(data=data)

    def start_lisiner(self):
        # IT call by ui when user login
        self.active=True
        self.thread.start()

    def run(self):
        self.ui.create_window()
        self.ui.set(self)
        self.ui.run()
        self.ui.active=False
        self.active=False
        self.send("Good bay!")

if __name__=="__main__":
    core=BTchat()
    core.run()