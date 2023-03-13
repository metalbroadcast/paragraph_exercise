## A string concatenation program to make entire paragraphs of random story by input some adjectives, verbs, nouns, etc.

# youtuber = "Kylie Ying" 
# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")

import random

#input terms
print("Input the followings terms to generate a paragraph:")
adj = input("Adjective: ")
verb1 = input("First Verb: ")
verb2 = input("Second Verb: ")
famous_person = input("Famous person: ")

#random paragraphs
paragraph_one = f"Computer programming is so {adj}! It is fascinated all the time because I love to {verb1}. Stay concentrated and {verb2} like if you were {famous_person}!"
paragraph_two = f"Running is so {adj}!. It feels great because I love to {verb1}. I love to {verb2} along with it. Makes me feel like if I was {famous_person}!"
paragraph_three = f"Going to the movies is so {adj}!. It is relaxing because I love to {verb1}. I rather choose to do that instead of {verb2} in a bar. As long as {famous_person} show off their acting skills in the big screen!"
paragraph_four = f"Soccer is so {adj}!. It gathers a lot of people of all nations to {verb1} while enyoing the championship. I like to {verb2} in the middle of the game. Even if it's in a big stadium accompanied with friends. Last game we went we saw {famous_person} close to us!"

#selection of random paragraphs
def selectParagraph(c):
    if c == 1:
        return paragraph_one
    elif c == 2:
        return paragraph_two
    elif c == 3:
        return paragraph_three
    elif c == 4:
        return paragraph_four

#randomize to select paragraph
i = random.randint(1,4)
randomParagraph = selectParagraph(i)

#print result
print(randomParagraph)




