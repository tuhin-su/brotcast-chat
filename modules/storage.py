import sqlite3
from modules.config import config

class DataBase:
    def __init__(self,conf:config) -> None:
        self.conf=conf
        self.db=sqlite3.connect(self.conf.databaseLocation)
    
    def close(self):
        self.db.close()
    
    def exe(self, qurey:str):
        try:
            return self.db.execute(qurey)
        except:
            return False

class DataBaseHandaler:
    def __init__(self, db:DataBase, conf:config) -> None:
        self.db=db
        self.conf=conf
        self.create_tabile()

    def create_tabile(self):
        query='''CREATE TABLE IF NOT EXISTS `msg` (
  				`id` INTEGER PRIMARY KEY AUTOINCREMENT,
                `MID` varchar(20),
                `GID` varchar(20),
                `UID` varchar(20),
                `DATA` varchar(80000),
                `TYPE` varchar(10),
                `FORMATE` varchar(10) NULL
            );'''
        try:
            self.exe(qurey=query)
            return True
        except:
            return False
    
    def addMsg(self, mid:str, gid:str, uid:str, data:str, dataType:str, formate:str=''):
        query="INSERT INTO `msg` VALUES( NUll, '{}', '{}', '{}', '{}', '{}', '{}');"
        if mid.isspace() == True or gid.isspace() == True or uid.isspace() == True or data.isspace() == True or dataType.isspace() == True:
            return False
        if dataType != 'file':
            if formate.isspace() == True:
                return
        query.format(mid, gid, uid, data, dataType, formate)
        try:
            return self.db.exe(qurey=query)
        except:
            return

    def deletMsg(self, mid:str):
        query="DELETE FROM `msg` WHERE `mid`='{}';"
        if mid.isspace() == True:
            return
        query.format(mid)
        try:
            return self.db.exe(qurey=query)
        except:
            return

    def loadMsg(self,start:int=0):
        query="SELECT * FROM `msg` ORDER BY `id` DESC LIMIT {}, {}".format(start,self.conf.loadRacodeSize)
        try:
            return self.db.exe(qurey=query)
        except:
            return
        
    def drop_table(self):
        query="DROP TABLE `msg`"
        try:
            self.db.exe(qurey=query)
            return True
        except:
            return