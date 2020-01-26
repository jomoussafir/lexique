## make alphabet from lexique
alphabet=list(set(''.join(lexique)))
alphabet.sort()

sys.exit(0)

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
