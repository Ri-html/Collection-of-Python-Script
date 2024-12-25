"""
this function converts an list of option into a switch case

the list in this case
{
                "add income category","add expense category",
                "select income category","select expense category",
                "get User's largest expense", "get sorted list of expense by category",
                "display money until saving goal"}
without any next line as it could only take in strings
"""
def getRawSentence(string):
    string2=""
    printToString2=False
    for i,items in enumerate(string):
        if printToString2:
            string2+=items
        if items=='"':
            printToString2=True if printToString2==False else False
    return string2[:-1]

def toSwitchCase(arr):
    option=input("What type of options?")
    startsAt=int(input("What value does your case start at"))
    print("switch(%s){"%(option))
    for i,options in enumerate(arr):
        option=getRawSentence(options)
        print("\tcase %s:"%(i+startsAt))
        print("\t\t//add option %s"%(options))
        print("\t\tbreak;\n")
    print("}")
    

arr=input().split(",")
toSwitchCase(arr)


    
