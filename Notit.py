def not_it(all_five_letter_words,letters_not_there):
    if letters_not_there!="":
        letter_not_there=[]
        for letter in letters_not_there:
            letter_not_there.append(letter)
        possibily = []
        for word in all_five_letter_words:
            insert=True
            for letter in word:
                for nletter in letter_not_there:
                    if nletter==letter:
                        insert=False
            if insert==True:
                possibily.append(word)
    else:
        possibily=all_five_letter_words
    return(possibily)