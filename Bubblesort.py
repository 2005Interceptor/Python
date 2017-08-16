"""              
def bubbleSort(a):
    for i in range (0, len(a)-1, 1): 
        for j in range(len(a), i+1, -1):
            if a[j] < a[j-1]:
                temp = a[j]
                a[j] = a[j-1]
                a[j-1] = temp 
    return a  
"""

"""

there is somthing wrong @ Michael Schmidt

"""

def bubbleSort(a):
    for passnum in range(len(a)-1,0,-1):
        for i in range(passnum):
            if a[i] > a[i+1]:
                temp = a[i]
                a[i] = a[i+1]
                a[i+1] = temp 
    return alist

alist = [0, 1, 6, 2, 4, 14, 9, 13]
alist2 = bubbleSort(alist)
print(alist2)
