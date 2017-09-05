Filop - File Operations
====================

This is a file or folder search engine made by python
Speed and other features added

Use as follow
-------

```python
    import filop as fi

    x=fi.Filop()

    drivers =  [ a for a in fi.Filop().drivers()]  # to find the all drivers from pc

    for driver in fi.Filop().drivers():
      print(driver)

    all_folder = [ a for a in x.isdir()] # to find the all folder from pc

    folder = [ a for a in x.searchfolder(word)]

    file_ = [ a for a in x.searchfile(word)]

    [ a for a in x.searchfile(word,"txt")]  # what file type you enter, it will give you these types

    [ a for a in x.searchfile(word,["txt","jpg","png"])] # you can enter like this

    open_=x.open(path) # This function will open files or folders

    size=x.size(path)  # this is a list
```


- path= this is may str or list
- word = this means ,This is the word you want to search

- to be continued
