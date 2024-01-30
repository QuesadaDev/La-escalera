def escalera(escalones):
    if escalones > 0:
        for escalon in range(escalones + 1):
            space = " " * (escalones-escalon)
            draw = "_" if escalon == 0 else "_|"
            print(f"{space} {draw}")
    if escalones < 0:
        for escalon in range(abs(escalones) + 1):
            space = " " * ((escalon*2)-1)
            draw = "_" if escalon == 0 else "|_"
            print(f"{space} {draw}")
    if escalones == 0:
        print("__")


escalera(-4)
escalera(0)
escalera(-20)
escalera(20)

