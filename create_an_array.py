"""
    This is a script to make it easier to create an array in Java
"""

def addPar(word):
    return "{%s}"%(word)

def addClass(word, className):
    return "new %s(%s)"%(className,word)

aClassName=""


print("What is the type of item put into the array?")
print("1. objects")
print("2. strings")
print("3. raw value")

choice=input()
if choice=="1":
    print("please input the object name")
    aClassName=input()


word=""

print("type to value you want to input into the list. Use -1 to end the loop")

#loops to add item into the list, ends when the user types \0
item=input()
while(item!="-1"):
    if choice=="1":
        item=addClass(item, aClassName)
    elif choice=="2":
        item='"%s"'%item
    word+=item+","
    item=input()

word=word[:-1]  #removing the extra comma at the end
word=addPar(word)   #adds the parenthesis that makes it an array in java


print(word)
item=input()    #added so that the program does not quit immediately
