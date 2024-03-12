class config:
    def __init__(self) -> None:
        self.configFolder='configs'
        self.databaseLocation=self.configFolder+"/BTChat.db"
        self.KeyFolder=self.configFolder+"/keys"
        self.loadRacodeSize=10

    def get_public_key(self, gid:str):
        return self.KeyFolder+"/{}.pub".format(gid)
    
    def get_private_key(self, gid:str):
        return self.KeyFolder+"/{}.key".format(gid)
