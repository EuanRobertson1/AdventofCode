import array
#init variables
currentLine = 0
total = 0
HighestTotal = 0
elfCounter = 0
topThreeTotal = 0
topThree = [0,0,0] 


#open the file 
file = open('Day1/input.txt')

#get contents 
fileContent = file.readlines()

#loop until end of file
while currentLine < len(fileContent):
#check if line is blank
 if fileContent[currentLine].strip():
    total += int(fileContent[currentLine])
    currentLine+= 1
 else:
    #check if total is higher than highest total
    print(str(total))
    if total > HighestTotal:
        #update highest total
        HighestTotal = total

        #move current 1st in top 3 Array to 2nd
        topThree[1] = topThree [0]
        topThree[0] = total
        


    #check if total makes it into 2nd or 3rd
    if HighestTotal > total > topThree[1]:#2nd
        #move current 2nd to third
        topThree[2] = topThree[1]
        #assign new second
        topThree[1] = total
    elif topThree[1] > total > topThree[2]:#3rd
        #assign new third
        topThree[2] = total 

    #reset total and add to counters
    total = 0
    currentLine +=1
    elfCounter +=1


#close file
file.close()
#get the total of the top 3
for i in range(0,len(topThree)):
    topThreeTotal += topThree[i]

#print results
print("Highest total was elf " + str(elfCounter) + " with " + str(HighestTotal) + " Calories!")
print("The top three highest calories were\n1st: " + str(topThree[0]) + "\n2nd: " + str(topThree[1]) + "\n3rd: " + str(topThree[2]))
print("The total of the top 3 is: " + str(topThreeTotal))
