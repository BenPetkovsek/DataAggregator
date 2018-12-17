import urllib.request
from urllib.request import Request, urlopen



with open("baseList.txt","r") as inputFile, open("UsersToRemove.txt","w") as outputFile:
    while(True):
        name = inputFile.readline()[:17]
        print("Scanning scores of user ID " + name)
        link = "https://scoresaber.com/u/" +name+ "&page=1&sort=2"
        req = urllib.request.Request(link,headers={'User-Agent': 'Mozilla/5.0'} )
        f = urllib.request.urlopen(req)
        scorePage = str(f.read())
       # print(scorePage)
        #print (scorePage.find("Arrows"))
        #print(scorePage.find("Arrows") == -1)
        if(scorePage.find("Arrows") == -1):
            #print("test")
            outputFile.write(name + "\n")
            outputFile.flush()
    inputFile.close()
    outputFile.close()


            
          
            

    


