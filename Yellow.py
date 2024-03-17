def yellow_it(half_way,yellow):
    result=[]
    letters=[]
    mid_way=half_way

    if len(yellow)>0:
        for thingy in yellow:
            letters.append(thingy[0])

    
    for word in half_way:
        done=False
        for thing in yellow:
            letter=thing[0]
            place=((int(thing[1]))-1)
            if word[place]==letter and done==False:
                mid_way.remove(word)
                done=True

    almost=[]
    
    #===============
    for word in mid_way:
        score=0
        total=len(yellow)
        for letter in letters:
            for letteri in word:
                if letter==letteri:
                    score+=1
        if score>=total:
            almost.append(word)

    #=================
    alp=almost
    
    for word in almost:
        for strange in yellow:
            not_letter=strange[0]
            not_place=(int(strange[1]))-1
            if word in alp:
                if word[not_place]==not_letter:
                    alp.remove(word)
                    
    result=alp
    
    return result
        