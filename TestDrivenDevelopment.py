import unittest
import Feature_Sport_Data
import LocalData
from mock import patch
import re
from datetime import date


class TDD(unittest.TestCase):
    @patch('Feature_Sport_Data.get_data_first_feature')
    def mockConnectionFirstFeature(self, mock):
        mock.return_value = LocalData.first_feature_data
        return mock()

    @patch('Feature_Sport_Data.get_data_second_feature')
    def mockConnectionSecondFeature(self, mock):
        mock.return_value = LocalData.second_feature_data
        return mock()

    # --------------------------Tests First Feature------------------------------------------
    @patch('Feature_Sport_Data.get_data_first_feature')
    def test_WinnerNameNotNone(self, mock):
        listofdata = self.mockConnectionFirstFeature()
        for i in range(len(listofdata)):
            self.assertIsNotNone(listofdata[i]['Winner Of League'])

    @patch('Feature_Sport_Data.get_data_first_feature')
    def test_StartDateSmallerThanEndDate(self, mock):
        listofdata = self.mockConnectionFirstFeature()
        for i in range(len(listofdata)):
            self.assertLess(listofdata[i]['Start Of Season'], listofdata[i]['End Of Season'])

    @patch('Feature_Sport_Data.get_data_first_feature')
    def test_AmountOfMatchIsSorted(self, mock):
        listofdata = self.mockConnectionFirstFeature()
        for i in range(len(listofdata)):
            for j in range(i + 1, len(listofdata)):
                self.assertLessEqual(listofdata[i]['Amount Of Match'], listofdata[j]['Amount Of Match'],
                                     'The list is not sorted')

    @patch('Feature_Sport_Data.get_data_first_feature')
    def test_NameOfCountryIsUnique(self, mock):
        listofdata = self.mockConnectionFirstFeature()
        for i in range(len(listofdata)):
            for j in range(i + 1, len(listofdata)):
                self.assertNotEqual(listofdata[i]['Name Country'], listofdata[j]['Name Country'])

    @patch('Feature_Sport_Data.get_data_first_feature')
    def test_NumberOfWeeksGreaterOfMatches(self, mock):
        listofdata = self.mockConnectionFirstFeature()
        for i in range(len(listofdata)):
            start = re.findall('\d+', (listofdata[i]['Start Of Season']))
            end = re.findall('\d+', (listofdata[i]['End Of Season']))
            start = date(int(start[0]), int(start[1]), int(start[2]))
            end = date(int(end[0]), int(end[1]), int(end[2]))
            num_of_weeks = (end - start).days // 7
            self.assertGreater(int(num_of_weeks), int(listofdata[i]['Amount Of Match']))

    # --------------------------------Tests Second Feature-----------------------------------------------------------------
    @patch('Feature_Sport_Data.get_data_second_feature')
    def test_ScorersIsSorted(self, mock):
        listofdata = self.mockConnectionSecondFeature()
        for i in range(len(listofdata)):
            for j in range(i + 1, len(listofdata)):
                self.assertGreaterEqual(listofdata[i]['Players']['Number Of Goals'],
                                        listofdata[j]['Players']['Number Of Goals'], 'The list is not sorted')

    @patch('Feature_Sport_Data.get_data_second_feature')
    def test_NamePlayerNotNone(self, mock):
        listofdata = self.mockConnectionSecondFeature()
        for i in range(len(listofdata)):
            self.assertIsNotNone(listofdata[i]['Players']['Name Player'])

    @patch('Feature_Sport_Data.get_data_second_feature')
    def test_NameTeamIsUnique(self, mock):
        listofdata = self.mockConnectionSecondFeature()
        for i in range(len(listofdata)):
            for j in range(i + 1, len(listofdata)):
                self.assertNotEqual(listofdata[i]['Name League'], listofdata[j]['Name League'],
                                    'Cannot be 2 player in same league')

    @patch('Feature_Sport_Data.get_data_second_feature')
    def test_AgeOfPlayerGeatherThanSixteen(self, mock):
        listofdata = self.mockConnectionSecondFeature()
        for i in range(len(listofdata)):
            for j in range(i + 1, len(listofdata)):
                today = date.today()
                playerDate = re.findall('\d+', (listofdata[i]['Players']['Date Of Birth']))
                self.assertGreater(today.year - int(playerDate[0]), 16)

    @patch('Feature_Sport_Data.get_data_second_feature')
    def test_NumberOfGoalGreaterThanZero(self, mock):
        listofdata = self.mockConnectionSecondFeature()
        for i in range(len(listofdata)):
            self.assertGreater(int(listofdata[i]['Players']['Number Of Goals']), 0)


if __name__ == '__main__':
    unittest.main()
