# temporary variable

employee1 = 15
employee2 = 21

employee1, employee2 = employee2, employee1

print employee1
print employee2

nums = [2, 5, 3]

nums[1], nums[1-1] = nums[1-1], nums[1]

print nums

--> [89, 1, 5, 82, 42]

num_swaps = 0
# FIRST OUTER LOOP
    # 1st inner loop
        [1, 89, 5, 89, 42] # SWAP
    # 2nd inner loop
        [1, 5, 89, 82, 42] # SWAP
    # 3rd inner loop
        [1, 5, 82, 89, 42] # SWAP
    # 4th inner loop
        [1, 5, 82, 42, 89] # SWAP
    
4 swaps

# SECOND LOOP
    # 1st inner loop
        [1, 5, 42, 82, 89] # SWAP
    # 2nd inner loop
        [1, 5, 42, 82, 89]
        

    