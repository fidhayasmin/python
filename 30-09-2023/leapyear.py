a=int(input("Enter the current year:"))
b=int(input("Enter the year to show upto:"))
for i in range(a,b+1):
      if i%4==0 and i%100!=0 or i%400==0:
          print(i)
