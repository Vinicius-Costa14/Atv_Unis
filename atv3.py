#Faça um programa que leia 3 números inteiros e mostre o menor deles.

class NumberComparer:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def find_smallest(self):
        return min(self.x, self.y, self.z)

def main():
    x = int(input("Enter first integer: "))
    y = int(input("Enter second integer: "))
    z = int(input("Enter third integer: "))
    
    comparer = NumberComparer(x, y, z)
    smallest = comparer.find_smallest()
    
    print(f"The smallest number is: {smallest}")

if __name__ == "__main__":
    main()