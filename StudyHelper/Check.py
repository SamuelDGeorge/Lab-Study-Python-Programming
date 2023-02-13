

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
    sol = 0 
    
    #define punctuation
    punc = ['.','!', ',', ':', ';', '?', 
            '[',']', '{','}',')', '(', '"', "'",'...']

    #handle dashed words
    test = test.replace('-', ' ')
    
    for i in test.split():
        #handle punctuation
        for v in punc:
            i = i.replace(v, '')

        #ignore non-words 
        if not i.isalpha():
            continue

        #lowercase all
        t = i.lower()

        #3 character words
        if len(t) <= 3:
            sol += 1
            continue 

        #ending is le
        if t[-2:] == 'le':
            sol+=1
            
        #drop special endings
        if t[-2:] in ['es','ed','le'] or t[-1:] == 'e':
            if t[-2:] in ['es','ed','le']:
                t = t[:-2]
            else:
                t = t[:-1]
        
        #count remaining vowels 
        for v in ['a','e','i','o','u']:
            sol += t.count(v)
    
    if val == sol:
        print("Your Solution Appears Correct")
        return 
    print("Your Solution Appears Incorrect")


        