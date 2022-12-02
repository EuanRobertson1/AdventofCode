import array

#variables
totalScore = 0
currentLine = 0
outcomeScore = 0
shapeScore = 0


#open file
file = open("Day2/input.txt")
#get contents
fileContents = file.readlines()

#loop until end of file

while currentLine < len(fileContents):
   
   #store round
   round = fileContents[currentLine]

   #get rid of all whitespace
   round = ''.join(round.split())

   print("---------------Current Matchup " + round)
   #check for win
   if round == "AY":
    totalScore+=6
   elif round == "BZ":
    totalScore+=6
   elif round == "CX":
    totalScore+=6

    #check for Draw
   if round == "AX":
    totalScore+=3
   elif round == "BY":
    totalScore+=3
   elif round == "CZ":
    totalScore+=3

   #shape scores
   if "X" in round:
     totalScore+=1
   elif "Y" in round:
     totalScore+=2
   else:
     totalScore+=3

   
   #update variables
   currentLine+= 1


#close file
file.close()

#print total
print("Total score is: " + str(totalScore))