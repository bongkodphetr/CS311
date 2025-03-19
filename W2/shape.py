import findarea
def displaymenu():
    print("="*45)
    print("  (T) : Triangle")
    print("  (R) : Rectangle")
    print("  (C) : Circle")
    print("="*45)
def getinput() :
    displaymenu()
    menu = input("Select your shape menu : ").upper()
    if menu == "T" :
        base = int(input("Base : "))
        height = int(input("Height : "))
        area = findarea.triangle(base,height)
        print(f"Area of trinagle = {area:0.2f}")
    elif menu == "C" :
        radius = int(input("Radius : "))
        area = findarea.circle(radius)
        print(f"Area of trinagle = {area:0.2f}")
    elif menu == "R" :
        width = int(input("Width : "))
        length = int(input("Length : "))
        area = findarea.rectangle(width,length)
        print(f"Area of trinagle = {area:0.2f}")
getinput()