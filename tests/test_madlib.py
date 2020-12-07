'''You are NOT required to test terminal input/output, AKA print and input functions.

However you are expected to meaningful tests for your application.

So how can we skip testing print and output functionality while still proceeding with confidence?

The resolution to that dilemma is to break down your code so that it is more easily testable.

[x] Create and test a **read_template** function that takes in a path to text file and returns a stripped string of the file’s contents.
[x] Create and test a **parse** function that takes in a template string and returns a string with language parts removed and a separate list of those language parts.
[ ] Create and test a **merge** function that takes in a “bare” template and a list of user entered language parts, and returns a string with the language parts inserted into the template.'''

import pytest

from madlib_cli.madlib import read_template
from madlib_cli.madlib import parse
from madlib_cli.madlib import merge


def test_read_template():
  actual = read_template("assets/template.txt")
  expected = """Make Me A Video Game!\n\nI the {Adjective} and {Adjective} {A First Name} have {Past Tense Verb}{A First Name}'s {Adjective} sister and plan to steal her {Adjective} {Plural Noun}!\n\nWhat are a {Large Animal} and backpacking {Small Animal} to do? Before you can help {A Girl's Name}, you'll have to collect the {Adjective} {Plural Noun} and {Adjective} {Plural Noun} that open up the {Number 1-50} worlds connected to A {First Name's} Lair. There are {Number} {Plural Noun} and {Number} {Plural Noun} in the game, along with hundreds of other goodies for you to find."""
  assert actual == expected

def test_parse():
  actual = parse("""Make Me A Video Game!\n\nI the {Adjective} and {Adjective} {A First Name} have {Past Tense Verb}{A First Name}'s {Adjective} sister and plan to steal her {Adjective} {Plural Noun}!\n\nWhat are a {Large Animal} and backpacking {Small Animal} to do? Before you can help {A Girl's Name}, you'll have to collect the {Adjective} {Plural Noun} and {Adjective} {Plural Noun} that open up the {Number 1-50} worlds connected to A {First Name's} Lair. There are {Number} {Plural Noun} and {Number} {Plural Noun} in the game, along with hundreds of other goodies for you to find.""")
  expected = ["""Make Me A Video Game!\n\nI the {} and {} {} have {}{}'s {} sister and plan to steal her {} {}!\n\nWhat are a {} and backpacking {} to do? Before you can help {}, you'll have to collect the {} {} and {} {} that open up the {} worlds connected to A {} Lair. There are {} {} and {} {} in the game, along with hundreds of other goodies for you to find.""", ["Adjective","Adjective","A First Name","Past Tense Verb","A First Name","Adjective","Adjective","Plural Noun","Large Animal","Small Animal","A Girl's Name","Adjective","Plural Noun","Adjective","Plural Noun","Number 1-50","First Name's","Number","Plural Noun","Number","Plural Noun"]]
  assert actual == expected


def test_merge():
  bare_template = '''Make Me A Video Game!\n\nI the {} and {} {} have {}...'''
  fake_user_words = ["Adjective","Adjective","A First Name","Past Tense Verb"]
  actual = merge(bare_template, fake_user_words)
  expected = """Make Me A Video Game!\n\nI the Adjective and Adjective A First Name have Past Tense Verb..."""
  assert actual == expected