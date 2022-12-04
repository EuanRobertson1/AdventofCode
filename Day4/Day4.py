import array

def readFromFile():
    #open file
    file = open("Day4/input.txt")
    #get contents
    con = file.readlines()
    #close fle
    file.close()
    return con

def checkForOverlap(o,e1, e2):
    
    
    
    #e1 overlapping e2 at the start/e2 overlapping e1 at the end
    if(int(e1[0])<= int(e2[0]) and int(e1[1]) >= int(e2[0])):
        o+= 1
    #e2 overlapping e1 at the start/e1 overlapping e2 at the end
    elif(int(e2[0]) <= int(e1[0]) and int(e2[1]) >= int(e1[0])):
        o+= 1
    
    
    return o

def part1and2():
 #variables
 fullyContained = 0
 i = 0
 content = readFromFile()
 overlapSum = 0

 #loop to end of file
 while i < len(content):

  #get a list of the pair
  pair = content[i].split(',')

  #make a list for each elf containing the start and end numbers
  elf1 = pair[0].split('-')
  elf2 = pair[1].split('-')

  #check if either range is fully contained within the other
  #elf1 range is inside elf2
  if(int(elf1[0]) >= int(elf2[0]) and int(elf1[1]) <= int(elf2[1])):
    fullyContained+=1
  #elf2 range is inside elf1
  elif(int(elf2[0]) >= int(elf1[0]) and int(elf2[1]) <= int(elf1[1])):
    fullyContained+=1 

  #check for overlapping pairs
  overlapSum = checkForOverlap(overlapSum,elf1, elf2)  

  #increase counter
  i+=1
 

 
 print("According to Part 1, the number of pairs fully contained within the other is: " + str(fullyContained))
 print("According to Part 2, the number of pairs overlapping is : " + str(overlapSum))
 
#run the function
part1and2()


