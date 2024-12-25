"""
	This is a python script to filter out use cases from a paragraph
"""
arr=[]
file=open("text.txt","r", encoding='utf-8')
for lines in file:
    if "Use Case:" in lines:
        arr.append(lines)
    if "Use case:" in lines:
        arr.append(lines)

file.close()

file=open("text_revised.txt","w", encoding='utf-8')
file.write(str(len(arr)))
for lines in arr:
    file.write(lines)
file.close()
