import sys
import re
import numpy as np

p = re.compile(r'(\w+)',re.UNICODE)

fd=open("livres/Les 3 Mousquetaires.txt")
lines=fd.readlines()
fd.close()


## make lexique
lexique=[]
for l in lines:
    lexique+=l.split(" ")
lexique_raw=list(set(lexique))

lexique=[]
for l in lexique_raw:
    m=p.search(l)
    if m:
        lexique.append(m.group(1))

lexique=list(set(lexique))
lexique.sort()

## make lexique with words of length i
max_word_length = max([len(w) for w in lexique])
lexique_dict={}
for i in np.arange(1,max_word_length+1):
    lexique_tmp =[]
    for w in lexique:
        if(len(w)==i):
            lexique_tmp.append(w)
    
    lexique_dict[i]=[s.lower() for s in list(set(lexique_tmp))]
    lexique_dict[i].sort()

## lexique lower case
lexique=[s.lower() for s in lexique]
lexique=list(set(lexique))
lexique.sort()

## make alphabet
alphabet=list(set(''.join(lexique)))
alphabet.sort()





