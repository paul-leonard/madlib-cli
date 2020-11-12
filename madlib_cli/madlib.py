'''
Keeping in mind the concept of Single Responsibility Principle, build a command line tool which will perform the following:

[x] Print a welcome message to the user, explaining the Madlib process and command line interactions
[ ] Read a template Madlib file (Example), and parse that file into usable parts.
You need to decide what components of this file are useful, and how to break those useful pieces apart
[ ] Once you know what parts of the template need user input, such as "Adjective", prompt the user to submit a series of words to fit each of the required components of the Madlib template.
[ ] With the collected user inputs, populate the template such that each provided input is placed into the correct position within the template.
[ ] After the resulting Madlib has been completed, provide the completed response back to the user in the command line.
[ ] Write the completed template (Example)to a new file on your file system (in the repo).'''


#funciton definitions
def read_template(path):
  '''This function opens a given file, reads it, strips the spaces, closes the file, and returns the stripped string'''
  with open(path) as incoming_file:
    incoming_file_string=incoming_file.read()
    stripped_incoming_file_string = incoming_file_string.strip()
    return stripped_incoming_file_string

def parse(template_string):
  '''This function takes in a string and returns two things in one list.  First item in the list is a modified string with the parts of speech removed.  The second item in the list is another list that contains each part of speech required for the story.'''
  #do things

  #return [string_wo_parts, required_language_parts]
  expected = [""""Make Me A Video Game!\n\nI the {} and {} {} have {}{}'s {} sister and plan to steal her {}{}!\n\nWhat are a {} and backpacking {} to do? Before you can help {}, you'll have to collect the {} {}and {} {} that open up the {} worlds connected to A {} Lair. There are {} {} and {} {} in the game, alongwith hundreds of other goodies for you to find.""", ["Adjective","Adjective","A First Name","Past TenseVerb","A First Name","Adjective","Adjective","Plural Noun","Large Animal","Small Animal","A Girl's Name""Adjective","Plural Noun","Adjective","Plural Noun","Number 1-50","First Name's","Number","Plural Noun""Number","Plural Noun"]]
  return expected


#variable definitions
path = 'assets/template.txt'

#execution
print("""\n\n*************************************\n\nWelcome to the time of your life!!! IT IS TIME FOR MADLIBS!!!\n\nEnter a word for each type of word requested to reveal your fun new story!\n\n*************************************\n\n""")

ans = read_template(path)

