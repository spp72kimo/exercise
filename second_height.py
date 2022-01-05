students = [['Mary', 158],['Steven', 174], ['Kelvin', 168], ['Alice', 168]]
def second_height(students=[]):
    height = [h[1] for h in students]
    result = sorted(height, reverse=True)
    second_height_value = result[1]
    second_name = [n[0] for n in students if n[1] == second_height_value]
    for name in second_name:
        print(name)

second_height(students)