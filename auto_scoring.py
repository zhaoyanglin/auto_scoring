"""
Zhaoyang Lin (Zee),
This program will computes win/loss record,
average score and average point spread of a sports team (or player).
"""

team_name = input('enter a team name: ')
num_games_played = input('enter how many games play: ')
#this test if the user enter letters when they should enter numbers
#reprompt the input if user enter letters
while num_games_played.isdigit() == False or int(num_games_played) <= 0:
    print('please enter a numbers greater than 0')
    num_games_played = input('enter how many games play: ')

#this function will calculate wins and lost, total point, and point diff which will be used for the point spread.
#everything will be kept in a array. 
def calculate_all():
    total_dif = 0
    home_total_points = 0
    wins = 0
    losts = 0
    for i in range(int(num_games_played)):
        print('\n***** Game {} *****'.format((i+1)))
        #testing home team points, making sure they are numbers and greater or equal to 0
        home_team_p = input('How many points did {} make? '.format(team_name))
        while home_team_p.isdigit() == False or int(home_team_p) < 0:
            print('please enter a numbers equal or greater than 0')
            home_team_p = input('How many points did {} make? '.format(team_name))

        #testing away team points, making sure they are numbers and greater or equal to 0
        away_team_p = input('How many points did the opponent make? ')
        while away_team_p.isdigit() == False or int(away_team_p) < 0:
                print('please enter a numbers equal or greater than 0')
                away_team_p = input('How many points did the opponent make? ')
            
        point_diff = abs(int(home_team_p) - int(away_team_p))
        total_dif += point_diff
        home_total_points += int(home_team_p)
    
        if int(home_team_p) > int(away_team_p):
            wins += 1
        elif int(away_team_p) > int(home_team_p):
            losts += 1
        else:
            print('draw')
    answers_ar = [total_dif, home_total_points, wins, losts]
    return answers_ar
        
#this function calculates the point spread
def point_diff(total_dif):
        average_point_diff = total_dif / int(num_games_played)
        return float(average_point_diff)
    
#this function calculates the points per game
def point_per_game(home_total_points):
    average_points_per_game = home_total_points / int(num_games_played)
    return float(average_points_per_game)

answers = calculate_all()

print('\nThe results are...\n')
print('The {} won {} and lost {}'.format(team_name, answers[2], answers[3]))
print('They scored a grand total of {} points.'.format(answers[1]))
print('They scored an average of {:.2f} points.'.format(point_per_game(answers[1])))
print('The average point spread was {:.2f}.'.format(point_diff(answers[0])))

