'''
Author: Harry He
Description: A simple python script to turn classes into format fit to be put into UML
Steps:
    1. Open the text.txt file
    2. paste the class into the text.txt file
    3. save the text.txt file
    4. run this code
    5. the code should be in the text_revised.txt file in the same folder as this code

Postconditions
    1. The transformed code does not have package protected fields
    2. Might have modifier that I missed
    3. Did this with Java code in mind so might not be the same with other codes
'''
import copy

# check if certain modifiers are in the line of code and remove the modifier from list
# @line an list containing line of code with public, private, and protected modifier
def filterForModifiers(line):
    aLine=copy.deepcopy(line)
    ifStatic = False
    ifAbstract = False
    ifFinal = False
    ifSynchronize = False

    for i,word in enumerate(reversed(aLine)):
        index= len(line)-i-1
        if word == "static":
            ifStatic = True
            del line[index]
            
        elif word == "abstract":
            ifAbstract = True
            del line[index]
            
        elif word == "final":
            ifFinal = True
            del line[index]
            
        elif word == "synchronized":
            ifSynchronize = True
            del line[index]
            
    return [ifStatic, ifAbstract, ifFinal, ifSynchronize]




# copy the lines of the code into an array
arr = []
file = open("text.txt","r")
for lines in file:
    arr.append(lines)
file.close()


#operating on the data stored in array and pasting the result in another file
keywords = ["public","protected","private"]
modifiers = ["static", "abstract", "final", "synchronized"]
file = open("text_revised.txt","w")

for lines in arr:
    line = lines.split()  #this would split out the keywords, field/method name and other important info

    if (len(line) == 0):   #skipping empty lines
        continue

    if line[0] in keywords:

        linend = -1  #states the end of line when copying copying
        lineToWrite = ""
        dataType = None
        checkModifier = filterForModifiers(line)

        if "(" not in line[1]:
            dataType= line.pop(1)

        #adding the access modifier to the UML spaces incorporated for what is after
        if(line[0] == "public"):
            lineToWrite += "+ "
            
        elif(line[0] == "protected"):
            lineToWrite += "# "
            
        else:
            lineToWrite += "- "
            
        #adding the other modifier in UML
        if checkModifier[2] == True:
            lineToWrite += "final "
            
        if checkModifier[0] == True:
            lineToWrite+= "_"   #static directly connects to the method name
            
        if checkModifier[1] == True:
            file.write("<<abstract>>\n")
            
        if checkModifier[3] == True:
            file.write("<<synchronized>>\n")
            
        #adding the name and any extension or implementation
        rest = " ".join(line[1:])

        if "=" in rest: #removing '=' and anything behind it in the field
            rest = rest[:rest.index("=")]
        else: #removing common unwanted noise
            rest = [x for x in rest if x not in "{;"]

        lineToWrite += "".join(rest)

        #adding in the data type and printing line
        if dataType != None:
            lineToWrite += ":" + dataType
        file.write(lineToWrite + "\n")
        
    elif line[0]=="@Override":
        file.write(line[0]+"\n")
file.close()
