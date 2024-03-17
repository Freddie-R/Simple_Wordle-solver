def new_fun(green,maybe,all_five_letter_words):
    best_score=0
    letters_to_check=[]
    place=green.index("")
    for i in maybe:
        letters_to_check.append(i[place])
    for word in all_five_letter_words:
        score=0
        ltc=letters_to_check
        for letter in word:
            if letter in letters_to_check:
                score+=1
                ltc.remove(letter)
                print(ltc)
        if score>best_score:
            best_score=score
            best_word=word
    return best_word