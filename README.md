# use as follow

# This is a file or folder search engine made by python

# Speed ​​and other features added

import filop as fi

to find the all drivers from pc --> fi.Filop().drivers

to find the all folder from pc --> fi.Filop().isdir

folder=fi.Filop().searchfolder(word) -->  this is a list

file=fi.Filop().searchfile(word)   -->   this is a list

type=fi.Filop().searchfile(word,"txt")  --> what file type you enter, it will give you these types

type=fi.Filop().searchfile(word,["txt","jpg","png"]) -->you can enter like this

open=fi.Filop().open(path) --> This function will open files or folders

size=fi.Filop().size(path)   -->   this is a list

If the file path is known, it needs to be done fi.Filop(dont_use_search = False).size(path) to calculate the size faster

You must enter the file path,if path is list,they will all open

--> path= this is may str or list

--> word = this means ,This is the word you want to search

# to be continued
