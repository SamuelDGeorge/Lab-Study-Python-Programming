

def CheckWordCount(function, test_string):
    val = function(test_string)
    sol = len(test_string.split())
    if val == sol:
        print("Your Solution Appears Correct")
        return 
    print("Your Solution Appears Incorrect")

def CheckSyllableCount(function, test):
    val = function(test)

    #calculate answer 
    sol = syllableSolution(test)
    
    if val == sol:
        print("Your Solution Appears Correct")
        return 
    print("Your Solution Appears Incorrect")


def syllableSolution(test):
    #calculate answer 
    sol = 0 

    #strip punctuation
    striped = ''
    for char in test:
        #preserve space
        if char == ' ':
            striped += ' '
            continue
        #handle dashed words
        if char == '-':
            striped += ' '
            continue
        #remove all other punctuation
        if char.isalpha():
                striped += char

    for i in striped.split():
        #lowercase all
        t = i.lower()
        #3 character words
        if len(t) <= 3:
            sol += 1
            continue 

        #handle special endings
        if t[-2:] in ['es','ed']:
            t = t[:-2]
        elif t[-1:] == 'e' and t[-2:] != 'le':
            t = t[:-1]
        
        #count remaining vowels 
        for v in ['a','e','i','o','u']:
            sol += t.count(v)
    
    return sol


        