import re 

sum = 0
curLn = 0
totalScratchcards = 0

#file handling
file = open('2023/Day4/test.txt')
fileCont = file.readlines()

#loop to end
while curLn < len(fileCont):

    points = 0
    wins = 0

   #get line content
    lineCont = re.split('[:|]', fileCont[curLn])
    #get the nums 
    winningNums = lineCont[1].split()
    elfNums = lineCont[2].split()
    
    #count the wins
    i=0
    while i < len(winningNums):
       p=0
       while p < len(elfNums):
           if winningNums[i] == elfNums[p]:
               wins+=1 
               

           p+=1
           
    
       i+=1


    #calcualte the points     
    if wins == 1:
        points = 1
    elif wins > 1:
       points = 1
       wins -=1

       while wins > 0:
           points = points * 2
           wins -=1

    sum += points

    curLn+=1


file.close()



print("Number of wins is", sum)