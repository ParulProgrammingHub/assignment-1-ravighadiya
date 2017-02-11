d=int(input("enter the no. of days= "))
y=int(d/360)
d=d%360
m=int(d/30)
d=d%30
days=int(d%30)
print(y)
print(y,"year",m,"month","and",days,"days")
