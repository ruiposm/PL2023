import sys
import re

ligado = False
r = 0

for l in sys.stdin:
    if res := re.findall(r'(\d+)', l):
        if(ligado):
            for num in res:
                r = r + int(num)
    elif (re.search(r'on', l, flags = re.IGNORECASE)):
        ligado = True
        print("On")
    elif (re.search(r'off', l, flags = re.IGNORECASE)):
        ligado = False
        print("Off")
    elif (re.search(r'=', l)):
        print("Soma = ", r)
    
print("O resultado da soma é: ", r)