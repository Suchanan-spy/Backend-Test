try:
    fact = int(input('enter your number : '))
except:
    fact = 0

# calculate factorial
if fact > 0:
    round = ''
    ans = 1
    for i in range( fact, 0, -1 ):
        ans *= int(i)
        round += str(i)
        if i > 1 :
            round += ' x '
        
    # print( fact, '! is', ans )

# find 0
num = str(ans)
total = len(num)
a = list(num)
# print(a[total-1])
count = 0
while total >= 0:
    if a[total-1] == '0':
        count = count + 1
    else:
        break
    
    total = total-1
print(count)




