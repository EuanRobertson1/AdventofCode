
def readFromFile():
    #open file
    file = open("Day2/input.txt")
    #get contents
    con = file.readlines()
    #close fle
    file.close()
    return con

def part1():
    #variables
    t = 0
    i = 0

    file = readFromFile()

    #loop until end of file
    while i < len(file):
    
     #store line
     line = file[i]

     #get rid of all whitespace
     line = ''.join(line.split())

     
     #check for win and add 6 if won
     if line in ["AY","BZ","CX"]:
        t+=6
     
     #check for Draw and add 3 if drawn
     if line in ["AX","BY","CZ"]:
        t+=3
    
     #add relevant score for each shape
     if "X" in line:
        t+=1
     elif "Y" in line:
        t+=2
     else:
        t+=3

     #increase counter
     i+= 1

    #return the result
    return t

def part2():
 #variables
 t = 0
 i = 0
 
 file = readFromFile()

 #loop until end of file
 while i < len(file):
  
  #store line
  line = file[i]
  
  #get rid of all whitespace
  line = ''.join(line.split())
  
  #check if told to loose and add points based on which losing shape you chose
  if "X" in line:
    if "A" in line:
     t+=3
    elif "B" in line:
     t+=1
    elif "C" in line:
     t+=2
     
  #check if told to Draw and add points based on the draw + which drawing shape you chose
  if "Y" in line:
    if "A" in line:
     t+=4
    elif "B" in line:
      t+=5
    elif "C" in line:
      t+=6      
    
  #check if told to Win and add points based on the Win + which Winning shape you chose
  if "Z" in line:
    if "A" in line:
     t+=8
    elif "B" in line:
      t+=9
    elif "C" in line:
      t+=7 
     
  #increase counter
  
  i+=1
    
 return t


#Part 1 
p1= part1()
print("Total score according to Part 1 is: " + str(p1))

#Part 2
p2 = part2()
print("Total score according to Part 2 is: " + str(p2))



