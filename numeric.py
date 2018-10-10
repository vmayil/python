str =input('str=')
try:
    i = float(str)
except (ValueError, TypeError):
    print('Not numeric')
else:
    print('Numeric')
