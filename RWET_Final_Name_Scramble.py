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

#create function for analyzing an incoming json file
def json_converter(files):
    return json.loads(files)

#open and read json file with family member names
family_members = open("RWET_Final_Names.json").read()
#assign result of function json_conversion to dictionary dic
dic = functions.json_converter(family_members)
#assign user input to a variable
letter = sys.stdin
#loop over lines in input variable
for line in letter:
    #strip away wite spaces from the lines
    line = line.decode('utf-8').strip()
    #split the lines into words along empty space
    words = line.split()
    #loop of words that appear in the dictionary
    for word in dic.keys():
        #randomly replace words from the dictionary with words in string "words"
        words = [word.replace(random.choice(dic.keys()), random.choice(dic.keys())) for word in words]
        #print the string resulting from the swap and join the sting elements at empty space.
    print " ".join(words)
