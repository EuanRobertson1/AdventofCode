import array

#vars
curLn = 0
sum = 0 
fullNum = ""


stringNums = ["one","two","three","four","five","six","seven","eight","nine"]

stringNumChecker = ""

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

        
        stringNumChecker += lineCont[i]
        
        
        x = 0
        #check if current str held in stringNumCheck matches any of the  values in each stringNums index
        while x < len(stringNums):
            if stringNums[x] in stringNumChecker:
               if firstDigit == 0:
                firstDigit = x +1
                
               else:
                lastDigit = x +1
                
               
               stringNumChecker = ""

               #allows for shared letters for word numbers
               i-=1
               
               
                
            
            x+=1
        
        if lineCont[i].isdigit():
            #reset stringNumChecker
            stringNumChecker = ""

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
    print(fullNum)

    #add to sum
    sum += int(fullNum)
    

    #fix vars
    curLn += 1
    stringNumChecker = ""
    

file.close()

print("Sum of all calibration values is " + str(sum))
    
            


