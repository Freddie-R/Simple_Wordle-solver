from Getnow import *
from Notit import *
from Yellow import *
from Green import *
from Score import *
from Return import *
from average import *
from Input import *
from scorept import *
import random

word=""
do_user=True
total=1

def main(do_user,total,wordset):

    average_per_100=[5.01,4.966,4.612,4.612,4.612,5.097,5.097]
    defff=0
    for number in average_per_100:
        defff+=number
    #printer=defff/len(average_per_20)
    #print(printer)
    
    
    add_lines=""
    all_five_letter_words=get_five_letter_words()


    loop=total
    guess_total=0
    counter=0
    for theire in range(loop):
        counter+=1
        print("count: ",counter)
        print("")
        maybe=["",""]

        #pick a random 5 letter word

        if wordset=="":
            random_word=all_five_letter_words[random.randint(0,len(all_five_letter_words))]
        else:
            random_word=wordset
        #random_word=all_five_letter_words[(theire+4000)]
        #print("The random word is:",random_word)

        add_lines+=(random_word+"; ")


        #define
        letter_not_there=("")
        yellow_p=[]
        green_p=["","","","",""]
        running=True
        guess=-1
        done=False
        all_five_letter_words=get_five_letter_words()
        starting=all_five_letter_words
        while running==True:
            guess+=1

            if done==True:
                running=False
                print("It took",guess,"guesses")
                print("")
                print("-----------------------------------------------")
                print("")
                guess_total+=guess
                starting=all_five_letter_words
                add_lines+=(str(guess))
                add_lines+="\n"

            elif len(maybe)==0:
                print("It broke")

            else:
                half_way=not_it(starting, letter_not_there)

                maybe1=yellow_it(half_way,yellow_p)

                maybe=do_green(maybe1,green_p)

                yd=0
                do_it_th=False
                for i in green_p:
                    if i=="":
                        yd+=1
                if yd==1:
                    do_it_th=True
                    

                if guess==0:
                    best_word="cares"
                elif do_it_th==True and len(maybe)!=1 and 1==2:
                    print("*********************")
                    best_word=new_fun(green_p,maybe,all_five_letter_words)

                #Below if you want random valid word
                elif 1==0:
                    call=random.randint(0,len(maybe))
                    best_word=maybe[call]
                
                else:
                    best_word=(get_score(maybe))

                return_to(best_word,maybe)
                print("")

                add_lines+=(best_word+", ")
                results=user_input(best_word,letter_not_there,yellow_p,green_p,random_word,do_user)
                print("")

                letter_not_there=results[0]

                yellow_p=results[1]

                green_p=results[2]

                done=results[3]

                starting.remove(best_word)

    #with open('result.txt', 'w') as b:
        #b.write(add_lines)
    #b.close

    print("")
    print("On average it takes:",guess_total/total,"guesses")



main(do_user,total,word)