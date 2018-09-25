num=int(input("Enter a number:")
hold=num
sum=0
if(num<=0):
  print("enter whole numbers")
else:
  while(num>0):
    sum=sum+num
    num=num-1
    print("sum of first",hold,"natural numbers is:",sum)
