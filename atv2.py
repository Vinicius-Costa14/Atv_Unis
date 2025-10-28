'''Elaborar um programa que lê 3 valores a,b,c e verifica se eles formam ou não um triângulo. 
Supor que os valores lidos são inteiros e positivos. Caso os valores formem um triângulo, 
calcular e escrever a área deste triângulo. Se não formam triângulo escrever os valores lidos. (Se a > b + c não formam triângulo algum, se a é o maior).
'''
class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def is_triangle(self):
        return self.a < self.b + self.c and self.b < self.a + self.c and self.c < self.a + self.b
    
    def area(self):
        s = (self.a + self.b + self.c) / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5

def main():
    a = int(input("Enter side a: "))
    b = int(input("Enter side b: "))
    c = int(input("Enter side c: "))
    
    triangle = Triangle(a, b, c)
    
    if triangle.is_triangle():
        area = triangle.area()
        print(f"The sides form a triangle. The area is: {area:.2f}")
    else:
        print(f"The sides do not form a triangle. The values are: a={a}, b={b}, c={c}")

if __name__ == "__main__":
    main()