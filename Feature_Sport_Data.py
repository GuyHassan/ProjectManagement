"""
Student 1 : Guy Hassan
ID 1:307845032
Student 2 : Yahav Mizrahi
ID 2: 305759185
Student 3 : Yinon Hirari
ID 3 : 203409024
"""
import http.client
import json

# this is list with all name of league that include our api
# - PL(EnglandLeague) ,PD(SpainLeague),PPL(PortugalLeague),DED(NetherlandLeague),
# BL1(GermanyLeague),FL1(FranceLeague),SA(ItalyLeague) .
list_of_name_leauge = ['PL', 'PD', 'PPL', 'DED', 'BL1', 'FL1', 'SA']
response = []
responseScorers = []


def connection_to_api_first_feature():
    """
    connection to our api and get the first request and append to response the data
    """
    connection = http.client.HTTPConnection('api.football-data.org')
    headers = {'X-Auth-Token': '50a1c314b27e45ee8184a31795fab8c1'}
    for i in range(len(list_of_name_leauge)):
        connection.request('GET', '/v2/competitions/' + list_of_name_leauge[i], None, headers)
        response.append(json.loads(connection.getresponse().read().decode()))


def connection_to_api_second_feature():
    """
    connection to our api and get the second request and append to responseScorers the data
    """
    connection = http.client.HTTPConnection('api.football-data.org')
    headers = {'X-Auth-Token': '276d39f355844de0ba7b1f7aa4474415'}
    for i in range(len(list_of_name_leauge)):
        connection.request('GET', '/v2/competitions/' + list_of_name_leauge[i] + '/scorers', None, headers)
        responseScorers.append(json.loads(connection.getresponse().read().decode()))


def get_data_first_feature():
    """
        this function create the first feature , he call to football api , and we arrange it to modify to our feature
        this feature is : give us the top league of each league and sort this for us by amount of games
        :return: dict with all our feature
        """
    connection_to_api_first_feature()
    list_of_data_base_teams = []
    for i in range(len(response)):
        attribute_data_base_teams = {'Name Country': '', 'Name League': '', 'Winner Of League': '',
                                     'Start Of Season': '',
                                     'End Of Season': '', 'Amount Of Match': ''}
        for j in response[i]:
            if (j == 'name'):
                attribute_data_base_teams['Name League'] = response[i][j]
            elif (j == 'area'):
                attribute_data_base_teams['Name Country'] = response[i][j]['name']
            elif (j == 'seasons'):
                attribute_data_base_teams['Amount Of Match'] = response[i][j][1]['currentMatchday']
                attribute_data_base_teams['Start Of Season'] = response[i][j][1]['startDate']
                attribute_data_base_teams['End Of Season'] = response[i][j][1]['endDate']
                attribute_data_base_teams['Winner Of League'] = response[i][j][1]['winner']['name']
        list_of_data_base_teams.append(attribute_data_base_teams)
    return sorted(list_of_data_base_teams, key=lambda i: i['Amount Of Match'])  # we sort by amount of games


def get_data_second_feature():
    """
    this function create the second feature , he call to football api , and we arrange it to modify to our feature
    this feature is : give us the top scorers sorting by amount goals
    :return: dict with all our feature
    """
    connection_to_api_second_feature()
    list_of_data_base_top_player = []
    for i in range(len(responseScorers)):
        attribute_data_base_top_player = {'Name Country': '', 'Name League': '', 'Players': ''}
        for j in responseScorers[i]:
            if (j == 'competition'):
                attribute_data_base_top_player['Name League'] = responseScorers[i][j]['name']
                attribute_data_base_top_player['Name Country'] = responseScorers[i][j]['area']['name']
            if (j == 'scorers'):
                player_details = {'Name Player': '', 'Position': '', 'Number Of Goals': '', 'Team He Play': '',
                                  'Date Of Birth': '', 'Country Of Birth': ''}
                player_details['Name Player'] = responseScorers[i][j][0]['player']['name']
                player_details['Position'] = responseScorers[i][j][0]['player']['position']
                player_details['Date Of Birth'] = responseScorers[i][j][0]['player']['dateOfBirth']
                player_details['Country Of Birth'] = responseScorers[i][j][0]['player']['countryOfBirth']
                player_details['Number Of Goals'] = responseScorers[i][j][0]['numberOfGoals']
                player_details['Team He Play'] = responseScorers[i][j][0]['team']['name']
                attribute_data_base_top_player['Players'] = player_details
        list_of_data_base_top_player.append(attribute_data_base_top_player)
    list_of_data_base_top_player = sorted(list_of_data_base_top_player, key=lambda i: i['Players']['Number Of Goals'])
    list_of_data_base_top_player = list(reversed(list_of_data_base_top_player))
    return list_of_data_base_top_player


list_of_data_base_teams = get_data_first_feature()
list_of_data_base_top_player = get_data_second_feature()

print('\n', '\t' * 2,
      'First Feature : List of all the teams who won the league Previous season sorted by number of games\n', '\t' * 2,
      '-' * 95)
for dictItem in list_of_data_base_teams:
    for details in dictItem:
        print("'", details, "'", ': ', "'", dictItem[details], "',")
    print('-' * 150)

print('\n', '\t' * 2, 'Second Feature : List of 10 players most goals in a diffrent league sorted by number of goals\n',
      '\t' * 2, '-' * 95)
for dictItem in list_of_data_base_top_player:
    for details in dictItem:
        if (details == 'Players'):
            for j in dictItem['Players']:
                print("'", j, "'", ': ', "'", dictItem['Players'][j], "',")
        else:
            print("'", details, "'", ': ', "'", dictItem[details], "',")
    print('*' * 150)
