def reorder(arr,index, n): 
  temp = [0] * n 
   for i in range(0,n): 
        temp[index[i]] = arr[i] 
   for i in range(0,n): 
        arr[i] = temp[i] 
        index[i] = i 
arr = [1,7,5,0,4]
index = [3,0,4,2,1]
n = len(arr) 
reorder(arr, index, n)  
print("Reordered array is:") 
for i in range(0,n): 
    print(arr[i],end = " ") 
print("\nModified Index array is:") 
for i in range(0,n): 
    print(index[i],end = " ") 
  



