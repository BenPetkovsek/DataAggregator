import urllib.request
from urllib.request import Request, urlopen
#1836 is max
namelist = list()
outputFile = open("baseList.txt","a")
for i in range(1,1836):
    print("Initiating scan on page " + str(i))
    link = "https://scoresaber.com/global/" + str(i)
    req = urllib.request.Request(link,headers={'User-Agent': 'Mozilla/5.0'} )
    f = urllib.request.urlopen(req)
    myfile = f.read()
    #print (myfile)
    
    splitfile = str(myfile).split("/u/")
    #print(splitfile)

    templist = list()
    #find user ID's from global rank page and add to list
    for j in range(len(splitfile)):
        templist.append([splitfile[j][:17]])
        #print(splitfile[j][:17])
    del templist[0]
    for j in range(len(templist)):
           #print (templist[j][0] + " --- " + str(j))
           outputFile.write(templist[j][0] + "\n")

outputFile.close()
