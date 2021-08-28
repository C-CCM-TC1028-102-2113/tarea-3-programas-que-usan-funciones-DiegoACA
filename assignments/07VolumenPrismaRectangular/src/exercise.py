
def area(b,h):
    a = b*h
    return a

def volumen(b,h,p):
    v = area(b,h) * p
    return v 

def main():
    print("El volumen del prisma es: ", volumen(b,h,p))
    pass

b = float(input("Dame la base: "))
h = float(input("Dame la altura: "))
p = float(input("Dame la profundidad: "))

if __name__=='__main__':
    main()
