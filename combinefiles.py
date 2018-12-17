combined = list()
with open("finalfinal.txt","r") as rowFile, open("finalwithnames.txt","r") as nameFile:
    for i in range (5214):
        row = rowFile.readline()
        name = nameFile.readline()
        combined.append(name + "," +row)

rowFile.close()
nameFile.close()
outFile = open("lastFinal.txt","w")
for i in range(len(combined)):
    outFile.write(combined[i].replace("\n","") + "\n")

outFile.close()
