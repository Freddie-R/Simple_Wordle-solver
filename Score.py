import random

def get_score(list_of_words):
    get=True
    double=[]

    
    for wordssss in list_of_words:
        use_list=[]
        prew=""
        done=False
        for lettereee in wordssss:
            use_list.append(lettereee)
        use_list.sort()
        for letterss in use_list:
            if letterss==prew and done==False:
                double.append(wordssss)
                done=True
            prew=letterss
    
    while get==True:
        q1=0
        w1=0
        e1=0
        r1=0
        t1=0
        y1=0
        u1=0
        i1=0
        o1=0
        p1=0
        a1=0
        s1=0
        d1=0
        f1=0
        g1=0
        h1=0
        j1=0
        k1=0
        l1=0
        z1=0
        x1=0
        c1=0
        v1=0
        b1=0
        n1=0
        m1=0
        q2=0
        w2=0
        e2=0
        r2=0
        t2=0
        y2=0
        u2=0
        i2=0
        o2=0
        p2=0
        a2=0
        s2=0
        d2=0
        f2=0
        g2=0
        h2=0
        j2=0
        k2=0
        l2=0
        z2=0
        x2=0
        c2=0
        v2=0
        b2=0
        n2=0
        m2=0
        q3=0
        w3=0
        e3=0
        r3=0
        t3=0
        y3=0
        u3=0
        i3=0
        o3=0
        p3=0
        a3=0
        s3=0
        d3=0
        f3=0
        g3=0
        h3=0
        j3=0
        k3=0
        l3=0
        z3=0
        x3=0
        c3=0
        v3=0
        b3=0
        n3=0
        m3=0
        q4=0
        w4=0
        e4=0
        r4=0
        t4=0
        y4=0
        u4=0
        i4=0
        o4=0
        p4=0
        a4=0
        s4=0
        d4=0
        f4=0
        g4=0
        h4=0
        j4=0
        k4=0
        l4=0
        z4=0
        x4=0
        c4=0
        v4=0
        b4=0
        n4=0
        m4=0
        q5=0
        w5=0
        e5=0
        r5=0
        t5=0
        y5=0
        u5=0
        i5=0
        o5=0
        p5=0
        a5=0
        s5=0
        d5=0
        f5=0
        g5=0
        h5=0
        j5=0
        k5=0
        l5=0
        z5=0
        x5=0
        c5=0
        v5=0
        b5=0
        n5=0
        m5=0
        get=False

    for wordt in list_of_words:
        if wordt[0]=="q":
            q1+=1
        elif wordt[0]=="w":
            w1+=1
        elif wordt[0]=="e":
            e1+=1
        elif wordt[0]=="r":
            r1+=1
        elif wordt[0]=="t":
            t1+=1
        elif wordt[0]=="y":
            y1+=1
        elif wordt[0]=="u":
            u1+=1
        elif wordt[0]=="i":
            i1+=1
        elif wordt[0]=="o":
            o1+=1
        elif wordt[0]=="p":
            p1+=1
        elif wordt[0]=="a":
            a1+=1
        elif wordt[0]=="s":
            s1+=1
        elif wordt[0]=="d":
            d1+=1
        elif wordt[0]=="f":
            f1+=1
        elif wordt[0]=="g":
            g1+=1
        elif wordt[0]=="h":
            h1+=1
        elif wordt[0]=="j":
            j1+=1
        elif wordt[0]=="k":
            k1+=1
        elif wordt[0]=="l":
            l1+=1
        elif wordt[0]=="z":
            z1+=1
        elif wordt[0]=="x":
            x1+=1
        elif wordt[0]=="c":
            c1+=1
        elif wordt[0]=="v":
            v1+=1
        elif wordt[0]=="b":
            b1+=1
        elif wordt[0]=="n":
            n1+=1
        elif wordt[0]=="m":
            m1+=1
        if wordt[1]=="q":
            q2+=1
        elif wordt[1]=="w":
            w2+=1
        elif wordt[1]=="e":
            e2+=1
        elif wordt[1]=="r":
            r2+=1
        elif wordt[1]=="t":
            t2+=1
        elif wordt[1]=="y":
            y2+=1
        elif wordt[1]=="u":
            u2+=1
        elif wordt[1]=="i":
            i2+=1
        elif wordt[1]=="o":
            o2+=1
        elif wordt[1]=="p":
            p2+=1
        elif wordt[1]=="a":
            a2+=1
        elif wordt[1]=="s":
            s2+=1
        elif wordt[1]=="d":
            d2+=1
        elif wordt[1]=="f":
            f2+=1
        elif wordt[1]=="g":
            g2+=1
        elif wordt[1]=="h":
            h2+=1
        elif wordt[1]=="j":
            j2+=1
        elif wordt[1]=="k":
            k2+=1
        elif wordt[1]=="l":
            l2+=1
        elif wordt[1]=="z":
            z2+=1
        elif wordt[1]=="x":
            x2+=1
        elif wordt[1]=="c":
            c2+=1
        elif wordt[1]=="v":
            v2+=1
        elif wordt[1]=="b":
            b2+=1
        elif wordt[1]=="n":
            n2+=1
        elif wordt[1]=="m":
            m2+=1
        if wordt[2]=="q":
            q3+=1
        elif wordt[2]=="w":
            w3+=1
        elif wordt[2]=="e":
            e3+=1
        elif wordt[2]=="r":
            r3+=1
        elif wordt[2]=="t":
            t3+=1
        elif wordt[2]=="y":
            y3+=1
        elif wordt[2]=="u":
            u3+=1
        elif wordt[2]=="i":
            i3+=1
        elif wordt[2]=="o":
            o3+=1
        elif wordt[2]=="p":
            p3+=1
        elif wordt[2]=="a":
            a3+=1
        elif wordt[2]=="s":
            s3+=1
        elif wordt[2]=="d":
            d3+=1
        elif wordt[2]=="f":
            f3+=1
        elif wordt[2]=="g":
            g3+=1
        elif wordt[2]=="h":
            h3+=1
        elif wordt[2]=="j":
            j3+=1
        elif wordt[2]=="k":
            k3+=1
        elif wordt[2]=="l":
            l3+=1
        elif wordt[2]=="z":
            z3+=1
        elif wordt[2]=="x":
            x3+=1
        elif wordt[2]=="c":
            c3+=1
        elif wordt[2]=="v":
            v3+=1
        elif wordt[2]=="b":
            b3+=1
        elif wordt[2]=="n":
            n3+=1
        elif wordt[2]=="m":
            m3+=1
        if wordt[3]=="q":
            q4+=1
        elif wordt[3]=="w":
            w4+=1
        elif wordt[3]=="e":
            e4+=1
        elif wordt[3]=="r":
            r4+=1
        elif wordt[3]=="t":
            t4+=1
        elif wordt[3]=="y":
            y4+=1
        elif wordt[3]=="u":
            u4+=1
        elif wordt[3]=="i":
            i4+=1
        elif wordt[3]=="o":
            o4+=1
        elif wordt[3]=="p":
            p4+=1
        elif wordt[3]=="a":
            a4+=1
        elif wordt[3]=="s":
            s4+=1
        elif wordt[3]=="d":
            d4+=1
        elif wordt[3]=="f":
            f4+=1
        elif wordt[3]=="g":
            g4+=1
        elif wordt[3]=="h":
            h4+=1
        elif wordt[3]=="j":
            j4+=1
        elif wordt[3]=="k":
            k4+=1
        elif wordt[3]=="l":
            l4+=1
        elif wordt[3]=="z":
            z4+=1
        elif wordt[3]=="x":
            x4+=1
        elif wordt[3]=="c":
            c4+=1
        elif wordt[3]=="v":
            v4+=1
        elif wordt[3]=="b":
            b4+=1
        elif wordt[3]=="n":
            n4+=1
        elif wordt[3]=="m":
            m4+=1
        if wordt[4]=="q":
            q5+=1
        elif wordt[4]=="w":
            w5+=1
        elif wordt[4]=="e":
            e5+=1
        elif wordt[4]=="r":
            r5+=1
        elif wordt[4]=="t":
            t5+=1
        elif wordt[4]=="y":
            y5+=1
        elif wordt[4]=="u":
            u5+=1
        elif wordt[4]=="i":
            i5+=1
        elif wordt[4]=="o":
            o5+=1
        elif wordt[4]=="p":
            p5+=1
        elif wordt[4]=="a":
            a5+=1
        elif wordt[4]=="s":
            s5+=1
        elif wordt[4]=="d":
            d5+=1
        elif wordt[4]=="f":
            f5+=1
        elif wordt[4]=="g":
            g5+=1
        elif wordt[4]=="h":
            h5+=1
        elif wordt[4]=="j":
            j5+=1
        elif wordt[4]=="k":
            k5+=1
        elif wordt[4]=="l":
            l5+=1
        elif wordt[4]=="z":
            z5+=1
        elif wordt[4]=="x":
            x5+=1
        elif wordt[4]=="c":
            c5+=1
        elif wordt[4]=="v":
            v5+=1
        elif wordt[4]=="b":
            b5+=1
        elif wordt[4]=="n":
            n5+=1
        elif wordt[4]=="m":
            m5+=1
    
        
    list_of_words.sort()
    bestwords=[]
    best_word=""
    best_score=0
    for word in list_of_words:
        score=0
        if word[0]=="q":
            score+=q1
        elif word[0]=="w":
            score+=w1
        elif word[0]=="e":
            score+=e1
        elif word[0]=="r":
            score+=r1
        elif word[0]=="t":
            score+=t1
        elif word[0]=="y":
            score+=y1
        elif word[0]=="u":
            score+=u1
        elif word[0]=="i":
            score+=i1
        elif word[0]=="o":
            score+=o1
        elif word[0]=="p":
            score+=p1
        elif word[0]=="a":
            score+=a1
        elif word[0]=="s":
            score+=s1
        elif word[0]=="d":
            score+=d1
        elif word[0]=="f":
            score+=f1
        elif word[0]=="g":
            score+=g1
        elif word[0]=="h":
            score+=h1
        elif word[0]=="j":
            score+=j1
        elif word[0]=="k":
            score+=k1
        elif word[0]=="l":
            score+=l1
        elif word[0]=="z":
            score+=z1
        elif word[0]=="x":
            score+=x1
        elif word[0]=="c":
            score+=c1
        elif word[0]=="v":
            score+=v1
        elif word[0]=="b":
            score+=b1
        elif word[0]=="n":
            score+=n1
        elif word[0]=="m":
            score+=m1
        if word[1]=="q":
            score+=q2
        elif word[1]=="w":
            score+=w2
        elif word[1]=="e":
            score+=e2
        elif word[1]=="r":
            score+=r2
        elif word[1]=="t":
            score+=t2
        elif word[1]=="y":
            score+=y2
        elif word[1]=="u":
            score+=u2
        elif word[1]=="i":
            score+=i2
        elif word[1]=="o":
            score+=o2
        elif word[1]=="p":
            score+=p2
        elif word[1]=="a":
            score+=a2
        elif word[1]=="s":
            score+=s2
        elif word[1]=="d":
            score+=d2
        elif word[1]=="f":
            score+=f2
        elif word[1]=="g":
            score+=g2
        elif word[1]=="h":
            score+=h2
        elif word[1]=="j":
            score+=j2
        elif word[1]=="k":
            score+=k2
        elif word[1]=="l":
            score+=l2
        elif word[1]=="z":
            score+=z2
        elif word[1]=="x":
            score+=x2
        elif word[1]=="c":
            score+=c2
        elif word[1]=="v":
            score+=v2
        elif word[1]=="b":
            score+=b2
        elif word[1]=="n":
            score+=n2
        elif word[1]=="m":
            score+=m2
        if word[2]=="q":
            score+=q3
        elif word[2]=="w":
            score+=w3
        elif word[2]=="e":
            score+=e3
        elif word[2]=="r":
            score+=r3
        elif word[2]=="t":
            score+=t3
        elif word[2]=="y":
            score+=y3
        elif word[2]=="u":
            score+=u3
        elif word[2]=="i":
            score+=i3
        elif word[2]=="o":
            score+=o3
        elif word[2]=="p":
            score+=p3
        elif word[2]=="a":
            score+=a3
        elif word[2]=="s":
            score+=s3
        elif word[2]=="d":
            score+=d3
        elif word[2]=="f":
            score+=f3
        elif word[2]=="g":
            score+=g3
        elif word[2]=="h":
            score+=h3
        elif word[2]=="j":
            score+=j3
        elif word[2]=="k":
            score+=k3
        elif word[2]=="l":
            score+=l3
        elif word[2]=="z":
            score+=z3
        elif word[2]=="x":
            score+=x3
        elif word[2]=="c":
            score+=c3
        elif word[2]=="v":
            score+=v3
        elif word[2]=="b":
            score+=b3
        elif word[2]=="n":
            score+=n3
        elif word[2]=="m":
            score+=m3
        if word[3]=="q":
            score+=q4
        elif word[3]=="w":
            score+=w4
        elif word[3]=="e":
            score+=e4
        elif word[3]=="r":
            score+=r4
        elif word[3]=="t":
            score+=t4
        elif word[3]=="y":
            score+=y4
        elif word[3]=="u":
            score+=u4
        elif word[3]=="i":
            score+=i4
        elif word[3]=="o":
            score+=o4
        elif word[3]=="p":
            score+=p4
        elif word[3]=="a":
            score+=a4
        elif word[3]=="s":
            score+=s4
        elif word[3]=="d":
            score+=d4
        elif word[3]=="f":
            score+=f4
        elif word[3]=="g":
            score+=g4
        elif word[3]=="h":
            score+=h4
        elif word[3]=="j":
            score+=j4
        elif word[3]=="k":
            score+=k4
        elif word[3]=="l":
            score+=l4
        elif word[3]=="z":
            score+=z4
        elif word[3]=="x":
            score+=x4
        elif word[3]=="c":
            score+=c4
        elif word[3]=="v":
            score+=v4
        elif word[3]=="b":
            score+=b4
        elif word[3]=="n":
            score+=n4
        elif word[3]=="m":
            score+=m4
        if word[4]=="q":
            score+=q5
        elif word[4]=="w":
            score+=w5
        elif word[4]=="e":
            score+=e5
        elif word[4]=="r":
            score+=r5
        elif word[4]=="t":
            score+=t5
        elif word[4]=="y":
            score+=y5
        elif word[4]=="u":
            score+=u5
        elif word[4]=="i":
            score+=i5
        elif word[4]=="o":
            score+=o5
        elif word[4]=="p":
            score+=p5
        elif word[4]=="a":
            score+=a5
        elif word[4]=="s":
            score+=s5
        elif word[4]=="d":
            score+=d5
        elif word[4]=="f":
            score+=f5
        elif word[4]=="g":
            score+=g5
        elif word[4]=="h":
            score+=h5
        elif word[4]=="j":
            score+=j5
        elif word[4]=="k":
            score+=k5
        elif word[4]=="l":
            score+=l5
        elif word[4]=="z":
            score+=z5
        elif word[4]=="x":
            score+=x5
        elif word[4]=="c":
            score+=c5
        elif word[4]=="v":
            score+=v5
        elif word[4]=="b":
            score+=b5
        elif word[4]=="n":
            score+=n5
        elif word[4]=="m":
            score+=m5

        if word in double:
            score=score*0.6

        #best_score=1000

        
        if score>=best_score:
            prebs=best_score
            best_score=score
            bestword=word
            if prebs==score:
                bestwords.append(bestword)
            else:
                bestwords=[bestword]
    call=random.randint(0,(len(bestwords)-1))
    best_word=bestwords[call]
    
    return best_word