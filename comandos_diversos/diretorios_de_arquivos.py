import os
### Handling slashes / when creating file paths
file = "process.py"
folder = "Documents/project1"
full_path = os.path.join(folder, file)
### Get the directory and file name from a full path
file = os.path.basename(full_path)
folder = os.path.dirname(full_path)
### Check if a file or folder exists
os.path.exists(full_path)
### Get the extension of a file 
name, extension = os.path.splitext(file)