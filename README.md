# madlib-cli
This Python module contains a traditional madlib text game. This was assignment Lab03 for Code401.

## Lab Submission Pull Requests
[Lab03: Errors, Files, and Packaging](https://github.com/paul-leonard/madlib-cli/pull/1)

## Release Info
**Author**: Paul Leonard
**Version**: 0.9.0

## Overview
This module produces a fun textual madlib game where you can go on a magical journey!  Discover your very own story!

## Architecture
A template story is used from a provided text file.  The text file is read in and the words needing replacement are identified through a parsing operation.  The user, game player, is prompted for inputs to create the story.  The produced story is printed in the terminal and also written to a new text file for later enjoyment.

## Change Log
**0.9.0** 11-11-2020 - Initial beta release
**1.0.0** 11-TBD-2020 - Initial release

## Credits and Collaborations
- Thanks to the SoloLearn Python Course for teaching me the basics to use in this app
- Thanks to the team at Code Fellows for getting me started on my third use of Python!
- Thanks to classmates I discussed and conferred with:  Alex, Bhagirath, Taylor, Lee, Hexx, and Seth
- Additional thanks to Skyler and JB for some pointers I heard them giving out.
- [W3 Schools Strip Method](https://www.w3schools.com/python/ref_string_strip.asp)
- [python.org re docs](https://docs.python.org/3/library/re.html)
- [Geeks for Geeks: Python Regex: re.search() VS re.findall()](https://www.geeksforgeeks.org/python-regex-re-search-vs-re-findall/)
- [Read/Write article at RealPython has replace example](https://realpython.com/read-write-files-python/)
- [Google for Education, Regex, Greedy vs Non-greedy, is the ? needed](https://developers.google.com/edu/python/regular-expressions)
- [Python.org docs on re.finditer, thought about using instead of findall](https://docs.python.org/3/library/re.html)
- [Google docs section on substitution using regex](https://developers.google.com/edu/python/regular-expressions)
- [replace guidance for merge function](https://note.nkmk.me/en/python-str-replace-translate-re-sub/)