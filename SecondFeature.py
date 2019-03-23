import http.client
import json
listOfNameLeauge = ['PL', 'PD', 'PPL', 'DED', 'BL1', 'FL1', 'SA']
responseScorers = []
def connectionToApi():
    connection = http.client.HTTPConnection('api.football-data.org')
    headers = {'X-Auth-Token': '50a1c314b27e45ee8184a31795fab8c1'}
    for i in range(len(listOfNameLeauge)):
        connection.request('GET', '/v2/competitions/' + listOfNameLeauge[i] + '/scorers', None, headers)
        responseScorers.append(json.loads(connection.getresponse().read().decode()))

connectionToApi()
listOfDataBaseTopPlayer = []
for i in range(len(responseScorers)):
    attributeDataBaseTopPlayer = {'Name Country':'','Name League':'','Players':''}
    for j in responseScorers[i]:
        if(j == 'competition'):
            attributeDataBaseTopPlayer['Name League'] = responseScorers[i][j]['name']
            attributeDataBaseTopPlayer['Name Country'] = responseScorers[i][j]['area']['name']
        if(j == 'scorers'):
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

listOfDataBaseTopPlayer = sorted(listOfDataBaseTopPlayer,key = lambda i : i['Players']['Number Of Goals'])
listOfDataBaseTopPlayer = reversed(listOfDataBaseTopPlayer)
print('\n','\t'*9,'List of 10 players most goals in a diffrent league sorted by number of goals\n','\t'*9,'-'*81)
for dictItem in listOfDataBaseTopPlayer:
    for details in dictItem:
        if (details == 'Players'):
                for j in dictItem['Players']:
                    print(j,': ',dictItem['Players'][j])
        else:
            print(details,': ',dictItem[details])
    print('*'*150)