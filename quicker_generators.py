# generator, oneliner wihtout "list"

my_nums = (n*n for n in [1,2,3,4,5]) # generator obj

print(my_nums)

for n in my_nums:
    print(n) 

print() # prints a blank row

# or converting in a list instead of looping:

my_nums = (n*n for n in [1,2,3,4,5]) # generator obj

print(list(my_nums))
