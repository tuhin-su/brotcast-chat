import sqlite3
class DataBase:
    def __init__(self) -> None:
        self.database_file="BTchat.db"
        self.db=sqlite3.connect(self.database_file)
    
    def close(self):
        self.db.close()
    
    def exe(self, qurey:str):
        try:
            return self.db.execute(qurey)
        except:
            return False
        

class DataBaseHandaler:
    def __init__(self, db:DataBase) -> None:
        self.db=db

    def create_tabile(self):
        query='''CREATE TABLE IF NOT EXISTS `msg` (
                `MID` varchar(20),
                `GID` varchar(20),
                `UID` varchar(20),
                `DATA` varchar(80000),
                `TYPE` varchar(10),
                `FORMATE` varchar(10) NULL
            );'''
        return self.exe(qurey=query)
    
    def addMsg(self):
        pass
    
    def deletMsg(self, mid:str):
        pass

    def loadMsg(self,start:int):
        pass