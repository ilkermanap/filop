# use as follow

# This is a file or folder search engine made by python

# Speed ​​and other features added

import filop as fi

to find the all drivers from pc --> fi.FILOP().drivers

to find the all folder from pc --> fi.FILOP().isdir

folder=fi.FILOP().SearchFolder(word) -->  this is a list

file=fi.FILOP().SearchFile(word)   -->   this is a list

open=fi.FILOP().OpenExtension(path) --> This function will open files or folders

size=fi.FILOP().Size(path)   -->   this is a list

If the file path is known, it needs to be done fi.FILOP(dont_use_search = False).Size(path) to calculate the size faster

You must enter the file path,if path is list,they will all open

--> path= this is may str or list

--> word = this means ,This is the word you want to search

# to be continued
