strr= input("Enter a string : ")
count = 0
for c in strr:
  if c.isspace() != True:
    count = count + 1
print("Total number of characters : ",count)
