def tarjetas(pa,pl):
    tpa = pa * 12
    tpl = pl * 35
    if tpa < tpl:
        x = tpa
    elif tpa > tpl:
        x = tpl
    return x

def main():
    print("El número máximo de tarjetas que se pueden hacer es: ", tarjetas(pa,pl))
    pass

pa = int(input("Dame la cantidad de pliegos de papel albanene: "))
pl = int(input("Dame la cantidad de plumones: "))

if __name__=='__main__':
    main()
