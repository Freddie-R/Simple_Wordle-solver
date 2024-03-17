def do_green(current,green):
    
    g1=green[0]
    g2=green[1]
    g3=green[2]
    g4=green[3]
    g5=green[4]
    
    result=[]
    for word in current:
        score=0
        if len(g1)>0:
            if g1[0]==word[0]:
                score+=1
        if len(g2)>0:
            if g2[0]==word[1]:
                score+=1
        if len(g3)>0:
            if g3[0]==word[2]:
                score+=1
        if len(g4)>0:
            if g4[0]==word[3]:
                score+=1
        if len(g5)>0:
            if g5[0]==word[4]:
                score+=1
        if score>=((len(g1))+(len(g2))+(len(g3))+(len(g4))+(len(g5))):
            result.append(word)
    return result