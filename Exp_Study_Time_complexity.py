from time import time

# ## Sol 1:
# def sumOfN(n):
#     sum = 0
#     for i in range (1, n+1):
#         sum += i
#     return sum


## Sol 2:
def sumOfN(n):

    return  int((n*(n+1))/2)


start_time = time()
x = sumOfN(1000000000000000000000000000000000000000000000000000000000000000000000000000000)

end_time = time()
d_time = end_time - start_time 
print(x)
print(d_time)