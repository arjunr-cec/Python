inputFile="examplefile.txt"
readFile=open(inputFile,'r')
outputFile="printoddline.txt"
writeFile=open(outputFile,'w')
ReadFileLines=readFile.readlines()
for x in range(0,len(ReadFileLines)):
    if(x%2!=0):
        writeFile.write(ReadFileLine[x])
        print(ReadFileLine[x])
    writeFile.close()
    readFile.close()
        
