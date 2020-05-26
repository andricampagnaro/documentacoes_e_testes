class ShapeInterface():
    def draw(self): pass

class Circle(ShapeInterface):
    def draw(self):
        print('Circle.draw')

class Square(ShapeInterface):
    def draw(self):
        print('Square.draw')

class ShapeFactory():
    @staticmethod
    def get_shape(type):
        if type == 'circle':
            return Circle()
        if type == 'square':
            return Square()
        assert 0, f'Could not find the shape {type}'

if __name__ == '__main__':
    factory = ShapeFactory()
    square = factory.get_shape('square')
    print(square)
