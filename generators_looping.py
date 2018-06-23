# generators , whitout "next", with loop

def sq_num(nums):
   
    for n in nums:
        yield(n*n)

my_nums = sq_num([1,2,3,4,5])

for n in my_nums:
    print(n)
