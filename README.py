def concrete_volume(length, width, depth):
    return length * width * depth

def steel_weight(dia, length):
    weight_per_m = (dia * dia) / 162
    return weight_per_m * length

def brickwork_quantity(length, width, height):
    return length * width * height

print("=== Construction Quantity Estimation Agent ===")

while True:
    print("\n1. Concrete Volume")
    print("2. Steel Weight")
    print("3. Brickwork Quantity")
    print("4. Exit")

    choice = input("Select Option: ")

    if choice == "1":
        l = float(input("Length (m): "))
        w = float(input("Width (m): "))
        d = float(input("Depth (m): "))
        print(f"Concrete Volume = {concrete_volume(l,w,d):.3f} m³")

    elif choice == "2":
        dia = float(input("Bar Diameter (mm): "))
        length = float(input("Total Length (m): "))
        print(f"Steel Weight = {steel_weight(dia,length):.2f} kg")

    elif choice == "3":
        l = float(input("Length (m): "))
        w = float(input("Width (m): "))
        h = float(input("Height (m): "))
        print(f"Brickwork Quantity = {brickwork_quantity(l,w,h):.3f} m³")

    elif choice == "4":
        break

    else:
        print("Invalid Option")
