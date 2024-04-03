from modules.UI import UI
from modules.transceiver import Transceiver
from modules.functions import *
from modules.storage import DataBaseHandaler
from modules.config import config
from threading import Thread

class BTchat:
    def __init__(self) -> None:
        self.conf=config()
        self.ui=UI(conf=self.conf)
        self.ui.set(self)
        self.trans=Transceiver()
        self.storage=DataBaseHandaler(conf=self.conf)
        self.id=None
        self.active_gid=None
        self.active=True
        self.thread=Thread(target=self.lisiner)
        self.lastMsgId=None
        
    def loadmsg(self, up:bool=True):
        if self.lastMsgId == None:
            self.lastMsgId=self.storage.len()[0]
            res=self.storage.loadMsg()
            
        else:
            if up==True:
                res=self.storage.loadMsg(id=self.lastMsgId-1)
            elif up == False:
                res=self.storage.loadMsg(id=self.lastMsgId+1)
        if res == None:
            return
        
        self.lastMsgId=res[0]

        return MsgLoader(MsgFormater(id=res[3], mid=res[1], gid=res[2], data=res[4], FileType=res[5], FileName=res[7], FileFormate=res[6] ))
    
    def send(self, data): # sending msg to resiver  
        self.active_gid="llb"
        if self.active_gid != None and self.id != None:
            data=fillterWord(["bac","bccd"], data)
            data=MsgFormater(id=self.id, mid=gen_unic(), gid=self.active_gid, data=data)
            if self.trans.send(data) and self.ui.active:
                data=MsgLoader(data=data)
                self.ui.add_msg(data=data)

    def lisiner(self):
        storage=DataBaseHandaler(conf=self.conf)
        self.trans.up()
        while self.active:
            data=self.trans.resive()
            data=MsgLoader(data=data)
            FileName=FileFormate=''
            if ('FileName' in data.keys()) and ('FileFormate' in data.keys()):
                FileName=data['FileName']
                FileFormate=data['FileFormate']
            storage.addMsg(mid=data['mid'], gid=data['gid'], uid=data['id'], data=data['data'], dataType=data['type'], formate=FileFormate, FileName=FileName)
            if data['id'] != self.id and self.ui.active:
                self.ui.add_msg(data=data)

    def start_lisiner(self):
        # IT call by ui when user login
        self.active=True
        self.thread.start()

    def run(self):
        self.ui.create_window()
        self.ui.set(contriler=self)
        self.ui.run()
        self.ui.active=False
        self.active=False
        self.send("Good bye!")

if __name__=="__main__":
    core=BTchat()
    core.run()