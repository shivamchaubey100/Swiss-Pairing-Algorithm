import pandas as pd
import random

def pairings(teams, previous_pairings):
    num= len(teams)
    byeTeamIndex = random.randint(1, num)
    newTeams = teams.drop(teams.index[byeTeamIndex-1])

    # pairing = [(newTeams.loc[newTeams.index[i]],newTeams.loc[newTeams.index[i+1]]) for i in range(0, len(newTeams), 2)]
    # printPairing = [(newTeams.loc[newTeams.index[i], 'Team Name'],newTeams.loc[newTeams.index[i+1], 'Team Name']) for i in range(0, len(newTeams), 2)]

    i = 0
    j=1
    used_j = []
    pairing = []
    printPairing = []
    # print(newTeams)
    while i < len(newTeams):
        # print(i, j)
        if j >= len(newTeams):
            break
        while frozenset((newTeams.loc[newTeams.index[i], 'Team Name'],newTeams.loc[newTeams.index[j], 'Team Name'])) in previous_pairings:
            j=j+1
            while j in used_j:
                j += 1
            if j == len(newTeams):
                j= j-1
                break
            

        pairing.append((newTeams.loc[newTeams.index[i]],newTeams.loc[newTeams.index[j]]))
        printPairing.append((newTeams.loc[newTeams.index[i], 'Team Name'],newTeams.loc[newTeams.index[j], 'Team Name']))  
        # print(printPairing)
        used_j.append(j)
        i += 1
        # print('Used J: ', used_j)
        while i in used_j:
            i += 1
        j = i+1
        while j in used_j:
            j += 1


    previous_pairing = set(printPairing)
    previous_pairings_frozen_set = {frozenset(pair) for pair in previous_pairing}
    previous_pairings.update(previous_pairings_frozen_set)
    
    byeTeam= teams.loc[teams.index[byeTeamIndex-1]]

    return pairing, printPairing, byeTeam

def calculate_winner_probability(rating_difference):
    if rating_difference < 5:
        return 0.5  # Both teams have an equal chance
    elif 5 <= rating_difference <= 10:
        return 0.65  # Team with higher rating wins with 65% probability
    else:
        return 0.9  # Higher-rated team wins with 90% probability

def update_scores(winning_team, losing_team, scoreTable):
    winning_teamName= winning_team['Team Name']
    losing_teamName= losing_team['Team Name']

    scoreTable.loc[scoreTable['TeamName'] == winning_teamName, 'Score'] += 1
    
    scoreTable.loc[scoreTable['TeamName'] == winning_teamName, 'RatingOfPrevOpposingTeam'] = losing_team['Rating']
    scoreTable.loc[scoreTable['TeamName'] == losing_teamName, 'RatingOfPrevOpposingTeam'] = winning_team['Rating']

    return winning_team, losing_team

    
def update_rating(winning_team, losing_team, df):
    
    winning_teamName= winning_team['Team Name']
    losing_teamName= losing_team['Team Name']

    if winning_team['Rating'] < losing_team['Rating']:
        df.loc[df['Team Name'] == winning_teamName, 'Rating'] += 2
        df.loc[df['Team Name'] == losing_teamName, 'Rating']-= 2  
    else:
        df.loc[df['Team Name'] == winning_teamName, 'Rating'] += 5
        df.loc[df['Team Name'] == losing_teamName, 'Rating']-= 5


def results(pairing, df, scoreTable):
    
    for team_a, team_b in pairing:
        
        ratingA = team_a['Rating']+ random.randint(-4, 4)
        ratingB = team_b['Rating']+ random.randint(-4, 4)

        rating_difference = abs(ratingA - ratingB)
        winning_probability = calculate_winner_probability(rating_difference)


        if random.random() < winning_probability:
            winner, loser = update_scores(team_a, team_b, scoreTable)
            update_rating(winner, loser, df)
            print(f"{winner['Team Name']} wins!")
        else:
            winner, loser = update_scores(team_b, team_a, scoreTable)
            update_rating(winner, loser, df)
            print(f"{winner['Team Name']} wins!")

def constraints(df):
    higherRated = df[df['Rating'] > 100]
    lowerRated =  df[df['Rating'] < 50]
    
    for index,team in higherRated.iterrows():
        teamName = team['Team Name']
        df.loc[df['Team Name'] == teamName, 'Rating'] = 100

    for index,team in lowerRated.iterrows():
        teamName = team['Team Name']
        df.loc[df['Team Name'] == teamName, 'Rating'] = 50

def bye_update(team, df, scoreTable):
    teamName = team['Team Name']
    print('Bye Team: ', teamName)
    df.loc[df['Team Name'] == teamName, 'Rating'] += 2
    scoreTable.loc[scoreTable['TeamName'] == teamName, 'Score'] += 1

df = pd.read_csv('data.csv')

data = {'TeamName': [f"A{i:02}" for i in range(1, 51)],
            'Score': [(0) for i in range(50) ],
            'RatingOfPrevOpposingTeam': [(0) for i in range(50) ]
            }

scoreTable = pd.DataFrame(data)

previous_pairings = set()
counter = 0
for i in range(10):
    # constraints(df)
    sorted_df = df.sort_values(by='Rating', ascending=False)
    print(sorted_df)

    cppLanguage = sorted_df.query('`Language of Code` == "C++"')
    pLanguage = sorted_df.query('`Language of Code` == "P"')

    pairingC ,printPairingC, byeTeamC = pairings(cppLanguage, previous_pairings)
    pairingP ,printPairingP, byeTeamP = pairings(pLanguage, previous_pairings)

    paired= printPairingC + printPairingP
    pairing= pairingC + pairingP
    print('Match Pairing: ',paired)

    counter = counter + len(paired)
    # print('Total Matches: ', counter)
    bye_update(byeTeamC, df, scoreTable)
    bye_update(byeTeamP, df, scoreTable)

    results(pairing, df, scoreTable)

    scoreTable = scoreTable.sort_values(by=['Score', 'RatingOfPrevOpposingTeam'], ascending=[False, False])
    print(scoreTable)
    

