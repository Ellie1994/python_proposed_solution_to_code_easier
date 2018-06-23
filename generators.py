# generators

def sq_num(nums):
   
    for n in nums:
        yield(n*n)

my_nums = sq_num([1,2,3,4,5])

print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums)) # outpu: StopIteration
