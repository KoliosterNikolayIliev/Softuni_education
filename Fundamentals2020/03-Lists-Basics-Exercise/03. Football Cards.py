team_A = [1] * 11
team_B = [1] * 11

cards = set(input().split(' '))

for card in cards:
    tokens = card.split('-')
    team = tokens[0]
    player = int(tokens[1])
    index = player - 1

    if team == 'A':
        team_A[index] = 0

    if team == 'B':
        team_B[index] = 0
print(f'Team A - {sum(team_A)}; Team B - {sum(team_B)}')

if sum(team_A) < 7 or sum(team_B) < 7:
    print('Game was terminated')
