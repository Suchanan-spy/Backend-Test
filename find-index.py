arrNumber = []
range_ = int(input('enter number of range array : '))
for i in range(range_):
    input_ = int(input('enter number : '))
    arrNumber.append(input_)
# print(arrNumber)


# find max number
max = None
for x in arrNumber:
    if max is None or x > max:
        max = x
    # print('Loop',x,max)
# print(max)


# find index of max number
index=arrNumber.index(max)
print('index of max',index)





