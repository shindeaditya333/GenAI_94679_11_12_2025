import Calculator
import geometry as geo
import greeting

greeting.greet("XYZ")

num1 = int(input("enter num1: "))
num2 = int(input("enter num2: "))

Calculator.add(num1, num2)
Calculator.multiply(num1, num2)

geo.calc_rect_area(num1, num2)
geo.calc_rect_peri(num1, num2)