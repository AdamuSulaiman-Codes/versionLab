# calculator.py 
class Calculator: 
    def add(self, a, b): 
        """This method adds two numbers""" 
        return a + b 
    def subtract(self, a, b): 
        """This method subtracts two numbers""" 
        return a - b 
calc = Calculator() 
print("Welcome to the Advanced Calculator!") 
print("Version: 2.0.0") # Update version number 
print("Result of add(2, 2) is:", calc.add(2, 2)) 
print("Result of subtract(5, 3) is:", calc.subtract(5, 3)) 