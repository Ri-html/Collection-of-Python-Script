"""
This template is designed for any future code that involves reading from a file, modifying its contents, and saving the revised version to another file.

Workflow:
1. The program will read the contents from an existing text file, "text.txt".
2. The revised content will be stored in a list called `arr`.
3. The modified content will then be written into a new file called "text_revised.txt".

Instructions:
- Replace the comment `#your code goes here` with your logic to modify the contents of the file.
- The list `arr` will contain the revised content. Ensure that after processing, all modified lines are added to this list.

Notes:
- Make sure to handle file reading and writing appropriately to avoid any data loss.
- The code assumes that the file "text.txt" exists and is in the same directory as the script.

"""

arr=[]
file=open("text.txt","r")
for lines in file:

#your code goes here

file.close()

file=open("text_revised.txt","w")
for lines in arr:
    file.write(lines+"\n")
file.close()
