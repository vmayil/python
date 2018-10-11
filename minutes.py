time = float(input("Input time in minutes: "))
day = time // (24 * 60)
time = time % (24 *60)
hour = time //60
time %= 3600
minutes = time // 60
time %= 60
minutes = time
print("h:m:", (day, hour, minutes))

