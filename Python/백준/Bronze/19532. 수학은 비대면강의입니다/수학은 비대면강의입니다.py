a,b,c,d,e,f = map(int, input("").split())
y = (d*c-a*f) / (b*d-a*e)
x = (f-e*y) / d
print(int(x), int(y))