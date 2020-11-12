'''
Keeping in mind the concept of Single Responsibility Principle, build a command line tool which will perform the following:

[x] Print a welcome message to the user, explaining the Madlib process and command line interactions
[ ] Read a template Madlib file (Example), and parse that file into usable parts.
You need to decide what components of this file are useful, and how to break those useful pieces apart
[ ] Once you know what parts of the template need user input, such as "Adjective", prompt the user to submit a series of words to fit each of the required components of the Madlib template.
[ ] With the collected user inputs, populate the template such that each provided input is placed into the correct position within the template.
[ ] After the resulting Madlib has been completed, provide the completed response back to the user in the command line.
[ ] Write the completed template (Example)to a new file on your file system (in the repo).'''

print("""\n\n*************************************\n\nWelcome to the time of your life!!! IT IS TIME FOR MADLIBS!!!\n\nEnter a word for each type of word requested to reveal your fun new story!\n\n*************************************\n\n""")

def read_template(path):
  with open(path) as incoming_file:
    incoming_file_string=incoming_file.read()
    stripped_incoming_file_string = incoming_file_string.strip()
    return stripped_incoming_file_string

path = 'assets/template.txt'
ans = read_template(path)

