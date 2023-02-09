

def Check(function, test_string):
    val = function(test_string)
    sol = len(test_string.split())
    if val == sol:
        print("Your Solution Appears Correct")
        return 
    print("Your Solution Appears Incorrect")