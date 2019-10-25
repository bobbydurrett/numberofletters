# Python implementation of Rosetta Code Task 
# http://rosettacode.org/wiki/Four_is_the_number_of_letters_in_the_...
# Uses inflect
# https://pypi.org/project/inflect/

import inflect

def count_letters(word):
    """
    count letters ignore , or -, or space
    """
    count = 0
    for letter in word:
        if letter != ',' and letter !='-' and letter !=' ':
            count += 1
            
    return count
    
def split_with_spaces(sentence):
    """
    Takes string with partial sentence and returns
    list of words with spaces included.
    
    Leading space is attached to first word.
    Later spaces attached to prior word.
    """
    sentence_list = []
    curr_word = ""
    for c in sentence:
        if c == " " and curr_word != "":
            # append space to end of non-empty words
            # assumed no more than 1 consecutive space.
            sentence_list.append(curr_word+" ")
            curr_word = ""
        else:
            curr_word += c
    
    # add trailing word that does not end with a space        
    
    if len(curr_word) > 0:
        sentence_list.append(curr_word)
    
    return sentence_list
        
def build_sentence(p, max_words):
    """
    
    Builds at most max_words of the task following the pattern:
    
    Four is the number of letters in the first word of this sentence, two in the second,
    three in the third, six in the fourth, two in the fifth, seven in the sixth,
    
    """
    
    # start with first part of sentence up first comma as a list
    
    sentence_list = split_with_spaces("Four is the number of letters in the first word of this sentence,")
      
    num_words = 13
    
    # which word number we are doing next
    # two/second is first one in loop
    
    word_number = 2
    
    # loop until sentance is at least as long as needs be
    
    while num_words < max_words:
        # Build something like
        # ,two in the second
        
        # get second or whatever we are on
        
        ordinal_string = p.number_to_words(p.ordinal(word_number), andword='')
        
        # get two or whatever the length is of the word_number word
        
        word_number_string = p.number_to_words(count_letters(sentence_list[word_number - 1]), andword='')
        
        # sentence addition
        
        new_string = " "+word_number_string+" in the "+ordinal_string+","

        new_list = split_with_spaces(new_string)
        
        sentence_list += new_list

        # add new word count
        
        num_words += len(new_list)
        
        # increment word number
        
        word_number += 1
        
    return sentence_list, num_words
    
def word_and_counts(word_num):
    """
    
    Print's lines like this:
    
    Word     1000 is "in", with 2 letters.  Length of sentence so far: 6279

    """
        
    sentence_list, num_words = build_sentence(p, word_num)
    
    word_str = sentence_list[word_num - 1].strip(' ,')
    
    num_letters = len(word_str)
    
    num_characters = 0
    
    for word in sentence_list:
       num_characters += len(word)
       
    print('Word {0:8d} is "{1}", with {2} letters.  Length of the sentence so far: {3}  '.format(word_num,word_str,num_letters,num_characters))
   
    
p = inflect.engine()

sentence_list, num_words = build_sentence(p, 201)

print(" ")
print("The lengths of the first 201 words are:")
print(" ")

print('{0:3d}:  '.format(1),end='')

total_characters = 0

for word_index in range(201):

    word_length = count_letters(sentence_list[word_index])
    
    total_characters += len(sentence_list[word_index])
    
    print('{0:2d}'.format(word_length),end='')
    if (word_index+1) % 20 == 0:
        # newline every 20
        print(" ")
        print('{0:3d}:  '.format(word_index + 2),end='')
    else:
        print(" ",end='')
 
print(" ")
print(" ")
print("Length of sentence so far: "+str(total_characters))
print(" ")

"""

Expected output this part:

Word     1000 is "in", with 2 letters.  Length of sentence so far: 6279
Word    10000 is "in", with 2 letters.  Length of sentence so far: 64140
Word   100000 is "one", with 3 letters.  Length of sentence so far: 659474
Word  1000000 is "the", with 3 letters.  Length of sentence so far: 7113621
Word 10000000 is "thousand", with 8 letters.  Length of sentence so far: 70995756

"""

#word_and_counts(1000)
#word_and_counts(10000)
#word_and_counts(100000)
#word_and_counts(1000000)
#word_and_counts(10000000)

"""
sentence_list, num_words = build_sentence(p, 1000)

num_characters = 0

print(" ")

for i in range(1000):
    curr_word = sentence_list[i]
    num_characters += len(curr_word)
    print(str(i+1)+":"+curr_word+":"+str(num_characters))
    
print(" ")
"""

# talk has full text of 2202 word string

#word_and_counts(2202)

sentence_list, num_words = build_sentence(p, 2202)

full_sentence = ""

for i in range(2202):
    full_sentence += sentence_list[i]
    
num_hundred_lines = len(full_sentence) // 100

length_remainder = len(full_sentence) % 100

print('1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890')

for i in range(num_hundred_lines):
    print(full_sentence[i*100:i*100+100])
    
print(full_sentence[(num_hundred_lines-1)*100+100:])

