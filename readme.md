# 3 Git Commands

- git add .
- git commit -m "Your message goes here"
- git push
- 

# For Loops
``` python
# Assume text is a variable that
# holds a string. Write Python code
# that prints out the position
# of the first occurrence of 'hoo'
# in the value of text, or -1 if
# it does not occur at all.

text = "first hoo" 

# print text.find("boo")


def finder():
    consecutive = 0
    index = 0
    final_index = 0
    for letter in text:
        # print(consecutive, letter)
        if letter == 'h':
            consecutive += 1
            final_index = index
        elif letter == 'o' and consecutive != 0:
            consecutive += 1
        else:
            consecutive = 0
        index += 1
    if consecutive == 3:
        return final_index
    else:
        return -1
    
        
print finder()
```
