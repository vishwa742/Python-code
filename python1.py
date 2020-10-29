# 2:
'''
def smallnum(x):
    lowest = min(x)
    min_index = x.index(lowest)
    update = 0
    small = x[min_index]
    for i in range(len(x)):
        update += x[i] - 0.75*x[i]
        x[i] = 0.75*x[i]
    x[min_index] = small + update - small*0.25
    return x

result = smallnum([16,10,8])
print(result)

'''

#4
'''
from collections import Counter

def frequency(x):
        c = Counter(x)
        d = len(x)
        return c
x = str(input('Enter words'))
list = x.split()
result = frequency(list)
print(result)

'''
#or
'''
count_list = []
unique = []
def frequency(x):
    count = 0
    x.sort()
    y,z = 0,0
    n = len(x)
    while count < n:
        #count = 0
        i = count
        z = x.count(x[i])
        count_list.append(z)
        y = z
        count += z
    
    for i in x:
        if i not in unique:
            unique.append(i)
    
    for i in range(len(count_list)):
        n = len(count_list)
        print(unique[i],':',count_list[i])


x = str(input(' Enter words'))
list = x.split()
result = frequency(list)

'''


#5:

'''
fist = []
def smallFactor(x):
    i = 2
    while x>0:
        if x%i==0:
            x = x//i
            print(i)
        else:
            i = i+1

x = int(input('Enter a number'))
result = smallFactor(x)
'''

#1:

'''
def checkPass(str):
    count_u, count_l, count_num, count_special = 0, 0, 0, 0 
    for i in str:
        if i.isupper():
            count_u += 1
        if i.islower():
            count_l += 1
        if i =='0' or i =='1' or i =='2' or i =='3' or i=='4' or i=='5' or i=='6' or i=='7' or i=='8' or i =='9':
            count_num += 1
        if i == '$' or i == '#' or i == '@':
            count_special += 1
            
    if len(str) > 5 and len(str)<13 and count_num>0 and count_special>0:
        return True
    else:
        return False
    
x = input(' Enter a password')
result = checkPass(x)
print(result)
'''

#3

'''
list = []
list_prefix_new = []
def category(x):
    temp = 0
    for i in x:
        z = i.split('.')
        list.append(z)
        
    #prefix:
    list_prefix = sorted(list)
    print("Sorted by Prefix: ",list_prefix)
    
    #suffix:
    list_suffix = sorted(list)
    for j in range(len(list_suffix)):
        temp = list_suffix[j][0]
        list_suffix[j][0] = list_suffix[j][1]
        list_suffix[j][1] = temp
    list_suffix.sort()
    
    print("Sorted by Suffix: ",list_suffix)
    
    
    #return list_prefix
    #return list_suffix
    
    
y = ['music_app.js', 'music_app.png', 'music_app.wav', 'tetris.png', 'tetris.js']
#z = y.split('.')
result = category(y)
'''





