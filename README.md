**INITIAL GOAL**

When I started working on this project, my intention was to explore the degredation of communication in people with dementia through procedurally generated text. The plan was to find as much research as possible on this topic and attempt to replicate failure of different language centers of the brain in a single patient through a Python script or series if scripts. Through my research (and corroborated by comments throughout what I found), I concluded two things:

1. Degeneration occurs primarily in regards to content.
2. The research that does exist focuses on care taker communication with patients, rather than the communication faculties of the patients.

The papers I read for this project:

[Investigating the Effects of Communication Problems on Caregiver Burden](https://academic.oup.com/psychsocgerontology/article/60/1/S48/617664/Investigating-the-Effects-of-Communication)

[Links Among Communication, Dementia, and Caregiver Burden](http://www.cjslpa.ca/download.php?file=2012_CJSLPA_Vol_36/No_04_264_355/Watson-Aizawa-Savundranayagam-Orange_CJSLPA.pdf)

[Relation of linguistic communication abilities of Alzheimer's patients to stage of disease](https://www.ncbi.nlm.nih.gov/pubmed/1377076)

[Symptoms of communication breakdown in dementia: Carers' perceptions](https://www.researchgate.net/publication/15552549_Symptoms_of_communication_breakdown_in_dementia_Carers'_perceptions)

**PIVOT**

I needed to switch my plan, so I simplified and made it more personal. Rather than base my procedure on studies, I focused the  work on my own experience with my grandmother and the specific degenerative traits she exhibited over the course of her slip into vascular dementia. The traits were:

1. Confusing people
2. Repetition of phrases
3. Confusing and reliving events
4. Decreased communication/generalization

For source text, I used six files: five Christmas letters and one json file containing the the names of family members mentioned in the letters. The letters were written by my mom over the course of five years in third person, so conveniently the writer can be framed as anyone. I have changed the names of individuals and places out of respect for privacy. The source can be found in this repo under file names that include "Source_Letter". 

**CODE**

To process the text, I wrote four scripts that simulate the communication challenges mentioned earlier. I also stored all of my functions in a module [functions.py](https://github.com/NatePadgett/RWET-Final-Slipping/blob/master/functions.py).

[Name_Scramble.py](https://github.com/NatePadgett/RWET-Final-Slipping/blob/master/Name_Scramble.py) replaces the names of individuals mentioned in the source next with a randomly chosen name from the JSON file [Names.json](https://github.com/NatePadgett/RWET-Final-Slipping/blob/master/Names.json). This is accomplished through a list comprehension.
 
```python
words = [word.replace(random.choice(dic.keys()), random.choice(dic.keys())) for word in words]
```

I randomly choose both which names to swap in the source text and what to swap them with. In both cases, the names to swap and swap with are pulled from a dictionary dic into which Names.json is parsed into. 

```python
dic = functions.json_converter(family_members)
```

```json
{
"Nathan": "son",
"Harry":"son",
"Stephan":"son",
"Tiffany": "girlfriend of Nathan",
"Daniel":"husband",
"Nancy":"self"
}
```

Because I'm working with a short dictionary of names, swapping names in this way mostly yielded subtle changes, i.e.: only one or two replacements per per run of the script. For the purposes of this project that is perfect. It gives an attentive reader the sense that something is off about the narrator and that they are confusing the characters in their own story. The few moments when no change is made by the program are like the moments of clarity amid the creeping haze of dementia experience by my grandmother. 

Example output:
>Stephan (turning 26 today) is still in NYC and living in Brooklyn, though he moved in September very close to Prospect Park and our favorite: Brooklyn Botanical Garden. The company he works for is growing faster than ever affording Nathan many opportunities to develop management skills, third party experience, etc. Salesforce invited him to speak at Dreamforce, so we spent the week before Thanksgiving together. Thankfully he and his wonderful girlfriend, Nancy, will be home for Christmas week.

(Nathan lives in NYC and turned 26. Stephan is his brother)

[Sentence_Scramble.py](https://github.com/NatePadgett/RWET-Final-Slipping/blob/master/Sentence_Scramble.py) does as it's name suggests: it mixes up scentences in each source text. This is accomplished through a line comprehension call as part of function `sentence_swap(string,list)`.

```python
def sentences_swap(string,lists):
    lists = [string.replace(string, random.choice(lists)) for string in lists]
    return lists
```

I also wrote a function for parsing the text into sentences to keep the code brief and elegant. : 

```python
def sentence_builder(lines):
    lines = lines.strip()
    sentences = lines.split("  ")
    return sentences
```

Sentence scrambling in this way is like my grandma's often random repetitions of phrases and stories as her disease worsened.

Example output:
>He is a great roommate so it is mutually beneficial for the entire family :) He is saving money while living at home. He is saving money while living at home. He is saving money while living at home.

[Name_And_Sentence_Scramble.py](https://github.com/NatePadgett/RWET-Final-Slipping/blob/master/Name_And_Sentence_Scramble.py) combines the two symptoms created in the previous two scripts. The resulting text is a confusing mix of name confusion and statement repitition. 

Example output: 

>Tiffany arrives on December 19th for two whole weeks! Yippee!
>
>Nathan arrives on December 19th for two whole weeks! Yippee!

This is indcative of the confluence of communicative challenges experienced by my grandmother well into her illness, when it became obvious to us that she had dementia. 

The final script, [Minimal.py](https://github.com/NatePadgett/RWET-Final-Slipping/blob/master/Minimal.py) simply pulls the print statement at the end of RWET_Final_Name_And_Sent_Scramble.py out of the last for loop for words an moves it up a level to the for loop above it. 

In Name_And_Sentence_Scramble:

```python
for word_lists in lists_of_words:
        for word in dic.keys():
            words = [word.replace(random.choice(dic.keys()), random.choice(dic.keys())) for word in word_lists]
        print " ".join(words)
```
       
In Minimal:

```python
for word_lists in lists_of_words:
        for word in dic.keys():
            words =[word.replace(random.choice(dic.keys()), random.choice(dic.keys())) for word in word_lists]
    print " ".join(words)
```
    
Pulling the print statement up out of the nested for loop that searches for words in the dictionary to the previous loop reduces the number of lines and removes repeated sentences.

Result with Name_And_Sent_Scramble:

>Merry Christmas & Happy New Year
>
>12/27/2016
>
>Dear Friends and Family,
>
>Our souls have been fed and we are thankful.
>
>He is super busy and energized.
>
>Harry started a new choir in January. It is a joint venture with his high school choir director. The choir is off to a great start with two concert seasons booked already. Harry’s time with the choir will be short as he will move to Texas in January to start a new job.
>
>He has a few more applications to submit, but by Fall 2017, mom and dad anticipate being real empty nesters – oh my!
>
>Nancy and Nathan continue to work together, trying to stay on top of all the changes in medicine.
>
>We hope 2017 will bring good tidings for all.
>
>Frohe Weinachten!
>
>with love from our family to yours

Result with Minimal:

>Merry Christmas & Happy New Year
>
>12/27/2016
>
>Dear Friends and Family,
>
>We have sunshine most of the year and rain has made us see green again.
>We have each other and we have wonderful friends.
>We have sunshine most of the year and rain has made us see green again.
>Our souls have been fed and we are thankful.
>We have each other and we have wonderful friends.
>We have each other and we have wonderful friends.
>
>He still resides in New York; working for a start up, living in Brooklyn, and is now attending graduate school.
>He still resides in New York; working for a start up, living in Brooklyn, and is now attending graduate school.
>Nathan will be home for three whole weeks, a long visit not enjoyed by us since UCSB.
>
>Harry started a new choir in January. It is a joint venture with his high school choir director. The choir is off to a great >start with two concert seasons booked already. Harry’s time with the choir will be short as he will move to Texas in January >to start a new job.
>Tiffany started a new choir in January. It is a joint venture with his high school choir director. The choir is off to a >great start with two concert seasons booked already. Harry’s time with the choir will be short as he will move to Texas in >January to start a new job.
>
>Stephan continues to juggle college and work, including a summer internship with our county DA’s office.
>In addition, he too joined the choir started by his brother Harry.
>In addition, he too joined the choir started by his brother Harry.
>In addition, he too joined the choir started by his brother Nancy.
>
>They have been blessed with a great team.
>Harry and Daniel continue to work together, trying to stay on top of all the changes in medicine.
>
>We hope 2017 will bring good tidings for all.
>
>Frohe Weinachten!
>
>with love from our family to yours

This represents the latest stage in my grandmother's illness, when she started communicating less because it was increasingly difficult to do so. During this current phase she speaks in short, incomplete thoughts and often confuse time, place, and the people involved.

Letters:

[Letter 1](https://github.com/NatePadgett/RWET-Final-Slipping/blob/master/Letter_1.txt)

[Letter 2](https://github.com/NatePadgett/RWET-Final-Slipping/blob/master/Letter_2.txt)

[Letter 3](https://github.com/NatePadgett/RWET-Final-Slipping/blob/master/Letter_3.txt)

[Letter 4](https://github.com/NatePadgett/RWET-Final-Slipping/blob/master/Letter_4.txt)

[Letter 5](https://github.com/NatePadgett/RWET-Final-Slipping/blob/master/Letter_5.txt)
