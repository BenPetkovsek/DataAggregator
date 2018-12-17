
baseList = list()
toRemove = list()
with open("baseList.txt","r") as baseFile, open("UsersToRemove.txt","r") as removeFile:
    #23219
    for i in range(0,34646):
        toRemove.append(removeFile.readline()[:17])
        print("Loading toRemove: user number " + str(i))
    for i in range(0,38146):
        baseList.append(baseFile.readline()[:17])
        print("Loading baseList: user number " + str(i))

print("...Loading complete!")
baseFile.close()
removeFile.close()
eligibleUsers = list()
eligibleUsersFile = open("NewEligibleUsers.txt","w")


for i in range(len(toRemove)):
    try:
        baseList.remove(toRemove[i])
    except:
        print("User " + toRemove[i] + " does not exist in baseList")
    


print("Adding eligible users to file")
for i in range(len(baseList)):
    
    print(baseList[i])
    eligibleUsersFile.write(baseList[i] + "\n")
    

eligibleUsersFile.close()
