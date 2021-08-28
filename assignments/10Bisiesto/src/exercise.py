def es_bisiesto(x):
    if ((x%4==0) and (x%100!=0)) or ((x%100==0) and (x%400==0)):
        z = "True"
    else:
        z = "False"
    return z

def main():
    if x > 0:
        print(es_bisiesto(x))
    else:
        print("Datos invalidos")
    pass

x = int(input("Dame un año: "))

if __name__=='__main__':
    main()
