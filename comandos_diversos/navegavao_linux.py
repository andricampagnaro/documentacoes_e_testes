import os
### Execute a shell command
os.system("echo 'My name is bob the builder'")
### Return the current working directory
os.getcwd()
### List all of the files and sub-directories in a particular folder
os.listdir("Documents")
### Create a single folder
os.mkdir("Data Science Projects")
### Create folders recursively
### The below line creates a folder "Documents" with a subfolder 
### inside it called "Data Science Projects" with a subfolder inside ### that one called "Project 1"
os.makedirs("Documents/Data Science Projects/Project 1")
### Delete a file 
os.remove("data.txt")  
### Delete a folder
os.rmdir("Data Science Projects")  
### Delete directories recursively.
os.removedirs("Documents/Data Science Projects/Project 1") 
### Rename a file or folder
os.rename("My Documents", "Your Documents")