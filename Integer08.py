x1=float(input("x1="))
y1=float(input("y1="))
x2=float(input("x2="))
y2=float(input("y2="))
x3=float(input("x3="))
y3=float(input("y3="))
a=((x2-x1)**2+(y2-y1)**2)**0.5
b=((x2-x3)**2+(y2-y3)**2)**0.5
c=((x3-x1)**2+(y3-y1)**2)**0.5
p=(a+b+c)/2
s=(p*(p-a)*(p-b)*(p-c))**0.5
javob_1=round(p, 2)
javob_2=round(s, 2)
print(javob_1*2, javob_2)