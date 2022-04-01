class Person:
    def __init__(self, args):
        self.name = args[0]
        self.lastname = args[1]
        self.dateofbirth = args[2]

    def printdetails(self):
        print(f"Name :{self.name}")
        print(f"Last Name :{self.lastname}")
        print(f"Date of birth :{self.dateofbirth}")

    def is_eligible(self, age):
        if age >= 18:
            return True
        else:
            return False


x = Person(["Harish", "D", "28 May, 2000"])

x.printdetails()
print(x.is_eligible(14))