
import  math
y = int(input("y ="))
x = int(input("h ="))
a = int(input("a="))
G =(math.cos(2*abs(y+x)-(x+y))**4*x*x)/(math.atan(x+a)**4*x**5)
print(G)