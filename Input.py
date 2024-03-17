def user_input(last_guess, letter_not_there,yellow_p,green_p,random_word,do_user):
    done=False

    #pick wether to do it yourself or bot

    letter1=last_guess[0]
    letter2=last_guess[1]
    letter3=last_guess[2]
    letter4=last_guess[3]
    letter5=last_guess[4]

    #print("Enter the result of your guess like below;")
    #print("0 for gray")
    #print("1 for yellow")
    #print("2 for green")
    #print("e.g. 00120")

    if do_user==True:
        user_result=input(": ")
    else:
        user_result=""
        if random_word[0]==last_guess[0]:
            user_result+="2"
        elif last_guess[0] in random_word:
            user_result+="1"
        else:
            user_result+="0"
        
        if random_word[1]==last_guess[1]:
            user_result+="2"
        elif last_guess[1] in random_word:
            user_result+="1"
        else:
            user_result+="0"

        if random_word[2]==last_guess[2]:
            user_result+="2"
        elif last_guess[2] in random_word:
            user_result+="1"
        else:
            user_result+="0"

        if random_word[3]==last_guess[3]:
            user_result+="2"
        elif last_guess[3] in random_word:
            user_result+="1"
        else:
            user_result+="0"

        if random_word[4]==last_guess[4]:
            user_result+="2"
        elif last_guess[4] in random_word:
            user_result+="1"
        else:
            user_result+="0"
        #####print(user_result)

    if user_result=="22222":
        done=True
    if int(user_result[0])==2:
        green_p[0]=letter1
    elif int(user_result[0])==1:
        letter1+="1"
        yellow_p.append(letter1)
    else:
        letter_not_there+=letter1

    if int(user_result[1])==2:
        green_p[1]=letter2
    elif int(user_result[1])==1:
        letter2+="2"
        yellow_p.append(letter2)
    else:
        letter_not_there+=letter2

    if int(user_result[2])==2:
        green_p[2]=letter3
    elif int(user_result[2])==1:
        letter3+="3"
        yellow_p.append(letter3)
    else:
        letter_not_there+=letter3

    if int(user_result[3])==2:
        green_p[3]=letter4
    elif int(user_result[3])==1:
        letter4+="4"
        yellow_p.append(letter4)
    else:
        letter_not_there+=letter4

    if int(user_result[4])==2:
        green_p[4]=letter5
    elif int(user_result[4])==1:
        letter5+="5"
        yellow_p.append(letter5)
    else:
        letter_not_there+=letter5

    return_thin=[letter_not_there,yellow_p,green_p,done]
    return return_thin
        