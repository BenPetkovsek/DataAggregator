import urllib.request
from urllib.request import Request, urlopen


combined = list()
with open("finalfinal.txt","r") as inputFile, open("finalwithnames.txt","r") as outputFile:
    while(True):
        name = inputFile.readline()[:17]
        #print("Scanning scores of user ID " + name)
        link = "https://scoresaber.com/u/" +name+ "&page=1&sort=2"
        req = urllib.request.Request(link,headers={'User-Agent': 'Mozilla/5.0'} )
        f = urllib.request.urlopen(req)
        scorePage = str(f.read())
        titleStartIndex = scorePage.find("<title>") + 7
        titleEndIndex = scorePage.find("'s profile", titleStartIndex)
        playername = scorePage[titleStartIndex:titleEndIndex -1]
        print(playername)
        outputFile.write(playername + "\n")
        outputFile.flush()
    inputFile.close()
    outputFile.close()
