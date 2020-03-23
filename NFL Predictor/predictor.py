from sportsreference.nfl.teams import Teams
from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np
from os import path
from name_converter import get_team

# Constants
HOME = .5
AWAY = -.5
NEUTRAL = 0
WIN = 1
LOSS = 0

# Creates a nested dictionary that maps year and team abbreviation to team data
def generate_teams(year1, year2, include_interval=True):
    all_teams_dict = {}
    if include_interval:
        for year in range(year1, year2 + 1):
            teams = Teams(year)
            teams_dict = {}
            for team in teams:
                abbr = team.abbreviation
                teams_dict[abbr] = team
            all_teams_dict[year] = teams_dict
    else:
        teams = Teams(year1)
        teams_dict = {}
        for team in teams:
            abbr = team.abbreviation
            teams_dict[abbr] = team
        all_teams_dict[year1] = teams_dict
        teams = Teams(year2)
        teams_dict = {}
        for team in teams:
            abbr = team.abbreviation
            teams_dict[abbr] = team
        all_teams_dict[year2] = teams_dict
    return all_teams_dict

# Returns a numpy array that represents a team's strength using a variety of stats
# [points per game, points allowed per game, SOS, yards per play, turnovers per game,
# yards from penalties per game, offensive rating, defensive rating, home/away]
def get_team_vector(team, home_or_away):
    team_vector = np.array([team.points_for / team.games_played, team.points_against / team.games_played,
                            team.strength_of_schedule, team.yards_per_play, team.turnovers / team.games_played,
                            team.yards_from_penalties / team.games_played, team.offensive_simple_rating_system,
                            team.defensive_simple_rating_system, home_or_away])
    return team_vector

# Makes training data and writes it to x_file and y_file
def make_data(teams_dict, x_file, y_file, start_year, end_year):
    game_vectors = []
    result_vector = []
    for year in range(start_year, end_year + 1):
        teams = teams_dict[year]
        for team in teams.values():
            schedule = team.schedule
            for game in schedule:
                if game.type == 'Reg':
                    result = game.result
                    if result == 'Win':
                        result_num = WIN
                    else:
                        result_num = LOSS
                    if game.location == 'Home':
                        location = HOME
                    elif game.location == 'Away':
                        location = AWAY
                    else:
                        location = NEUTRAL

                    team_vector = get_team_vector(team, location)
                    opponent_vector = get_team_vector(teams_dict[year][game.opponent_abbr], -location)

                    game_vector = list(team_vector - opponent_vector)
                    result_vector.append(result_num)
                    game_vectors.append(game_vector)

    np_game_vectors = np.array(game_vectors)
    np_game_vectors = np_game_vectors.transpose()
    result_vector = np.array(result_vector)
    x_data = get_x_data(np_game_vectors)
    y_data = {'Result': result_vector}
    df_x = pd.DataFrame(x_data)
    df_y = pd.DataFrame(y_data)
    df_x.to_csv(x_file, index=False)
    df_y.to_csv(y_file, index=False)

# Uses logistic regression model to fit training data
def train(x_file, y_file):
    df = pd.read_csv(x_file)
    target = pd.read_csv(y_file)
    x_train = df
    y_train = target
    log_reg = LogisticRegression()
    log_reg.fit(x_train, y_train.values.ravel())
    return log_reg

# Tests model on teams from specified years
def test(model, teams_dict, start_year, end_year):
    correct = 0
    total = 0
    for year in range(start_year, end_year + 1):
        teams = teams_dict[year]
        for team in teams.values():
            schedule = team.schedule
            for game in schedule:
                if game.type == 'Reg':
                    if game.location == 'Home':
                        location = HOME
                    elif game.location == 'Away':
                        location = AWAY
                    else:
                        location = NEUTRAL
                    team_vector = get_team_vector(team, location)
                    opponent_vector = get_team_vector(teams_dict[year][game.opponent_abbr], -location)
                    game_vector = team_vector - opponent_vector
                    game_vector = game_vector.transpose()
                    x_data = get_x_data(game_vector)
                    x_test = pd.DataFrame([x_data])
                    prediction = model.predict(x_test)
                    result = game.result
                    if result == 'Win':
                        result = WIN
                    else:
                        result = LOSS
                    if prediction == result:
                        correct += 1
                    total += 1
    print('For the', start_year, '-', end_year, 'NFL seasons')
    print('Correct predictions:', correct)
    print('Total predictions:', total)
    print('Accuracy: {:.1%}'.format(correct / total))

# Gives the probability of a team winning a game
def predict(model):
    team = input('First Team:')
    while get_team(team) is None:
        team = input('Invalid name/abbreviation. Please try again.')
    team = get_team(team)
    year = int(input('Which season?'))
    location = input('Home, Away, or Neutral?').lower()
    while location != 'home' and location != 'away' and location != 'neutral':
        location = input('Invalid response. Please enter "Home", "Away", or "Neutral".')
    if location == 'home':
        location = HOME
    elif location == 'away':
        location = AWAY
    else:
        location = NEUTRAL
    opponent = input('Second Team:')
    while get_team(opponent) is None:
        opponent = input('Invalid name/abbreviation. Please try again.')
    opponent = get_team(opponent)
    opp_year = int(input('Which season?'))
    teams_dict = generate_teams(year, opp_year, False)
    team_vector = np.array(get_team_vector(teams_dict[year][team], location))
    opp_vector = np.array(get_team_vector(teams_dict[opp_year][opponent], -location))
    game_vector = team_vector - opp_vector
    x_data = get_x_data(game_vector)
    x = pd.DataFrame([x_data])
    probability = model.predict_proba(x)[0][1]
    print('The probability of the', year, teams_dict[year][team].name, 'beating the', opp_year,
          teams_dict[opp_year][opponent].name, 'is {:.1%}'.format(probability))

# Gives top 10 ranking for years specified
def rank(model, teams_dict, start_year, end_year):
    all_teams = []
    for year in range(start_year, end_year + 1):
        teams = teams_dict[year]
        for team in teams.keys():
            all_teams.append((team, year))
    # Uses first team in all_teams as baseline to compare to other teams
    rankings = {all_teams[0]: 0.5}
    starting_abbr = all_teams[0][0]
    starting_year = all_teams[0][1]
    starting_vector = get_team_vector(teams_dict[starting_year][starting_abbr], NEUTRAL)
    for team_index in range(1, len(all_teams)):
        team = all_teams[team_index]
        abbr = team[0]
        year = team[1]
        team_vector = get_team_vector(teams_dict[year][abbr], NEUTRAL)
        game_vector = starting_vector - team_vector
        game_vector = game_vector.transpose()
        x_data = get_x_data(game_vector)
        x = pd.DataFrame([x_data])
        win_prob = model.predict_proba(x)[0][0]
        rankings[team] = win_prob
    rankings = {k: v for k, v in sorted(rankings.items(), key=lambda item: item[1], reverse=True)}
    i = 1
    for team in rankings.keys():
        abbr = team[0]
        year = team[1]
        t = teams_dict[year][abbr]
        index = str(i) + '.'
        print(index, year, t.name)
        i += 1

# Helper method that returns the dictionary used for creating the x_data Pandas DataFrame
def get_x_data(np_game_vectors):
    x_data = {'Points For': np_game_vectors[0],
              'Points Against': np_game_vectors[1],
              'Strength of Schedule': np_game_vectors[2],
              'Yards Per Play': np_game_vectors[3],
              'Turnovers': np_game_vectors[4],
              'Yards From Penalties': np_game_vectors[5],
              'Offensive Rating': np_game_vectors[6],
              'Defensive Rating': np_game_vectors[7],
              'Location': np_game_vectors[8]}
    return x_data

def main():
    command = input('Enter "train" to train a new model, "test" to test the model over a range of years, "predict" to '
                    'predict a game\'s outcome, or "rank" to show the model\'s rankings of the teams').lower()
    while command != 'train' and command != 'test' and command != 'predict' and command != 'rank':
        command = input('Invalid command. Enter "train" to train a new model, "test" to test'
                        ' the model over a range of years, "predict" to predict a game\'s outcome,'
                        ' or "rank" to show the model\'s rankings of the teams').lower()
    if command == 'train':
        start_year = int(input('Start year:'))
        end_year = int(input('End year:'))
        teams_dict = generate_teams(start_year, end_year)
        make_data(teams_dict, 'data.csv', 'results.csv', start_year, end_year)
    else:
        if not path.exists('data.csv') or not path.exists('results.csv'):
            print('No data found to create model. Rerun and train a model first')
        else:
            model = train('data.csv', 'results.csv')
            if command == 'test' or command == 'rank':
                start_year = int(input('Start year:'))
                end_year = int(input('End year:'))
                teams_dict = generate_teams(start_year, end_year)
                if command == 'test':
                    test(model, teams_dict, start_year, end_year)
                else:
                    rank(model, teams_dict, start_year, end_year)
            else:
                predict(model)
    exit(0)

if __name__ == '__main__':
    main()