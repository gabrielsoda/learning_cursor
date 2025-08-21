import time

class Calculator:
    def __init__(self):
        print("Welcome to the calculator!")
        time.sleep(1)
        print("--------------------------------")

        pass
    
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Division by zero is not allowed!")
        return a / b
    
    def power(self, a, b):
        # Handle cases where power operation might cause issues
        if a == 0 and b < 0:
            raise ValueError("Error: Cannot raise 0 to a negative power!")
        if abs(b) > 1000:
            raise ValueError("Error: Power exponent too large (max 1000)!")
        return a ** b
    
    def square_root(self, a):
        if a < 0:
            raise ValueError("Cannot calculate square root of negative number!")
        return a ** 0.5
    
    def display_menu(self):
        print("Calculator Menu:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power")
        print("6. Square Root")
        print("7. Exit")

    def main(self):
        try:
            while True:
                self.display_menu()
                choice = input("Enter your choice: ").strip()
                
                if choice == "1":
                    try:
                        a = float(input("Enter first number: "))
                        b = float(input("Enter second number: "))
                        result = self.add(a, b)
                        print(f"Result: {result}")
                    except KeyboardInterrupt:
                        raise
                    except Exception as e:
                        print(f"Error: {e}")
                    for i in range(3):
                        print(".", end="", flush=True)
                        time.sleep(0.8)
                    print()
                    
                elif choice == "2":
                    try:
                        a = float(input("Enter first number: "))
                        b = float(input("Enter second number: "))
                        result = self.subtract(a, b)
                        print(f"Result: {result}")
                    except KeyboardInterrupt:
                        raise
                    except Exception as e:
                        print(f"Error: {e}")
                    for i in range(3):
                        print(".", end="", flush=True)
                        time.sleep(0.8)
                    print()
                    
                elif choice == "3":
                    try:
                        a = float(input("Enter first number: "))
                        b = float(input("Enter second number: "))
                        result = self.multiply(a, b)
                        print(f"Result: {result}")
                    except KeyboardInterrupt:
                        raise
                    except Exception as e:
                        print(f"Error: {e}")
                    for i in range(3):
                        print(".", end="", flush=True)
                        time.sleep(0.8)
                    print()
                    
                elif choice == "4":
                    try:
                        a = float(input("Enter first number: "))
                        b = float(input("Enter second number: "))
                        result = self.divide(a, b)
                        print(f"Result: {result}")
                    except KeyboardInterrupt:
                        raise
                    except Exception as e:
                        print(f"Error: {e}")
                    for i in range(3):
                        print(".", end="", flush=True)
                        time.sleep(0.8)
                    print()
                    
                elif choice == "5":
                    try:
                        a = float(input("Enter base number: "))
                        b = float(input("Enter exponent: "))
                        result = self.power(a, b)
                        print(f"Result: {result}")
                    except KeyboardInterrupt:
                        raise
                    except Exception as e:
                        print(f"Error: {e}")
                    for i in range(3):
                        print(".", end="", flush=True)
                        time.sleep(0.8)
                    print()
                    
                elif choice == "6":
                    try:
                        a = float(input("Enter the number: "))
                        result = self.square_root(a)
                        print(f"Result: {result}")
                    except KeyboardInterrupt:
                        raise
                    except Exception as e:
                        print(f"Error: {e}")
                    time.sleep(2)
                    
                elif choice == "7":
                    print("See you next time!")
                    time.sleep(1)                
                    print("Exiting the calculator...")
                    time.sleep(1)
                    break
                    
                else:
                    print("Invalid choice. Please try again.")
                    time.sleep(2)
                    
        except KeyboardInterrupt:
            print("\n\nCalculator interrupted by user.")
            print("Exiting gracefully...")
            time.sleep(1)
        except Exception as e:
            print(f"\nUnexpected error occurred: {e}")
            print("Exiting calculator...")
            time.sleep(2)

if __name__ == "__main__":
    calculator = Calculator()
    calculator.main()

