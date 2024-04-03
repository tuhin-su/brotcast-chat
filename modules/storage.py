import sqlite3
from modules.config import config

class DataBaseHandaler:
    def __init__(self, conf:config) -> None:
        self.conf=conf
        self.db=self.db=sqlite3.connect(self.conf.databaseLocation)
        self.create_tabile()

    def create_tabile(self):
        query='''CREATE TABLE IF NOT EXISTS `msg` (
  				`id` INTEGER PRIMARY KEY AUTOINCREMENT,
                `MID` varchar(40),
                `GID` varchar(40),
                `UID` varchar(40),
                `DATA` varchar(80000),
                `TYPE` varchar(10),
                `FORMATE` varchar(10) NULL,
                `FILENAME` varchar(30) NULL
            );'''
        try:
            self.db.execute(query)
        except Exception as e:
            return e
    
    def addMsg(self, mid:str, gid:str, uid:str, data:str, dataType:str='text', formate:str='', FileName:str=''):
        query="INSERT INTO `msg` VALUES( NUll, '{}', '{}', '{}', '{}', '{}', '{}', '{}');"

        if mid.isspace() == True or gid.isspace() == True or uid.isspace() == True or data.isspace() == True or dataType.isspace() == True:
            return False
        
        if dataType != 'text':
            if formate.isspace() == True:
                return
            
        query=query.format(mid, gid, uid, data, dataType, formate, FileName)
        try:
            self.db.execute(query)
            self.db.commit()
        except Exception as e:
            return e

    def deletMsg(self, mid:str):
        query="DELETE FROM `msg` WHERE `mid`='{}';"
        if mid.isspace() == True:
            return
        query.format(mid)
        try:
            return self.db.execute(query)
        except:
            return

    def loadMsg(self, id:int=1):
        query="SELECT * FROM `msg` WHERE  `id`='{}';".format(id)

        print(query)
        try:
            return self.db.execute(query).fetchone()
        except Exception as e:
            return e
        
    def drop_table(self):
        query="DROP TABLE `msg`"
        try:
            self.db.execute(query)
            return True
        except Exception as e:
            return e
        
    def len(self):
        query="SELECT COUNT(*) AS record_count FROM msg;"
        try:
           return self.db.execute(query).fetchone()
        except:
            pass
