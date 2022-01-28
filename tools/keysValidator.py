import os


class Area:
    def __init__(self, areaID, mapID, areaName) -> None:
        self.areaID = areaID
        self.mapID = mapID
        self.areaName = areaName

class DbKey(Area):
    def __init__(self, areaID, mapID, areaName, keyName) -> None:
        super().__init__(areaID, mapID, areaName)
        self.keyName = keyName

def validateDbKey(dbKey: DbKey, expectedArea: Area):
    if(dbKey.areaID != expectedArea.areaID):
        print(f'Error in DBKey {dbKey.keyName}: Wrong area ID. Expected {expectedArea.areaID} but found {dbKey.areaID}')
        return True
    elif(dbKey.mapID != expectedArea.mapID):
        print(f'Error in DBKey {dbKey.keyName}: Wrong map ID. Expected {expectedArea.mapID} but found {dbKey.mapID}')
        return True
    else:
        return False    

def main():
    
    errorCounter = 0
    areas = []
    dbKeyLines = []
    keysFileName = os.path.abspath(__file__ + "/../../globals/patch/generated/keys.patch")
    areasFileName = os.path.dirname(__file__) + "/areaCodes.txt"

    with open(keysFileName) as keysDB :
        dbKeyLines = keysDB.readlines()
    
    areaCodeLines = open(areasFileName,'r').read().splitlines()
    for line in areaCodeLines:
        areaData = line.split(", ")
        area = Area(areaData[0], areaData[1], areaData[2])
        areas.append(area)

    for dbKeyText in dbKeyLines:
        # print(dbKey)
        areaNameStartIndex = dbKeyText.find("DBKey:") + 6
        areNameEndIndex = dbKeyText.find(":", areaNameStartIndex)
        areaName = dbKeyText[areaNameStartIndex: areNameEndIndex].lower()

        dbKeyNameStartIndex = areaNameStartIndex + 7
        dbKeyNameEndIndex = dbKeyText.find(' ', dbKeyNameStartIndex)
        dbKeyName = dbKeyText[dbKeyNameStartIndex: dbKeyNameEndIndex]

        areaIDIndex = dbKeyText.find("A1") +2
        areaID = dbKeyText[areaIDIndex: areaIDIndex + 2]
        mapID = dbKeyText[areaIDIndex + 2: areaIDIndex + 4]

        dbKey = DbKey(areaID, mapID, areaName, dbKeyName)

        for expectedArea in areas:
            if(expectedArea.areaName == dbKey.areaName):
                hasError = validateDbKey(dbKey, expectedArea)
                if(hasError):
                    errorCounter += 1
    
    print(f'Done! Found {errorCounter} error(s) in keys.patch file')





if __name__ == "__main__":
    main()