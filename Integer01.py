# Berilgan ifodani hisoblang: (𝑎^3 − 𝑏^3) + (𝑎^3 + 𝑏^3)
# Input: a, b. (0<a<1000 va 0<b<1000) 
x1=int(input("a="))
x2=int(input("b="))
natija=((x1**3-x2**3)+(x1**3+x2**3))**(1/4)
print(natija)