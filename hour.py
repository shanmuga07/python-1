a = float(input("Input a in minutes: "))
if (a<60):
  hour=0
  minutes=a
else:
  hour=a/60
  minutes=a%60
print("h:m-> %d %d" % (hour, minutes))
