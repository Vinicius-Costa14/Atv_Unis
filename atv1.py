'''Faça um programa que leia a idade de uma pessoa expressa em dias e mostre-a expressa em anos, meses e dias.'''

class Person:
    def __init__(self, name, age_in_days):
        self.name = name
        self.age_in_days = age_in_days
    
    def convert_age(self):
        years = self.age_in_days // 365
        remaining_days = self.age_in_days % 365
        months = remaining_days // 30
        days = remaining_days % 30
        return years, months, days
    
def main():
    name = input("Enter your name: ")
    age_in_days = int(input("Enter your age in days: "))
    
    person = Person(name, age_in_days)
    years, months, days = person.convert_age()
    
    print(f"{person.name}, your age is {years} years, {months} months, and {days} days.")
    
if __name__ == "__main__":
    main()
    