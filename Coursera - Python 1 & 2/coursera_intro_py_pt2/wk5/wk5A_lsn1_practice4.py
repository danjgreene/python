# String list joining problem

###################################################
# Student should enter code below

def string_list_join(string_list):
    combo = ""
    for lst_str in range(len(string_list)):
        combo += string_list[lst_str]
    return combo
        
#string_list[0] + string_list[1]

###################################################
# Test data

print string_list_join([])
print string_list_join(["pig", "dog"])
print string_list_join(["spam", " and ", "eggs"])
print string_list_join(["a", "b", "c", "d"])


###################################################
# Output

#
#pigdog
#spam and eggs
#abcd