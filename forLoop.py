#for loop
for y in range (5,10): #will print 5 until 9. 10 not included
    print(y)

days = ["Mon", "Tues", "Wed", "Thu", "Fri", "Sat", "Sun"]

#for d in days:
  #  print (d)

#stop at thursday
for d in days:
    if(d=="Thu"): break
    print (d)

#skip thursday
for m in days:
    if(m=="Thu"): continue #skip thursday
    print(m)

