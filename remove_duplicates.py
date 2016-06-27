def item_in(lst, num):
    for val in lst:
        if val == num:
            return True
    return False
        
#print item_in([1, 1, 3], 2)

def unique(lst):
    """
    removes duplicates from a list
    lst: list
    return: list
    """
    clean_lst = []
    for num in lst:
        if not item_in(clean_lst, num):
            clean_lst.append(num)
    return clean_lst

def unique2(lst):
    """
    removes duplicates from a list
    lst: list
    return: list
    """
    clean_lst = []
    for num in lst:
    	found = False
        for val in clean_lst:
        	if num == val:
        		found = True
        if not found:
			clean_lst.append(num)
    return clean_lst

print unique2([2, 3, 4, 6, 4, 3, 5, 2, 2])