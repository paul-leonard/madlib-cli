'''
Keeping in mind the concept of Single Responsibility Principle, build a command line tool which will perform the following:

[x] Print a welcome message to the user, explaining the Madlib process and command line interactions
[x] Read a template Madlib file (Example), and parse that file into usable parts.
You need to decide what components of this file are useful, and how to break those useful pieces apart
[ ] Once you know what parts of the template need user input, such as "Adjective", prompt the user to submit a series of words to fit each of the required components of the Madlib template.
[ ] With the collected user inputs, populate the template such that each provided input is placed into the correct position within the template.
[x] After the resulting Madlib has been completed, provide the completed response back to the user in the command line.
[x] Write the completed template (Example)to a new file on your file system (in the repo).'''

#imports
import re

#funciton definitions
def read_template(path):
  '''This function opens a given file, reads it, strips the spaces, closes the file, and returns the stripped string'''
  with open(path) as incoming_file:
    incoming_file_string=incoming_file.read()
    stripped_incoming_file_string = incoming_file_string.strip()
    return stripped_incoming_file_string

def parse(template_string):
  '''This function takes in a string and returns two things in one list.  First item in the list is a modified string with the parts of speech removed.  The second item in the list is another list that contains each part of speech required for the story.'''
  #originally thought of finding index of each { and }, then looping through to cut out text for new list and deleting the parts of speech... would involve loops and slice after searching... but after talking to Lee and Taylor... I like the regex approach better

  required_language_parts = re.findall(r"\{(.*?)\}", template_string)
  string_wo_parts = re.sub(r"\{(.*?)\}","{}", template_string)

  return [string_wo_parts, required_language_parts]
  
  #fake expected test results below (from testing the test)
  #return [""""Make Me A Video Game!\n\nI the {} and {} {} have {}{}'s {} sister and plan to steal her {}{}!\n\nWhat are a {} and backpacking {} to do? Before you can help {}, you'll have to collect the {} {}and {} {} that open up the {} worlds connected to A {} Lair. There are {} {} and {} {} in the game, alongwith hundreds of other goodies for you to find.""", ["Adjective","Adjective","A First Name","Past TenseVerb","A First Name","Adjective","Adjective","Plural Noun","Large Animal","Small Animal","A Girl's Name""Adjective","Plural Noun","Adjective","Plural Noun","Number 1-50","First Name's","Number","Plural Noun""Number","Plural Noun"]]

#*****************
#def merge?
#'''   sdfsdf ''''
#string_to_find_and_replace = '{}'
#for string_to_replace_it_with in players_words
  #include optional third agrgument to say to only replace the first set of '{}'
  #output_string = input_string.replace(string_to_find_and_replace, string_to_replace_it_with, 1)
  #since strings are immuatable... it may be better to do this as a function to pass the new string back in


def write_story_to_file(story):
  '''This function writes the new story to a file on the repo so it may be enjoyed later.'''
  with open('assets/your_story.text','w') as new_file:
    new_file.write(story)

#in place test that passed:
#storytime = "this is a good one if it works!"
#write_story_to_file(storytime)

#variable definitions
path = 'assets/template.txt'

#execution
print("""\n\n*************************************\n\nWelcome to the time of your life!!! IT IS TIME FOR MADLIBS!!!\n\nEnter a word for each type of word requested to reveal your fun new story!\n\n*************************************\n\n""")

#open and read template file
template_file_string = read_template(path)

#parse it
useable_template = parse(template_file_string)
print(useable_template)

#prompt user for words

#merge the story
story = "The finished story will go here in the future."

#print the story
print(story)

#save the story
write_story_to_file(story)