side = float(input())
n_sheets = int(input())
sheet_area = float(input())

box_area = side * side * 6
total_sheet_area = 0

for i in range(1, n_sheets + 1):
    mod_sheet = sheet_area
    if i % 3 == 0:
        mod_sheet = 0.25 * sheet_area
    total_sheet_area += mod_sheet

percentage = (total_sheet_area / box_area)*100

print(f"You can cover {percentage:.2f}% of the box.")
