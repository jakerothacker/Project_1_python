test = [0,1]
print(test)

t = len(test)
i=0
while i < t:
    print(i)
    print(test[i])
    if test[i]%2 == 0:
        test.pop(i)
        i -= 1
    i += 1
    t=len(test)
print(test)