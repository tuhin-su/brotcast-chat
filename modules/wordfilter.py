def fillterWord(badWord:list, string:str):
    for i in badWord:
        while i in string:
            inde= string.index(i)
            count= len(string[inde])-3
            start= string[inde][:2]
            end= string[inde][-1]
            mid= ("*" * count)
            string[inde] = (start+mid+end)
    return (" ".join(string))