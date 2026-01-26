import math

def paint_calculate(height, width):
    area = height * width
    cans = area / 5
    # Rounding up and saving back to the variable
    cans = math.ceil(cans)
    print(f"Total Cans Required to paint:{cans}")

paint_calculate(10, 20)
