m1=float(input("enter the marks of sub1= "))
m2=float(input("enter the marks of sub2= "))
m3=float(input("enter the marks of sub3= "))
m4=float(input("enter the marks of sub4= "))
m5=float(input("enter the marks of sub5= "))
sum=m1+m2+m3+m4+m5
mean=sum/5
per=(sum/500)*100
print(mean)
if per>35:
  print("pass")
else:
  print("fail")
