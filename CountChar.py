import re
 
 
string = "HelloEveryone !, 123"
 
# Creating separate lists using
# the re.findall() method.
uppercase_characters = re.findall(r"[A-Z]", string)
lowercase_characters = re.findall(r"[a-z]", string)
numerical_characters = re.findall(r"[0-9]", string)
special_characters = re.findall(r"[, .!?]", string)
