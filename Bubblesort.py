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
#there is somthing wrong @ Michael Schmidt
# this is also how to make make comments use the # 
# Im getign an error say that there is a problem with indexing 
# I dont think you need to return alist ?  

# try this 

def bubbleSort(a):
    for passnum in range(len(a)-1,0,-1):
        for i in range(passnum):
            if a[i] > a[i+1]:
                temp = a[i]
                a[i] = a[i+1]
                a[i+1] = temp 


alist = [0, 1, 6, 2, 4, 14, 9, 13]
bubbleSort(alist)
print(alist)

