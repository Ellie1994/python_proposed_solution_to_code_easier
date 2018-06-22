# remove ambiguity; 3-liner

nums = [1,1,1,1,2,2,2,2,2,2,3,3,3,3,4,5,6,7,8,8,8,9,9,9,9]

some_set = set() # empty set

for n in nums:  # loops over the nums-list

    some_set.add(n) # The add() method doesn't add an element to the set if it's already present in it.

print(some_set)
