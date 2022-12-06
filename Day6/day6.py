
def readFromFile():
    #open file
    file = open("Day6/input.txt")
    #get contents
    con = file.readlines()
    #close fle
    file.close()
    return con

def isUnique(string):
    #for storing checked charactecrs
    chars = []
    #check each character
    for s in string:
        #if it exists in checked character list return false otherwise add it to the list
        if s in chars:
            return False
        else:
            chars.append(s)
    #return true if all characters checked without one being the same
    return True

def p1():
 #read file
 content = str(readFromFile())
 #tidy up variable
 content = content.replace("'","")
 
 #variables
 index = 0
 x = 4
 unique = False

 while x < len(content):
  
  #create a variable containing the last 4 characters
  setOf4 = ""
  c = 0
  while c < 4:
     setOf4 = setOf4 + content[x-c]
     c+=1

  #check if most recent 4 are unique
  unique = isUnique(setOf4)
  
  #if they are, store index and exit loop otherwise keep iterating
  if unique == True:
    index = x
    break
  else:
    x+=1



 print("P1 Characters processed: " + str(index)) 
       
def p2():
 #read file
 content = str(readFromFile())
 #tidy up variable
 content = content.replace("'","")
 
 #variables
 index = 0
 x = 14
 
 unique = False 
 

 while x < len(content):
    setOf14 = ""
    c = 0
    while c < 14:
     setOf14 = setOf14 + content[x-c]
     c+=1
    
 #check if most recent 14 are unique
    unique = isUnique(setOf14)
 #if they are, store index and exit loop otherwise keep iterating
    if unique == True:
     index = x
     break
    else:
      x+=1

 print("P2 Characters processed: " + str(index))       
    
    

    
p1()
p2()