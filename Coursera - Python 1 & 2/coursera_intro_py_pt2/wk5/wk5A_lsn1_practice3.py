# Day to number problem

###################################################
# Student should enter code below

def day_to_number(day):
    idx_num = 0
    for day_wk in day_list:
        if day_wk == day:
            return idx_num
        idx_num += 1

day_list = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]


###################################################
# Test data

print day_to_number("Sunday")
print day_to_number("Monday")
print day_to_number("Tuesday")
print day_to_number("Wednesday")
print day_to_number("Thursday")
print day_to_number("Friday")
print day_to_number("Saturday")

###################################################
# Sample output

#0
#1
#2
#3
#4
#5
#6
