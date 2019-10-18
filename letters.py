# Python implementation of Rosetta Code Task 
# http://rosettacode.org/wiki/Four_is_the_number_of_letters_in_the_...
# Uses inflect
# https://pypi.org/project/inflect/

import inflect

def count_letters(word):
    """
    count letters ignore , or -
    """
    count = 0
    for letter in word:
        if letter != ',' and letter !='-':
            count += 1
            
    return count

def build_sentence(p, max_words):
    """
    
    Builds at most max_words of the task following the pattern:
    
    Four is the number of letters in the first word of this sentence, two in the second,
    three in the third, six in the fourth, two in the fifth, seven in the sixth,
    
    """
    
    # start with first part of sentence up first comma
    
    sentence = "Four is the number of letters in the first word of this sentence"
    
    # save as list also for easy counting
    
    sentence_list = sentence.split()
    
    num_words = 13
    
    # which word number we are doing next
    # two/second is first one in loop
    
    word_number = 2
    
    # loop until sentance is at least as long as needs be
    
    while num_words < max_words:
        # Build something like
        # ,two in the second
        
        # get second or whatever we are on
        
        ordinal_string = p.number_to_words(p.ordinal(word_number))
        
        # get two or whatever the length is of the word_number word
        
        word_number_string = p.number_to_words(len(sentence_list[word_number - 1]))
        
        # sentence addition
        
        new_string = ", "+word_number_string+" in the "+ordinal_string
        
        new_list = new_string.split()
        
        # update main sentence
        
        sentence += new_string
        
        # update sentence list
        
        sentence_list += new_list
        
        # add new word count
        
        num_words += len(new_list)
        
        # increment word number
        
        word_number += 1
        
    return sentence, sentence_list, num_words
    
p = inflect.engine()

sentence, sentence_list, num_words = build_sentence(p, 201)

print("The lengths of the first 201 words are:")
print(" ")

print('{0:3d}:  '.format(1),end='')
for word_index in range(201):
    print('{0:2d}'.format(count_letters(sentence_list[word_index])),end='')
    if (word_index+1) % 20 == 0:
        # newline every 20
        print(" ")
        print('{0:3d}:  '.format(word_index + 2),end='')
    else:
        print(" ",end='')
        

