def egyedi_betuk(szoveg:str=""):
    cv = 0
    betuk=[]

    while cv<len(szoveg):
        betu=szoveg[cv].lower()
        if betu.isalpha() and betu not in betuk:
            betuk.append(betu)
            cv+=1
        else:
            cv+=1
        hany=szoveg.count(betu)
        i=betuk.index(betuk)
        betuk.insert(i+1, hany)

    return sorted(betuk)