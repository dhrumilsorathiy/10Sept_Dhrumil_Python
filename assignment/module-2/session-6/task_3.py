teams = ["GT", "MI", "RCB", "RR", "CSK"]
points = [12, 8, 18, 16, 10]
team_dict = dict(zip(teams, points))
for team, point in team_dict.items():
    if point > 10:
        print(team, point)