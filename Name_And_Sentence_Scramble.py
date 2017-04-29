#Goal is to simulate what dementia and Alzheimers do to
#written language.
#
#I am using my mother's christmas cards as my source text
#but am basing that program and text manipulation on
#interactions with my grandmother, who has severe vascular
#dementia

#import random, json, sys, and my functions module
import random
import json
import sys
import functions

#open and read json file with family member names
family_members = open("RWET_Final_Names.json").read()
#assign result of function json_conversion to dictionary dic
dic = functions.json_converter(family_members)
#assign user input to a variable
letter = sys.stdin
#loop over lines in input variable
for line in letter:
    #create lists for function arguments
    sentence = list()
    lists_of_words = list()
    words = str()
    word_list = list()
    #function for building sentences
    lists_of_sentences = functions.sentence_builder(line)
    #randomly swap out sentences:
    lists_of_sentences = functions.sentences_swap(sentence,lists_of_sentences)
    #function for producing words in each sentence
    lists_of_words = functions.string_conv(lists_of_words, words, lists_of_sentences)
    #loop over a further parsed lists of lists words from the sentences.
    for word_lists in lists_of_words:
        #loop over parsed out words from the dictionary
        for word in dic.keys():
            #list comprehension to randomly swap the names of people mentioned in the letters
            words = [word.replace(random.choice(dic.keys()), random.choice(dic.keys())) for word in word_lists]
            #print the string resulting from the swap and join the sting elements at empty space.
        print " ".join(words)
