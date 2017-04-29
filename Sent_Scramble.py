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
    #create lists for function argument
    sentence = list()
    #store sentence_swap result in a variable
    lists_of_sentences = functions.sentence_builder(line)
    #randomly swap out sentences:
    lists_of_sentences = functions.sentences_swap(sentence,lists_of_sentences)
    #print the swapped sentences and join together nicely
    print " ".join(lists_of_sentences)
