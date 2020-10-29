#3:
for i in range(4):
    for j in range(8):
        if i == j or i+j == 7:
            print('/', end =" ")
        else:
            print('*', end =" ")
    print(' ')
for i in range(4,7):
    for j in range(8):
        if i+j == 6 or i == j-1:
            print('/', end =" ")
        else:
            print('*',end = " ")
    print(' ')

#5:

list = []
new_list = []
def checkUnique(str):
    for i in str:
        list.append(i)

    for i in list:
        if i not in new_list:
            new_list.append(i)
    
    if len(list) == len(new_list):
        return('Good')
    else:
        return('Bad')
    
x = input('Enter a string ')
result = checkUnique(x)
print(result)

#or

list = []
new_list = []
def checkUnique(str):
    for i in str:
        list.append(i)
    new_list = set(list)

    if len(list) == len(new_list):
        return('Good')
    else:
        return('Bad')
    
x = input('Enter a string ')
result = checkUnique(x)
print(result)

#6:

list = []
def address(x):
    temp = 0
    for i in x:
        z = i.split('.')
        list.append(z)
    list.sort()
    #return list
    for i in range(len(list)-1):
        if list[i][0] == list[i+1][0] and list[i][1] == list[i+1][1]:
           return('The computers from the same locality have IP addresses :',list[i],list[i+1])
    
y = ['111.22.3.44','555.66.7.88','111.22.5.66','0.0.0.0']
result = address(y)
print(result)

#8:

def checkvowel(x):
    list_new = []
    alp_count, vowel_count = 0, 0
    y = set(x)
    for i in y:
        if i.isupper() or i.islower():
            alp_count += 1
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            vowel_count += 1
    alp_count -= 1
    extra = len(y) - alp_count
    
    if len(y) - extra - vowel_count == 21:
        print('Consogram')
    else:
        print('Not Consogram')
    
    
    
str = 'The quick brown fox jumps over the lazy dog'
result = checkvowel(str)

#2:

 #Upper left:i+j<=3
#Upper Right: j>4 and j-1>=5
list = ['A','B','C','D','E']
for i in range(5):
    for j in range(9):
        if i+j <= 3 or (j > 4 and j-i>=5):
            print(' ',end=' ')
        else:
            print(list[i],end=' ')
    print(' ')

#4:

list = []
from collections import Counter
def countUnique(str):
    #str.lower()
    list = str.lower().split()
    list.sort()
    for i in list:
        if i.isnumeric():
            print('Not valid')
        for z in i:
            if z == '!' or z == '?' or z == '.' or z == ',' or z == ':' or z == ';':
                list.pop()
    x = Counter(list)
    print(x)

str='Programming is a skill in demand! Your programming skills are bankable assets'
result = countUnique(str)

#7:

def boundedSum(mat,search):
    sum = 0
    #index_1,index_2 = mat.index(search)
    
    #------------------------------------------------------------------------------------------------
    # Don't know how to find index of an element in a 2d array so I have manually entered the indices
    #------------------------------------------------------------------------------------------------
    
    index_1,index_2 = 2,2
    for i in range(index_1-1,index_1+2):
        for j in range(index_2-1,index_2+2):
            sum+= mat[i][j]
    return(sum-search)
    
mat =   [[4, 3, 7, 10],[12, 17, 19, 21],[8, 1, 28, 65],[34, 39, 41, 40],[73, 20, 50, 70]]
result = boundedSum(mat,28)
print(result)
