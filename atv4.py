#Implementar uma função que retorne verdadeiro se o número for primo (falso caso contrário). Testar de 1 a 100.

class PrimeChecker:
    def __init__(self, number):
        self.number = number
    
    def is_prime(self):
        if self.number <= 1:
            return False
        for i in range(2, int(self.number**0.5) + 1):
            if self.number % i == 0:
                return False
        return True

def main():
    for num in range(1, 101):
        checker = PrimeChecker(num)
        if checker.is_prime():
            print(f"{num} is a prime number.")
        else:
            print(f"{num} is not a prime number.")
            
if __name__ == "__main__":
    main()