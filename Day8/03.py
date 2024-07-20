import math

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: ")) 
coverage = 5

def paint_clac(height, width, cover):  
    area = height * width
    num_of_cans = math.ceil(area / cover)
    print(f"You'll need {num_of_cans} cans of paint.")

paint_clac(height=test_h, width=test_w, cover=coverage)  
