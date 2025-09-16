import tracemalloc as tm

# ## Sol 1:
# def sumOfN(n):
#     sum = 0
#     for i in range (1, n+1):
#         sum += i
#     return sum


# Sol 2:
def sumOfN(n):

    return  int((n*(n+1))/2)


tm.start()
x = sumOfN(1000000000)
print(x)
print(tm.get_traced_memory())
tm.stop()
