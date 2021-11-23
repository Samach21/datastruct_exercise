teams = input('Enter Input : ').split('/')
teams = list(map(lambda team: team.split(','), teams))

result = []
for i in range(len(teams)):
    name = teams[i][0]
    wins, loss, draws, scored, conceded = list(map(int, teams[i][1:]))
    points = (3 * wins) + (0 * loss) + (1 * draws)
    gd = scored - conceded
    index = 0
    for j in range(len(result)):
        if points < result[j][1]['points']:
                index += 1
        elif points == result[j][1]['points']:
            if gd < result[j][2]['gd']:
                index += 1
        
    result.insert(index, [name, {'points': points}, {'gd': gd}])

print('== results ==')
for i in result:
    print(i)