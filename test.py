# https://pypi.org/project/inflect/

import inflect

# initialize

p = inflect.engine()

# get second or whatever we are on

ordinal_string = p.number_to_words(p.ordinal(101), andword='')
#ordinal_string = p.number_to_words(p.ordinal(101))

print(ordinal_string)

