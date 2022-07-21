team = int(input())

played = int(input())

gamesleft = [(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)]
points = {1:0,2:0,3:0,4:0}

for i in range(played):
    game = list(map(int, input().split()))
    team1 = game[0]
    team2 = game[1]
    score1 = game[2]
    score2 = game[3]
    gamenum = tuple(sorted((team1,team2)))
    gamesleft.remove(gamenum)
    if score1 == score2:
        points[team1] += 1
        points[team2] += 1
        continue
    elif score1 > score2:
        points[team1] += 3
        continue
    else:
        points[team2] += 3

def chances(points,gamesleft, WinTeam):
    numbers = [i for i in range(len(gamesleft))]
    
            
        
        

