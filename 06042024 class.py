# a = 1
# b = 1
# fib = [a, b]
# count = 2

# sum = 0
# while count <= 100:
#    next = a + b
#    fib.append(next)
#    a = b
#    b = next
#    count += 1

# print(fib)

# while True:
#    next = a + b
#    fib.append(next)
#    a, b = b, next
#    count += 1
#    if count == 4:
#        break
# print(sum(fib))

a1 = 1
d = 3
n=1
list = []
while n<10:
    anext = a1+ (n-1)*d
    list.append (anext)
    n+=1
print (list)

t1 = 1
k = 1
tlist = []
while k<11:
    tnext = (k*(k+1))//2
    tlist.append (tnext)
    k+=1
print(tlist)