steps_made = int(input())
step_length = float(input()) / 100
travel_distance = int(input())

total_steps_length = 0
for step in range(1, steps_made + 1):
    if step % 5 == 0:
        total_steps_length += 0.7 * step_length
    else:
        total_steps_length += step_length

percentage = (total_steps_length / travel_distance) * 100

print(f"You travelled {percentage:.2f}% of the distance!")
