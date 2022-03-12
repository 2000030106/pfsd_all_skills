import math as m
class A:
    def Circle(self, radius):
        self.radius=radius
        Area=m.pi*radius*radius
        Perimetre=2*m.pi*radius
        print("The Area of Circle is", Area)
        print("The Area of Perimetre is", Perimetre)
    def Square(self,side):
        self.side=side
        Area=side*side
        Perimetre=4*side
        print("The Area of Square is", Area)
        print("The Perimetre of Square is", Perimetre)
    def Rectangle(self,side1,side2):
        self.side1=side1
        self.side2=side2
        Area=side1*side2
        Perimetre=2*(side1+side2)
        print("The Area of Rectangle is", Area)
        print("The Perimetre of Rectangle is ", Perimetre)
if __name__ == "__main__":
    a = A()
    side = eval(input("Enter the side of Square: "))
    radius = eval(input("Enter the Radius of Circle: "))
    r1 = eval(input("Enter the 1st side of Rectangle: "))
    r2 = eval(input("Enter the 2nd side of Rectangle: "))
    a.Square(side)
    a.Circle(radius)
    a.Rectangle(r1, r2)