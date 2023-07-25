from abc import ABC, abstractmethod

class jsonify(ABC):
    @abstractmethod
    def toJSON(self):
        pass

class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calcArea(self):
        pass


class Circle(GraphicShape,jsonify):
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return 3.14 * (self.radius ** 2)
    
    def toJSON(self):
        return f"{{\" square\" : {str(self.calcArea())} }}"


c = Circle(10)
print(c.calcArea())
print(c.toJSON())