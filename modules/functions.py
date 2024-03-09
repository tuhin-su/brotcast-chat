from json import dumps

def fillterWord(badWord:list, string:str):
    string=string.split(" ")
    for badword in badWord: 
        for i, word in enumerate(string):
            if badword.lower() == word.lower():
                inde= string.index(word)
                count= len(string[inde])-3
                start= string[inde][:2]
                end= string[inde][-1]
                if count <= 0:
                    count=count+2
                    start= string[inde][:1]
                    end=""
                mid= ("*" * count)
                string[inde] = (start+mid+end)
    return (" ".join(string))

def MsgFormater(id:str, gid:str, data:str, FileType:str="text", **kwargs) -> bytes:
    Interdata={
        "id":id,
        "gid":gid,
        "type":FileType,
        "data":data,
    }
    if FileType == "file":
        try:
            Interdata["FileName"]=kwargs["FileName"]
            Interdata["FileFormate"]=kwargs["FileFormate"]
        except KeyError:
            return False
        else:
            return dumps(Interdata).encode()