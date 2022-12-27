def is_triangle(side1, side2, side3):
    # check if all sides are > 0
    if side1 > 0 and side2 > 0 and side3 > 0:
        # check if side1+side2 > side3 OR side2+side > side1 OR ... 
        if side1+side2 >= side3 and side2+side3 >= side1 and side3+side1 >= side2:
            return True

    return False
#print(is_triangle(0,0,0))
#print(is_triangle(10,0,0))
#print(is_triangle(10,20,0))
#print(is_triangle(10,20,30))
#print(is_triangle(10,1,1))
#print(is_triangle(10,5,5))
#print(is_triangle(10,5,4))
def is_equilateral(side1, side2, side3):
    '''check if the sides are a Triangle AND all sides are equal'''
    return is_triangle(side1, side2, side3) and (side1 == side2 == side3)


# print(is_equilateral(10, 10, 10))
#  print(is_equilateral(0, 0, 0))
# print(is_equilateral(5, 5, 5))
# print(is_equilateral(5, 5, 4))
#print(is_equilateral(5, 3, 4))
#print(is_equilateral(0.5, 0.5, 0.5))
#print(is_equilateral(10, 1, 1))
def is_scalene(side1, side2, side3):
	return is_triangle (side1,side2,side3) and (side1!=side2 and side2!=side3 and side1!=side3)

#print(is_scalene(10, 10, 10))
#print(is_scalene(0, 0, 0))
#print(is_scalene(5, 5, 5))
#print(is_scalene(5, 5, 4))
#print(is_scalene(5, 3, 4))
#print(is_scalene(0.5, 0.5, 0.5))
#print(is_scalene (10, 1, 1))
def is_degenerate(side1, side2, side3):
	return is_triangle(side1,side2,side3) and (side1+side2>side3 and side2+side3>side1 and side3+side1>side2)
print(is_scalene(10, 10, 10))
print(is_scalene(0, 0, 0))
print(is_scalene(5, 5, 5))
print(is_scalene(5, 5, 4))
print(is_scalene(5, 3, 4))
print(is_scalene(0.5, 0.5, 0.5))
print(is_scalene (10, 1, 1))