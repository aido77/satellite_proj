from requests import bigData
def stringSplit():
    newData = bigData #creates new variable to be manipulated whilst preserving bigData
    lineBreak = newData.find("\r\n")
    lineCount = 0 #iterative amount of linebreaks [3 needed to split up into seperate full satellite data]
#\r\n indicates linebreak
    while lineBreak != -1:
        if lineCount == 3: #if the satellite data is over i.e. three rows have passed
            newData = newData.split("\r\n",1) #only splits once
            lineCount = 0 #resets line counter
        else:
            newData[lineBreak:lineBreak+3] == "" #if satellite data is STILL ONGOING, replace with "" so it doesnt get picked up again
            lineCount = lineCount + 1 #iterates linecount   
            #bigData is now newData
    print(newData)
stringSplit()