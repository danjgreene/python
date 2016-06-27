# Purpose of the function is to find the word "able" in random string
# and provide index of each letter

# First we set up the function -- it has a single argument, which is the string
# we want to search for "able"
def able_finder(string):
    # Now let's initialize some variables within the function -- we need an generic index 
    # along with one to hold the final value for each letter found
    # We also need a variable to keep track of consecutive letters in the word

    index = 0
    index_a = 0
    index_b = 0
    index_c = 0
    consec_let = 0

    # Next, let's create a loop so we can check each character in the string for
    # the letters we want to find

    for letter in string:
        # let's increment the index count by 1 no matter what
        # print index, letter, consec_let
        
        # Now we need an if statement to check if the character is 'a'
        if letter == 'a' and consec_let == 0:
            index_a = index
            consec_let += 1
        elif letter == 'b' and consec_let == 1:
            index_b = index
            consec_let += 1
        elif letter == 'l' and consec_let == 2:
            index_l = index
            consec_let += 1
        elif letter == 'e' and consec_let == 3:
            index_e = index
            consec_let += 1
        elif consec_let == 4:
            break
        #else:
            #consec_let = 0
        index += 1
    if consec_let == 4:
        return "'able' found at " + str(index_a) + " " + str(index_b) + " " + str(index_l) + " " + str(index_e) + " in " + "'" + string + "'"
    else:
        return "'able' not found"




print able_finder(raw_input("Enter a random string of text:"))