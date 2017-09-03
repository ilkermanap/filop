Filop - File Operations
====================

This is a file or folder search engine made by python
Speed and other features added

Use as follow
-------

```python
    import filop as fi
    x=fi.Filop() # Because it scans all the files, it does so for speeding up other processes
    fi.Filop().drivers() # to find the all drivers from pc
    x.isdir() # to find the all folder from pc
    folder=x.searchfolder(word)  # this is a list
    file_=x.searchfile(word)  #  this is a list
    type_=x.searchfile(word,"txt")  # what file type you enter, it will give you these types
    type_=x.searchfile(word,["txt","jpg","png"]) # you can enter like this
    open_=x.open(path) # This function will open files or folders
    size=x.size(path)  # this is a list
    #If the file path is known, it needs to be done to calculate the size faster
    fi.Filop().size(path) #You must enter the file path,if path is list,they will all open
                                                  
```
    
                                                  
- path= this is may str or list
- word = this means ,This is the word you want to search

- to be continued
