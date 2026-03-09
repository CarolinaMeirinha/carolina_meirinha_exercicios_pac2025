def ex15():
    for i in range(256):
        print(str(i) + " = " + chr(i))
        if (i+1) % 20 == 0:
            resp = input("Continuar? (s/n): ")
            if resp != "s":
                break

ex15()