import sys
import re
import numpy as np



fd=open("livres/Les 3 Mousquetaires.txt")
lines=fd.readlines()
fd.close()


## lexique_raw is a sorted unique list
## of space separated words found in file
lexique_raw=[]
for l in lines:
    lexique_raw+=l.split(" ")
lexique_raw=list(set(lexique_raw))

## lexique is a sorted unique list
## of space separated unicode words found in file
## removes nbsp and \n from lexique_raw
lexique=[]
p = re.compile(r'(\w+)',re.UNICODE)
for l in lexique_raw:
    m=p.search(l)
    if m:
        lexique.append(m.group(1))

lexique=list(set(lexique))
lexique.sort()







