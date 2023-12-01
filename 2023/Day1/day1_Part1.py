import array

#vars
curLn = 0
sum = 0 
fullNum = ""



#file handling
file = open('2023/Day1/input.txt')
fileCont = file.readlines()

#loop to end
while curLn < len(fileCont):

    lineCont = fileCont[curLn].strip()

    #find the digits
    i = 0
    firstDigit = 0
    lastDigit = 0

    while i < len(lineCont):
        if lineCont[i].isdigit():
            if firstDigit == 0:
                firstDigit = lineCont[i]
            else:
                lastDigit = lineCont[i]
        
        
        i +=1
    
    #check if only one digit is in line
    if lastDigit == 0:
        lastDigit = firstDigit


    #combine 
    fullNum = str(firstDigit) + str(lastDigit)

    #add to sum
    sum += int(fullNum)
    

    #fix vars
    curLn += 1
    

file.close()

print("Sum of all calibration values is " + str(sum))
    
            


