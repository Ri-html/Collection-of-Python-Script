'''
AUTHOR: HARRY
DESCRIPTION: TEST WHETHER X AND Y HEXIDECIMAL ARE REVERSE OF EACH OTHER
SCENARIO:
    1. TYPE THE HEXIDECIMAL IN X
    2. TYPE THE HEXIDECIMAL YOU THINK IS THE REVERSE IN Y
    3. RUN THE PROGRAM
    4. YOU WILL GET WHETHER THEY ARE REVERSED BITS OF EACH OTHER
'''

def decToBin(num):
    bina=""
    while num!=0:
        bina+=str(num%2)
        num//=2
    bina=bina[::-1]
    lens=len(bina)
    if lens<4:
        bina=(4-lens)*"0"+bina
    return bina

def hexToDec(hexa):
    ALPH='ABCDEF'
    if hexa.isalpha():
        return 10+ALPH.index(hexa)
    else:
        return int(hexa)

def hexToBin(hexa):
    bina=""
    for ch in hexa:
        dec=hexToDec(ch)
        bina+=decToBin(dec)
    return bina

x='01FF01FF'
x1=hexToBin(x)

y='FF80FF80'
y1=hexToBin(y)
print(x1)
print(y1[::-1])
print(x1==y1[::-1])

