import re
curLn = 0
values = [12,13,14]
colors = ['red','green','blue']
sum = 0


#file handling
file = open('2023/Day2/input.txt')
fileCont = file.readlines()

#loop to end
while curLn < len(fileCont):
    possible = True
    

    #get line content
    lineCont = re.split(';|,|:', fileCont[curLn])

    #get current game
    curGame = int(''.join(re.findall(r'\b\d+\b',lineCont[0])))
    print("current game is",curGame)

    
    i = 0
    while i < len(lineCont):
        x = 0
        
        while x < len(colors):
            if colors[x] in lineCont[i]:
                
                colorIndex = x
                #get the int value 
                n = int(''.join(re.findall(r'\b\d+\b',lineCont[i])))
                
                #check if number is possible
                if n <= values[x]:
                    print(n, "is possible as it is <=", values[x])
                elif n > values[x]:
                    print(n, "is impossible as it is >", values[x])
                    possible = False
                
            x+=1

        i+=1        

    
    if(possible):
        sum+=curGame   
        print("Overall Game:", curGame, "is possible")   
    else:
        print("Overall Game:", curGame, "is impossible")

    print('\n')
     
    curLn+=1

file.close()

print("Sum of all values is ",sum)