def get_five_letter_words():
    a_file = open("all_five.txt", "r")
    almost=[]
    almostt=[]
    for line in a_file:
        stripped_line = line.strip()
        line_list = stripped_line.split()
        almost.append(line_list)

    a_file.close()

    for wordish in almost:
        for word in wordish:
            almostt.append(str(word))

    english_word_set=almostt

    all_five_letter_words=[]
    for word in english_word_set:
        do=True
        for letter in word:
            if ord(letter)<97 and ord(letter)>122:
                do = False
        if do==True:    
            all_five_letter_words.append(word.lower())
    all_five_letter_words.sort()
    pword=""
    for word in all_five_letter_words:
        if word==pword:
            all_five_letter_words.remove(word)
        pword=word
        
    return all_five_letter_words

