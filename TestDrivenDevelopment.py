import unittest
import Feature_Sport_Data
import LocalData
from mock import patch
import re
from datetime import date


class TDD(unittest.TestCase):

    @patch('Feature_Sport_Data.getDataFirstFeature')
    # --------------------------Tests First Feature------------------------------------------
    def test_WinnerNameNotNone(self, mock):
        mock.return_value = LocalData.firstFeatureData
        listOfData = mock()
        print(listOfData)
        for i in range(len(listOfData)):
            self.assertIsNotNone(listOfData[i]['Winner Of League'])

    def test_StartDateSmallerThanEndDate(self):
        listOfData = Feature_Sport_Data.getDataFirstFeature()
        for i in range(len(listOfData)):
            self.assertLess(listOfData[i]['Start Of Season'], listOfData[i]['End Of Season'])

    def test_AmountOfMatchIsSorted(self):
        listOfData = Feature_Sport_Data.getDataFirstFeature()
        for i in range(len(listOfData)):
            for j in range(i + 1, len(listOfData)):
                if (listOfData[i]['Amount Of Match'] > listOfData[j]['Amount Of Match']):
                    self.assertGreater(listOfData[i]['Amount Of Match'], listOfData[j]['Amount Of Match'],
                                       'The list is not sorted')

    def test_NameOfCountryIsUnique(self):
        listOfData = Feature_Sport_Data.getDataFirstFeature()
        for i in range(len(listOfData)):
            for j in range(i + 1, len(listOfData)):
                if (listOfData[i]['Name Country'] == listOfData[j]['Name Country']):
                    self.assertEqual(listOfData[i]['Name Country'], listOfData[j]['Name Country'])

    @patch('Feature_Sport_Data.getDataFirstFeature')
    def test_NumberOfWeeksGreaterOfMatches(self, mock):
        mock.return_value = LocalData.firstFeatureData
        listOfData = mock()
        for i in range(len(listOfData)):
            start = re.findall('\d+', (listOfData[i]['Start Of Season']))
            end = re.findall('\d+', (listOfData[i]['End Of Season']))
            start = date(int(start[0]), int(start[1]), int(start[2]))
            end = date(int(end[0]), int(end[1]), int(end[2]))
            numOfWeeks = (end - start).days // 7
            self.assertGreater(int(numOfWeeks), int(listOfData[i]['Amount Of Match']))

    # --------------------------------Tests Second Feature-----------------------------------------------------------------
    def test_ScorersIsSorted(self):
        listOfData = Feature_Sport_Data.getDataSecondFeature()
        for i in range(len(listOfData)):
            for j in range(i + 1, len(listOfData)):
                if (listOfData[i]['Players']['Number Of Goals'] < listOfData[j]['Players']['Number Of Goals']):
                    self.assertGreater(listOfData[j]['Players']['Number Of Goals'],
                                       listOfData[i]['Players']['Number Of Goals'], 'The list is not sorted')

    def test_NamePlayerNotNone(self):
        listOfData = Feature_Sport_Data.getDataSecondFeature()
        for i in range(len(listOfData)):
            self.assertIsNotNone(listOfData[i]['Players']['Name Player'])

    def test_NameTeamIsUnique(self):
        listOfData = Feature_Sport_Data.getDataSecondFeature()
        for i in range(len(listOfData)):
            for j in range(i + 1, len(listOfData)):
                self.assertNotEqual(listOfData[i]['Name League'], listOfData[j]['Name League'],
                                    'Cannot be 2 player in same league')


if __name__ == '__main__':
    unittest.main()
