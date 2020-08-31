team=input()
games_count=int(input())

total_time=0
penalties=False
additional_time=False
counter1=0
counter2=0
for games in range (games_count):
    time=int(input())
    total_time+=time
    if 120>= time >90:
        additional_time=True
        counter1+=1
    if time>120:
        penalties=True
        counter2+=1

average_time=total_time/games_count

print(f"{team} has played {total_time:} minutes. Average minutes per game: {average_time:.2f}")
print(f"Games with penalties: {counter2}")
print(f"Games with additional time: {counter1}")
