### Check if a string contains a substring
sentence = "Hi I'm Bob!"
if "Bob" in sentence:
    print("YES")
### Let's take care of those capital letters too, just in case the ### string for "bOb" looks a little bit different ...
if "bOb".lower() in sentence.lower():
    print("YES")
### These two will convert a string to lower and upper case letters
sentence.lower()
sentence.upper()
### Check the properties of your string
sentence.isalpha() # Alphabetic characters only (no symbols or nums)
sentence.isnumeric() # Numbers only
sentence.islower() # Is it all lower case?
sentence.isupper() # Is it all upper case?
### Clean up your string
sentence.capitalize() # First char is capitalized
sentence.lstrip() # Remove whitespace on left side
sentence.rstrip() # Remove whitespace on right side
sentence.strip() # Remove whitespace on both sides
### The .join() method can concatenate strings with a separator
### list --> string
>>> " ".join(["Bob","has","a","balloon"])
"Bob has a balloon"### The .split() method does the opposite of .join()
### string --> list
>>> "Bob has a balloon".split(" ")
["Bob","has","a","balloon"]
### The .replace() method can replace a substring with another
>>> "Bob has a balloon".replace("has", "is")
"Bob is a balloon"