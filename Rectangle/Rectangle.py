# Kyle Stewart CIS261 Rectangle

class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def perimeter(self):
        return 2 * (self.height + self.width)

    def area(self):
        return self.height * self.width

    def print_rectangle(self):
        for i in range(self.height):
            if i == 0 or i == self.height - 1:
                print('* ' * self.width)
            else:
                print('* ' + '  ' * (self.width - 2) + '*')

def main():
    height = int(input("Enter the height of the rectangle: "))
    width = int(input("Enter the width of the rectangle: "))

    rect = Rectangle(height, width)

    print(f"\nHeight: {rect.height}")
    print(f"Width: {rect.width}")
    print(f"Perimeter: {rect.perimeter()}")
    print(f"Area: {rect.area()}\n")

    rect.print_rectangle()

    while True:
        cont = input("\nContinue? (y/n): ").lower()
        if cont == 'y':
            main()
        elif cont == 'n':
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

if __name__ == "__main__":
    main()
