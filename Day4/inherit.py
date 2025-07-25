class super1:
    def __init__(self):
        self.name = "Payal"
        self.roll = 26

    def show(self):
        print(self.name)
        print(self.roll)

class super2(super1):
    def __init__(self):
        super().__init__()  # Call the constructor of super1
        self.age = 20

    def display(self):
        print("Name:", self.name)
        print("Roll:", self.roll)
        print("Age:", self.age)
    
# Create an instance of super2
s2 = super2()
s2.display()  # Display the attributes of super2    