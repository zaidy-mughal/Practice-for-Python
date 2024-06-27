from Shape import Shape
from Circle import Circle
from Rectangle import Rectangle
from Triangle import Triangle


allShapes = []
shape = None
print("\n====== Shapes Area Calculation System ======\n")

while True:
    print("\n1. Add Shape")
    print("2. Remove Shape")
    print("3. Show Area of Shape")
    print("4. Show All Shapes")
    print("5. Press Other than 1-4 to Close.")

    choice = int(input("\nEnter your choice: "))
        
    if choice == 1:
        while True:
            type = input("Which Shape do you want to Add\nCircle \nRectangle \nTriangle \nType: ")
            if type == "Circle":
                color = input("Enter Circle's Color: ")
                radius = float(input("Enter Circle's Radius: "))
                shape = Circle(type,color,radius)
                allShapes.append(shape)

            elif type == "Rectangle":
                color = input("Enter Rectangle's Color: ")
                length = float(input("Enter Length: "))
                width = float(input("Enter Width: "))
                shape = Rectangle(type,color,length,width)
                allShapes.append(shape)

            elif type == "Triangle":
                color = input("Enter Triangle's Color: ")
                base = float(input("Enter Base: "))
                height = float(input("Enter Height: "))
                shape = Triangle(type,color,base,height)
                allShapes.append(shape)
            
            else:
                break
        print("Shape Added Successfully")


    elif choice == 2:
        type = input("Which Shape do you want to Remove\nCircle \nRectangle \nTriangle \nType: ")

        for shape in allShapes:
            if shape.type == type:
                allShapes.remove(shape)
                print("Shape removed Successfully!")
                break
        else:
            print("Shape Not Found!")

        
    elif choice == 3:
        if shape is not None:
            print(f"Area of Last Added Shape is: {shape.calculateArea():.2f}")
        else:
            print("Add Shape First!")


    elif choice == 4:
        for shape in allShapes:
            print(shape)

    else:
        break