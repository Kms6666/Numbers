import sys

print(sys.argv[0])
print(sys.argv[1])
print(sys.argv[2])
print(sys.argv[3])

a = (sys.argv[1])
b = (sys.argv[2])
c = (sys.argv[3])

def addnumbers(x,y,z):
   n = int(x) + int(y) + int(z)
   print(f"The sum is {n}")

addnumbers(a,b,c)
