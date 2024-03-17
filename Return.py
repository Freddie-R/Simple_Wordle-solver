def return_to(best_word,list):
    if (len(list))!=1:
        print("There is a possiibility of",len(list),"words")
        print("")
        print("I suggest you guess:", best_word)
    elif (len(list))==0:
        print("IT BROKE AGAIN!!!!!!!!!!!!!")
    else:
        print("There is only:",best_word,":left")