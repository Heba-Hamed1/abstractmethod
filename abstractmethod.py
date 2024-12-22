from abc import ABC, abstractmethod 
class Shape(ABC):
    
    @abstractmethod 
    def area(self):
        pass 
    
    @abstractmethod 
    def perimeter(self):
        pass

class Rectangle(Shape):
    
    def __init__(self, width, height):
        self.width = width 
        self.height = height 
        
    def area(self):
        return self.height * self.width
    
    def perimeter(self):
        return 2 * (self.height + self.width)


rectangle = Rectangle(5, 8)
print("Area:", rectangle.area())
print("Perimeter:", rectangle.perimeter())
