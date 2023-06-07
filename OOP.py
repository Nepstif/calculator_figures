import math
from abc import ABC, abstractmethod


class Shape(ABC):
    _title = 'Фигура'

    @abstractmethod
    def area_calculation(self):
        pass

    @abstractmethod
    def perimeter_calculation(self):
        pass


class Triangle(Shape):
    _title = 'Треугольник'

    @classmethod
    def classmethod(cls):
        side_a = abs(float(input("Please enter side a: ")))
        side_b = abs(float(input("Please enter side b: ")))
        side_c = abs(float(input("Please enter side c: ")))
        return side_a, side_b, side_c

    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def area_calculation(self):
        half = self.perimeter_calculation() / 2
        return math.sqrt(half * (half - self.side_a) *
                         (half - self.side_b) * (half - self.side_c))

    def perimeter_calculation(self):
        return self.side_a + self.side_b + self.side_c

    def median_calculation(self):
        median_side_a = (math.sqrt(2 * self.side_b ** 2 + 2 * self.side_c ** 2
                                   - self.side_a ** 2)) / 2
        median_side_b = (math.sqrt(2 * self.side_a ** 2 + 2 * self.side_c ** 2
                                   - self.side_b ** 2)) / 2
        median_side_c = (math.sqrt(2 * self.side_a ** 2 + 2 * self.side_b ** 2
                                   - self.side_c ** 2)) / 2
        return f"""The medians of the triangle were as follows: 
        from the top of the corner a: {median_side_a};
        from the top of the corner b: {median_side_b};
        from the top of the corner c: {median_side_c}."""

    def __repr__(self):
        return f"<Figure name: {self._title}, area: {self.area_calculation()}, perimeter: {self.perimeter_calculation()}, " \
               f" median angular: {self.median_calculation()}>"


class Pyramid_three_sides(Triangle):
    _title = 'Трехсторонняя пирамида'

    @classmethod
    def classmethod(cls):
        side_a = abs(float(input("Please enter side a: ")))
        side_b = abs(float(input("Please enter side a: ")))
        side_c = abs(float(input("Please enter side a: ")))
        height = abs(float(input("Please enter side height: ")))
        return side_a, side_b, side_c, height

    def __init__(self, side_a, side_b, side_c, height):
        super().__init__(side_a, side_b, side_c)
        self.height = height

    def area_calculation(self):
        pass

    def volume_calculator(self):
        return Triangle.area_calculation(self) * self.height / 3

    def __repr__(self):
        return f"<Figure name: {self._title}, volume: {self.volume_calculator()}"


class Square(Shape):
    _title = 'Квадрат'

    @classmethod
    def classmethod(cls):
        side_a = abs(float(input("Please enter side a: ")))
        return side_a

    def __init__(self, side_a):
        self.side_a = side_a

    def area_calculation(self):
        return self.side_a ** 2

    def perimeter_calculation(self):
        return self.side_a * 4

    def __repr__(self):
        return f"<Figure name: {self._title}, area: {self.area_calculation()}, perimeter: {self.perimeter_calculation()}"


class Rhombus(Square):
    _title = "Ромб"

    @classmethod
    def classmethod(cls):
        side_a = abs(float(input("Please enter side a: ")))
        height = abs(float(input("Please enter side height: ")))
        return side_a, height

    def __init__(self, side_a, height):
        super().__init__(side_a)
        self.height = height

    def area_calculation(self):
        return self.side_a * self.height

    def perimeter_calculation(self):
        return Square.perimeter_calculation(self)

    def __repr__(self):
        return f"<Figure name: {self._title}, area: {self.area_calculation()}, perimeter: {self.perimeter_calculation()}"


class Cube(Square):
    _title = 'Куб'

    @classmethod
    def classmethod(cls):
        side_a = abs(float(input("Please enter side a: ")))
        return side_a

    def area_calculation(self):
        return 6 * Square.area_calculation(self)  # Площадь одного квадрата

    def perimeter_calculation(self):
        return self.side_a * 12

    def volume_calculator(self):
        return self.side_a ** 3

    def __repr__(self):
        return f"<Figure name: {self._title}, area: {self.area_calculation()}, perimeter: {self.perimeter_calculation()}," \
               f"volume: {self.volume_calculator()}"


class Rectangle(Square):
    _title = 'Прямоугольник'

    @classmethod
    def classmethod(cls):
        side_a = abs(float(input("Please enter side a: ")))
        side_b = abs(float(input("Please enter side b: ")))
        return side_a, side_b

    def __init__(self, side_a, side_b):
        super().__init__(side_a)
        self.side_b = side_b

    def area_calculation(self):
        return self.side_a * self.side_b

    def perimeter_calculation(self):
        return 2 * (self.side_a + self.side_b)

    def __repr__(self):
        return f"<Figure name: {self._title}, area: {self.area_calculation()}, perimeter: {self.perimeter_calculation()}"


class Pyramid_four_sides(Rectangle):
    _title = 'Четырехсторонняя пирамида'

    @classmethod
    def classmethod(cls):
        side_a = abs(float(input("Please enter side a: ")))
        side_b = abs(float(input("Please enter side b: ")))
        height = abs(float(input("Please enter side height: ")))
        return side_a, side_b, height

    def __init__(self, side_a, side_b, height):
        super().__init__(side_a, side_b)
        self.height = height

    def area_calculation(self):
        pass

    def volume_calculator(self):
        return Rectangle.area_calculation(self) * self.height / 3

    def __repr__(self):
        return f"<Figure name: {self._title}, volume: {self.volume_calculator()}"


class Parallelepiped(Rectangle):
    _title = 'Параллелепипед'

    @classmethod
    def classmethod(cls):
        side_a = abs(float(input("Please enter side a: ")))
        side_b = abs(float(input("Please enter side b: ")))
        height = abs(float(input("Please enter side height: ")))
        return side_a, side_b, height

    def __init__(self, side_a, side_b, height):
        super().__init__(side_a, side_b)
        self.height = height

    def area_calculation(self):
        # Площадь основания: прямоугольник + бокавая площадь
        return 2 * (self.side_a * self.side_b + self.side_a * self.height
                    + self.side_b * self.height)

    def perimeter_calculation(self):
        return Rectangle.perimeter_calculation(self) * 2 + (self.height * 4)

    def volume_calculator(self):
        return Rectangle.area_calculation(self) * self.height  # Площадь основания на высоту

    def __repr__(self):
        return f"<Figure name: {self._title}, area: {self.area_calculation()}, perimeter: {self.perimeter_calculation()}" \
               f" volume: {self.volume_calculator()}"


class Trapezoid(Rectangle):
    _title = 'Трапеция'

    @classmethod
    def classmethod(cls):
        side_a = abs(float(input("Please enter side a: ")))
        side_b = abs(float(input("Please enter side b: ")))
        side_c = abs(float(input("Please enter side c: ")))
        side_d = abs(float(input("Please enter side d: ")))
        height = abs(float(input("Please enter side height: ")))
        return side_a, side_b, side_c, side_d, height

    def __init__(self, side_a, side_b, side_c, side_d, height):
        super().__init__(side_a, side_b)
        self.side_c = side_c
        self.side_d = side_d
        self.height = height

    def area_calculation(self):
        return (self.side_a + self.side_b) / 2 * self.height

    def perimeter_calculation(self):
        return self.side_a + self.side_b + self.side_c + self.side_d

    def __repr__(self):
        return f"<Figure name: {self._title}, area: {self.area_calculation()}, perimeter: {self.perimeter_calculation()}"


class Circle(Shape):
    _title = 'Круг'

    @classmethod
    def classmethod(cls):
        radius = abs(float(input("Please enter radius: ")))
        return radius

    def __init__(self, radius):
        self.radius = radius
        self.number_Pi = math.pi

    def area_calculation(self):
        return self.number_Pi * (self.radius ** 2)

    def perimeter_calculation(self):
        pass

    def __repr__(self):
        return f"<Figure name: {self._title}, area: {self.area_calculation()}"


class Sphere(Circle):
    _title = 'Сфера'

    @classmethod
    def classmethod(cls):
        radius = abs(float(input("Please enter radius: ")))
        return radius

    def area_calculation(self):
        return 4 * Circle.area_calculation(self)

    def volume_calculator(self):
        return self.area_calculation() * self.radius / 3

    def __repr__(self):
        return f"<Figure name: {self._title}, area: {self.area_calculation()}, volume: {self.volume_calculator()}"


class Cylinder(Circle):
    _title = 'Цилиндр'

    @classmethod
    def classmethod(cls):
        radius = abs(float(input("Please enter radius: ")))
        height = abs(float(input("Please enter height: ")))
        return radius, height

    def __init__(self, radius, height):
        super().__init__(radius)
        self.height = height

    def area_calculation(self):
        return 2 * Circle.area_calculation(self) + 2 * self.number_Pi * self.radius * self.height

    def volume_calculator(self):
        return Circle.area_calculation(self) * self.height

    def __repr__(self):
        return f"<Figure name: {self._title}, area: {self.area_calculation()}, volume: {self.volume_calculator()}"


class Cone(Circle):
    _title = 'Конус'

    @classmethod
    def classmethod(cls):
        radius = abs(float(input("Please enter radius: ")))
        height = abs(float(input("Please enter height: ")))
        return radius, height

    def __init__(self, radius, height):
        super().__init__(radius)
        self.height = height

    def area_calculation(self):
        length = math.sqrt((self.radius ** 2 + self.height ** 2))
        area = Circle.area_calculation(self) + (self.number_Pi * self.radius * length)
        return area

    def perimeter_calculation(self):
        pass

    def volume_calculator(self):
        return Circle.area_calculation(self) * self.height / 3

    def __repr__(self):
        return f"<Figure name: {self._title}, area: {self.area_calculation()}, volume: {self.volume_calculator()} >"


list_figures = [Triangle, Pyramid_three_sides, Square, Rhombus, Cube, Pyramid_four_sides, Parallelepiped,
                Circle, Sphere, Cylinder, Cone]


def conclusion_figures(list_figures):
    figure = input("Please enter figure: ")
    for element_figure in list_figures:
        if element_figure._title == figure.capitalize():
            return element_figure

    if element_figure._title != figure.capitalize():
        print("Selected shape is missing")
        return conclusion_figures(list_figures)


def conclusion(figure, options_figure):
    if isinstance(options_figure, float):
        return figure(options_figure)
    elif isinstance(options_figure, tuple):
        return figure(*options_figure)


def calculator():
    for element in list_figures:
        print(element._title)
    figure = conclusion_figures(list_figures)
    options_figure = figure.classmethod()
    my_figure = conclusion(figure, options_figure)
    print(my_figure)


def run_calculator():
    while True:
        answer = input("Do you want to work as a calculator of geometric shapes? y/n: ")
        if ((answer == "y") or (answer == "Y")):
            calculator()
        elif ((answer == "n") or (answer == "N")):
            break
        else:
            print("Please select one of the answer options")
            run_calculator()

run_calculator()

