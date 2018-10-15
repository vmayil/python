str=input("str=")
try:
   i=float(str)
except(ValueError,TypeError):
   print("not numeric")
else:
   print("numeric")
