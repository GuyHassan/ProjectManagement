import http.client
import json
#this is list with all name of league that include our api - PL(EnglandLeague) ,PD(SpainLeague),PPL(PortugalLeague),DED(NetherlandLeague),
# BL1(GermanyLeague),FL1(FranceLeague),SA(ItalyLeague) .
listOfNameLeauge = ['PL','PD','PPL','DED','BL1','FL1','SA']
response = []
connection = http.client.HTTPConnection('api.football-data.org')
for i in range(len(listOfNameLeauge)):
    headers = { 'X-Auth-Token': '50a1c314b27e45ee8184a31795fab8c1'}
    connection.request('GET','/v2/competitions/'+listOfNameLeauge[i] , None, headers )
    response.append(json.loads(connection.getresponse().read().decode()))
#----------------------------------------------------------------------------------------------------
listOfDataBaseTeams = []
for i in range(len(response)):
    attributeDataBaseTeams = {'Name Country': '', 'Name League': '', 'Winner Of League': '', 'Start Of Season': '',
                         'End Of Season': '', 'Amount Of Match': ''}
    for j in response[i]:
        if(j == 'name'):
            attributeDataBaseTeams['Name League'] = response[i][j]
        elif(j == 'area'):
            attributeDataBaseTeams['Name Country'] = response[i][j]['name']
        elif(j == 'seasons'):
            attributeDataBaseTeams['Amount Of Match'] = response[i][j][1]['currentMatchday']
            attributeDataBaseTeams['Start Of Season'] = response[i][j][1]['startDate']
            attributeDataBaseTeams['End Of Season'] = response[i][j][1]['endDate']
            attributeDataBaseTeams['Winner Of League'] = response[i][j][1]['winner']['name']
    listOfDataBaseTeams.append(attributeDataBaseTeams)

listOfDataBaseTeams = sorted(listOfDataBaseTeams, key = lambda i: i['Amount Of Match']) # we sort by amount of games

print('\n','\t'*9,'List of all the teams who won the league Previous season sorted by number of games\n','\t'*9,'-'*81)
for dictItem in listOfDataBaseTeams:
    for details in dictItem:
        print(details,': ',dictItem[details])
    print('-'*150)
