import http.client
import json

# this is list with all name of league that include our api - PL(EnglandLeague) ,PD(SpainLeague),PPL(PortugalLeague),DED(NetherlandLeague),
# BL1(GermanyLeague),FL1(FranceLeague),SA(ItalyLeague) .
listOfNameLeauge = ['PL', 'PD', 'PPL', 'DED', 'BL1', 'FL1', 'SA']
response = []
responseScorers = []


def connectionToApiFirstFeature():
    connection = http.client.HTTPConnection('api.football-data.org')
    headers = {'X-Auth-Token': '50a1c314b27e45ee8184a31795fab8c1'}
    for i in range(len(listOfNameLeauge)):
        connection.request('GET', '/v2/competitions/' + listOfNameLeauge[i], None, headers)
        response.append(json.loads(connection.getresponse().read().decode()))


def connectionToApiSecondFeature():
    connection = http.client.HTTPConnection('api.football-data.org')
    headers = {'X-Auth-Token': '276d39f355844de0ba7b1f7aa4474415'}
    for i in range(len(listOfNameLeauge)):
        connection.request('GET', '/v2/competitions/' + listOfNameLeauge[i] + '/scorers', None, headers)
        responseScorers.append(json.loads(connection.getresponse().read().decode()))


def getDataFirstFeature():
    connectionToApiFirstFeature()
    listOfDataBaseTeams = []
    for i in range(len(response)):
        attributeDataBaseTeams = {'Name Country': '', 'Name League': '', 'Winner Of League': '', 'Start Of Season': '',
                                  'End Of Season': '', 'Amount Of Match': ''}
        for j in response[i]:
            if (j == 'name'):
                attributeDataBaseTeams['Name League'] = response[i][j]
            elif (j == 'area'):
                attributeDataBaseTeams['Name Country'] = response[i][j]['name']
            elif (j == 'seasons'):
                attributeDataBaseTeams['Amount Of Match'] = response[i][j][1]['currentMatchday']
                attributeDataBaseTeams['Start Of Season'] = response[i][j][1]['startDate']
                attributeDataBaseTeams['End Of Season'] = response[i][j][1]['endDate']
                attributeDataBaseTeams['Winner Of League'] = response[i][j][1]['winner']['name']
        listOfDataBaseTeams.append(attributeDataBaseTeams)
    return sorted(listOfDataBaseTeams, key=lambda i: i['Amount Of Match'])  # we sort by amount of games


def getDataSecondFeature():
    connectionToApiSecondFeature()
    listOfDataBaseTopPlayer = []
    for i in range(len(responseScorers)):
        attributeDataBaseTopPlayer = {'Name Country': '', 'Name League': '', 'Players': ''}
        for j in responseScorers[i]:
            if (j == 'competition'):
                attributeDataBaseTopPlayer['Name League'] = responseScorers[i][j]['name']
                attributeDataBaseTopPlayer['Name Country'] = responseScorers[i][j]['area']['name']
            if (j == 'scorers'):
                PlayerDetails = {'Name Player': '', 'Position': '', 'Number Of Goals': '', 'Team He Play': '',
                                 'Date Of Birth': '', 'Country Of Birth': ''}
                PlayerDetails['Name Player'] = responseScorers[i][j][0]['player']['name']
                PlayerDetails['Position'] = responseScorers[i][j][0]['player']['position']
                PlayerDetails['Date Of Birth'] = responseScorers[i][j][0]['player']['dateOfBirth']
                PlayerDetails['Country Of Birth'] = responseScorers[i][j][0]['player']['countryOfBirth']
                PlayerDetails['Number Of Goals'] = responseScorers[i][j][0]['numberOfGoals']
                PlayerDetails['Team He Play'] = responseScorers[i][j][0]['team']['name']
                attributeDataBaseTopPlayer['Players'] = PlayerDetails
        listOfDataBaseTopPlayer.append(attributeDataBaseTopPlayer)
    listOfDataBaseTopPlayer = sorted(listOfDataBaseTopPlayer, key=lambda i: i['Players']['Number Of Goals'])
    listOfDataBaseTopPlayer = list(reversed(listOfDataBaseTopPlayer))
    return listOfDataBaseTopPlayer

# connectionToApiFirstFeature()
# listOfDataBaseTeams = getDataFirstFeature()
# connectionToApiSecondFeature()
# listOfDataBaseTopPlayer = getDataSecondFeature()

# print('\n', '\t' * 9, 'List of all the teams who won the league Previous season sorted by number of games\n', '\t' * 9,
#       '-' * 81)
# for dictItem in listOfDataBaseTeams:
#     for details in dictItem:
#         print("'",details,"'", ': ',"'",dictItem[details],"',")
#     print('-' * 150)
# print('\n','\t'*9,'List of 10 players most goals in a diffrent league sorted by number of goals\n','\t'*9,'-'*81)
# for dictItem in listOfDataBaseTopPlayer:
#     for details in dictItem:
#         if (details == 'Players'):
#                 for j in dictItem['Players']:
#                     print("'",j,"'",': ',"'",dictItem['Players'][j],"',")
#         else:
#             print("'",details,"'",': ',"'",dictItem[details],"',")
#     print('*'*150)
