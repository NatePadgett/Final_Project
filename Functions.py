#import releveant modules
import json
import random
#function for converting a file from json
def json_converter(files):
    return json.loads(files)
#function for building a list of sentences
def sentence_builder(lines):
    lines = lines.strip()
    sentences = lines.split("  ")
    return sentences
#function for swapping sentences
def sentences_swap(string,lists):
    lists = [string.replace(string, random.choice(lists)) for string in lists]
    return lists
#function for converting a string to a list
def string_conv(lists2, string, lists3):
    lists2 = [string.decode('utf-8').strip().split() for string in lists3]
    return lists2
#function for swapping just words (NOT WORKING)
def solo_word_swap(string2,lists4, dictionary):
    lists4 = [string2.replace(random.choice(dictionary.keys()), random.choice(dictionary.keys())) for string2 in lists4]
    return lists4
#function for swapping sentences and words (NOT WORKING)
def sent_word_swap(string3, list5, dictionary2):
    middle_dictionary = dictionary2
    lists5 = [string3.replace(random.choice(middle_dictionary.keys()), random.choice(middle_dictionary.keys())) for string3 in lists5]
    return lists5
