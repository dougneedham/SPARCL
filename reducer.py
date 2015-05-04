#!/usr/bin/python

from __future__ import division
import sys

current_word = None
current_count = 0
word = 'NULL'
count = 1

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we get only do it in the case we have a proper key\tvalue

    if len(line) > 1:
    	word, count = line.split('\t', 1)

    # convert count (currently a string) to int

    try:
        count = int(count)
    except ValueError:

        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this if statement requires the output of the mapper be sorted. 

    if current_word == word:
	# if the current word is the same as the word we are working with 
 	# just add the counter
        current_count += count
    else:
	# the current word is not the same as the word we are working with
	# therefore we have switched to a new word trusting that the data is sorted. 
	# Let's print the current_word, and current count.
        print '%s\t%s' % (current_word, current_count)
	# Now reset the current count to the value passed in
        current_count = count
	# and set current_word to our new word
        current_word = word

# This is for the last switch-over for the last word
if current_word == word:
    print '%s\t%s' % (current_word, current_count)

