import math

def area(b,h):
    a = math.trunc(b * h)
    return a

def main():
    if b > 0 and h > 0:
        print("El área del rectángulo es: ", area(b,h))
    else:
        print("Datos invalidos")
    pass

b = float(input("Dame la base: "))
h = float(input("Dame la altura: "))

if __name__=='__main__':
    main()
