import findarea as f
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
        #call function in module
        area = f.triangle(base,height)
        print(f"Area of trinagle = {area:0.2f}")
    elif menu == "C" :
        radius = int(input("Radius : "))
        #call function in module
        area = f.circle(radius)
        print(f"Area of trinagle = {area:0.2f}")
    elif menu == "R" :
        width = int(input("Width : "))
        length = int(input("Length : "))
        #call function in module
        area = f.rectangle(width,length)
        print(f"Area of trinagle = {area:0.2f}")
getinput()