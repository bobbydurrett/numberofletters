# numberofletters
Python implementation of Rosetta Code task "Four is the number of letters in the ..."

http://rosettacode.org/wiki/Four_is_the_number_of_letters_in_the_...

I think I can use the same approach as in https://github.com/bobbydurrett/ebannumbers

inflect module generates english for numbers. probably slow but should be easy to
code.

Output so far:

The lengths of the first 201 words are:

  1:   4  2  3  6  2  7  2  3  5  4  2  4  8  3  2  3  6  5  2  3
 21:   5  3  2  3  6  3  2  3  5  5  2  3  5  3  2  3  7  5  2  3
 41:   6  4  2  3  5  4  2  3  5  3  2  3  8  4  2  3  7  5  2  3
 61:  10  5  2  3 10  3  2  3  9  5  2  3  9  3  2  3 11  4  2  3
 81:  10  3  2  3 10  5  2  3  9  4  2  3 11  5  2  3 12  3  2  3
101:  11  5  2  3 12  3  2  3 11  5  2  3 11  3  2  3 13  5  2  3
121:  12  4  2  3 11  4  2  3  9  3  2  3 11  5  2  3 12  4  2  3
141:  11  5  2  3 12  3  2  3 11  5  2  3 11  5  2  3 13  4  2  3
161:  12  3  2  3 11  5  2  3  8  3  2  3 10  4  2  3 11  3  2  3
181:  10  5  2  3 11  4  2  3 10  4  2  3 10  3  2  3 12  5  2  3
201:  11

Length of sentence so far: 1203

Word     1000 is "in", with 2 letters.  Length of the sentence so far: 6082
Word    10000 is "in", with 2 letters.  Length of the sentence so far: 61396
Word   100000 is "the", with 3 letters.  Length of the sentence so far: 636884
Word  1000000 is "five", with 4 letters.  Length of the sentence so far: 6880573
Word 10000000 is "three", with 5 letters.  Length of the sentence so far: 66783764

Second part is not right. Last one takes a few minutes to run.

