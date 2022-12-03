import array
from collections import Counter

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

#make array of letters
lettersArr = list(letters)

def readFromFile():
    #open file
    file = open("Day3/input.txt")
    #get contents
    con = file.readlines()
    #close fle
    file.close()
    return con




def part1():
    #declare varibles
    sum = 0
    i = 0
    content = readFromFile()
    

    while i < len(content):
        #split string in half
        head, tail = content[i][:len(content[i])//2], content[i][len(content[i])//2:]

        #make dictionaries out of both strings then make combined dictionary
        d1 = Counter(head)
        d2 = Counter(tail)
        comDict = d1 & d2

        #make a list of the shared elements
        shared = list(comDict.elements())
        
        #get priority of shared element via index of letters array
        index = lettersArr.index(shared[0])

        #add to sum (and add 1 to compensate for array indexes starting at 0)
        index+=1
        sum+= index

        i+=1

    return sum      
        
        

            



     
   
    




p1 = part1()

print("Sum of part 1 is: " + str(p1))
