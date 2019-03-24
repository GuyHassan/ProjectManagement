import unittest
import Feature_Sport_Data
import LocalData
from mock import patch
import re
from datetime import date


class TDD(unittest.TestCase):

    @patch('Feature_Sport_Data.getDataFirstFeature')
    def mockConnectionFirstFeature(self, mock):
        mock.return_value = LocalData.firstFeatureData
        return mock()

    @patch('Feature_Sport_Data.getDataFirstFeature')
    def mockConnectionSecondFeature(self, mock):
        mock.return_value = LocalData.SecondFeatureData
        return mock()

    # --------------------------Tests First Feature------------------------------------------
    @patch('Feature_Sport_Data.getDataFirstFeature')
    def test_WinnerNameNotNone(self, mock):
        listOfData = self.mockConnectionFirstFeature()
        for i in range(len(listOfData)):
            self.assertIsNotNone(listOfData[i]['Winner Of League'])

    @patch('Feature_Sport_Data.getDataFirstFeature')
    def test_StartDateSmallerThanEndDate(self, mock):
        listOfData = self.mockConnectionFirstFeature()
        for i in range(len(listOfData)):
            self.assertLess(listOfData[i]['Start Of Season'], listOfData[i]['End Of Season'])

    @patch('Feature_Sport_Data.getDataFirstFeature')
    def test_AmountOfMatchIsSorted(self, mock):
        listOfData = self.mockConnectionFirstFeature()
        for i in range(len(listOfData)):
            for j in range(i + 1, len(listOfData)):
                self.assertLessEqual(listOfData[i]['Amount Of Match'], listOfData[j]['Amount Of Match'],
                                     'The list is not sorted')

    @patch('Feature_Sport_Data.getDataFirstFeature')
    def test_NameOfCountryIsUnique(self, mock):
        listOfData = self.mockConnectionFirstFeature()
        for i in range(len(listOfData)):
            for j in range(i + 1, len(listOfData)):
                self.assertNotEqual(listOfData[i]['Name Country'], listOfData[j]['Name Country'])

    @patch('Feature_Sport_Data.getDataFirstFeature')
    def test_NumberOfWeeksGreaterOfMatches(self, mock):
        listOfData = self.mockConnectionFirstFeature()
        for i in range(len(listOfData)):
            start = re.findall('\d+', (listOfData[i]['Start Of Season']))
            end = re.findall('\d+', (listOfData[i]['End Of Season']))
            start = date(int(start[0]), int(start[1]), int(start[2]))
            end = date(int(end[0]), int(end[1]), int(end[2]))
            numOfWeeks = (end - start).days // 7
            self.assertGreater(int(numOfWeeks), int(listOfData[i]['Amount Of Match']))

    # --------------------------------Tests Second Feature-----------------------------------------------------------------
    @patch('Feature_Sport_Data.getDataSecondFeature')
    def test_ScorersIsSorted(self, mock):
        listOfData = self.mockConnectionSecondFeature()
        for i in range(len(listOfData)):
            for j in range(i + 1, len(listOfData)):
                self.assertGreaterEqual(listOfData[i]['Players']['Number Of Goals'],
                                        listOfData[j]['Players']['Number Of Goals'], 'The list is not sorted')

    @patch('Feature_Sport_Data.getDataSecondFeature')
    def test_NamePlayerNotNone(self, mock):
        listOfData = self.mockConnectionSecondFeature()
        for i in range(len(listOfData)):
            self.assertIsNotNone(listOfData[i]['Players']['Name Player'])

    @patch('Feature_Sport_Data.getDataSecondFeature')
    def test_NameTeamIsUnique(self, mock):
        listOfData = self.mockConnectionSecondFeature()
        for i in range(len(listOfData)):
            for j in range(i + 1, len(listOfData)):
                self.assertNotEqual(listOfData[i]['Name League'], listOfData[j]['Name League'],
                                    'Cannot be 2 player in same league')

    @patch('Feature_Sport_Data.getDataSecondFeature')
    def test_AgeOfPlayerGeatherThanSixteen(self, mock):
        listOfData = self.mockConnectionSecondFeature()
        for i in range(len(listOfData)):
            for j in range(i + 1, len(listOfData)):
                today = date.today()
                playerDate = re.findall('\d+', (listOfData[i]['Players']['Date Of Birth']))
                self.assertGreater(today.year - int(playerDate[0]), 16)

    @patch('Feature_Sport_Data.getDataSecondFeature')
    def test_NumberOfGoalGreaterThanZero(self,mock):
        listOfData = self.mockConnectionSecondFeature()
        for i in range(len(listOfData)):
            self.assertGreater(int(listOfData[i]['Players']['Number Of Goals']), 0)


if __name__ == '__main__':
    unittest.main()
