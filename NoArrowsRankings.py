import urllib.request
from urllib.request import Request, urlopen
from operator import itemgetter

#holds the user ID's and eventually score totals of the users
namelist = list()

with open("finalEligibleUsers.txt", "r") as users, open("finalResults.txt","w") as outputResults:
    for i in range(0,1684):
        namelist.append([users.readline()[:17]])


    #GO TO EVERY USER PAGE AND SUM SCORES FOR NO ARROWS MAPS
           #len(namelist)
    for i in range(len(namelist)):
        print("Scanning scores of user ID " + namelist[i][0])
        link = "https://scoresaber.com/u/" + namelist[i][0]+ "&page=1&sort=2"
        req = urllib.request.Request(link,headers={'User-Agent': 'Mozilla/5.0'} )
        f = urllib.request.urlopen(req)
        myfile = str(f.read())

            
            #find the start and end index of where the num of scores set is
        numScoresStartIndex = myfile.find("Play Count:</b> ") + 16
        #print(str(numScoresStartIndex) + str(myfile)[numScoresStartIndex])

        numScoresEndIndex = myfile.find("<",numScoresStartIndex)
            #the number o0f scores the user has set
        #print (myfile[numScoresStartIndex:numScoresEndIndex])
        numScoresSet = int(myfile[numScoresStartIndex:numScoresEndIndex].replace(",",""))
        #print ("    User has set " +str(numScoresSet) + " scores.")

            #the number of pages is the number of scores divided by 8 scores per page
        numPages = round(numScoresSet/8)
        #print("     Therefore, the user has " + str(numPages) + " pages of scores.")

            #SCAN EACH PAGE OF SCORES AND FIND RANK FOR EACH NO ARROWS SONG, ADD TO NAMELIST UNDER USER ID
        

        rankSum = 0
        scoreSum = 0
        finalSum = 0
        numScores = 0
        #numPages + 1
        for j in range(1,numPages + 1):
                #get the page for the scores
            scorePageLink = "https://scoresaber.com/u/" + namelist[i][0] + "&page=" + str(j) +"&sort=2"
            request = urllib.request.Request(scorePageLink,headers={'User-Agent': 'Mozilla/5.0'} )
            file = urllib.request.urlopen(request)
            scorePage = str(file.read())
                #individual scores are separated into href headers
            splitScorePage = scorePage.split("href")

            for p in range(0, len(splitScorePage)):
                #print (splitScorePage[p])
                #print ("")
                #print ("--")
                #print ("--")
                #print ("")
                if (splitScorePage[p].find("Arrows") != -1):
                    eligible = True
                    rankStartIndex = splitScorePage[p].find("# ") + 2
                    rankEndIndex = splitScorePage[p].find("<", rankStartIndex)
                    scoreStartIndex = rankEndIndex + 9
                    scoreEndIndex = splitScorePage[p].find("<", scoreStartIndex)
                    score = int(splitScorePage[p][scoreStartIndex:scoreEndIndex].replace(",",""))
                    #print(score)
                    rank = int(splitScorePage[p][rankStartIndex:rankEndIndex])
                    #print(rank)
                    numScores = numScores + 1
                    scoreSum = scoreSum + score
                    rankSum = rankSum + rank
                    finalSum = finalSum + (float(score)/float(rank))
                    
                    #print("Found No Arrows song! Their rank is: " + rank)
        outputResults.write(namelist[i][0]+ ","+ str(finalSum)+ "," + str(numScores)+ ","+ str(rankSum)+ ","+str(scoreSum) + "\n")
        outputResults.flush()
        namelist[i].append(str(rankSum))
        namelist[i].append(str(scoreSum))
        namelist[i].append(str(numScores))
        namelist[i].append(str(finalSum))

                

    finalDict = dict()
    #len(namelist)
    for i in range(len(namelist)):
        print("User ID: " + namelist[i][0])
        print("Rank of No Arrows Songs: ")
        rankSum = float(namelist[i][1])
        scoreSum = float(namelist[i][2])
        numScores = float(namelist[i][3])
        finalSum = float(namelist[i][4])
                  # the final score is your total number of no arrows scores multiplied by the ratio of the sum of ranks in no arrows to the number of no arrows scores
        if(rankSum != 0):
            
            finalDict[namelist[i][0]] = finalSum
        print("Number of scores: " + str(numScores))
        print("Sum of scores: " + str(scoreSum))
        print("Sum of ranks: " + str(rankSum))
        print("Average rank: " + str(rankSum/numScores))
        print("FINAL SCORE: " + str(finalSum))
        print("")
              
              
    finalList = sorted(finalDict.items(),key=itemgetter(1))

    for i in range(0,11):
        print ("==========GLOBAL POSITION " + str(i) + " ==========")
        print ("USER " + finalList[i][0] + " WITH A SCORE OF " + str(finalList[i][1]))
            

            

            
        








        



        print("-------------")

        
