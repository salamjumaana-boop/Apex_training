while True:
    print("\n1. Circle")
    print("2. Rectangle")
    print("3. Square")
    print("4. Exit")

    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        radius = float(input("Enter radius: "))
        area = 3.14 * radius * radius
        print("Area of circle =", int(area))

    elif choice == 2:
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        area = length * width
        print("Area of rectangle =", int(area))

    elif choice == 3:
        side = float(input("Enter side: "))
        area = side * side
        print("Area of square =", int(area))

    elif choice == 4:
        print("Program exited.")
        break

    else:
        print("Invalid choice. Please enter 1-4.")
