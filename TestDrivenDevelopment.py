import unittest
import Feature_Sport_Data
import LocalData
from mock import patch


class TDD(unittest.TestCase):
    @patch('Feature_Sport_Data.getDataFirstFeature')
    # --------------------------Tests First Feature------------------------------------------
    def test_WinnerNameNotNone(self,mock):
        mock.return_value = LocalData.firstFeatureData
        listOfData = mock()
        for i in range(len(listOfData)):
            self.assertIsNotNone(listOfData[i]['Winner Of League'])

    def test_StartDateSmallerThanEndDate(self,mock):
        mock.return_value = LocalData.firstFeatureData
        listOfData = mock()
        for i in range(len(listOfData)):
            self.assertLess(listOfData[i]['Start Of Season'], listOfData[i]['End Of Season'])

    def test_AmountOfMatchIsSorted(self,mock):
        mock.return_value = LocalData.firstFeatureData
        listOfData = mock()
        for i in range(len(listOfData)):
            for j in range(i + 1, len(listOfData)):
                self.assertLessEqual(listOfData[i]['Amount Of Match'], listOfData[j]['Amount Of Match'],
                                     'The list is not sorted')

    def test_NameOfCountryIsUnique(self,mock):
        mock.return_value = LocalData.firstFeatureData
        listOfData = mock()
        for i in range(len(listOfData)):
            for j in range(i + 1, len(listOfData)):
                self.assertNotEqual(listOfData[i]['Name Country'], listOfData[j]['Name Country'])

    # --------------------------------Tests Second Feature-----------------------------------------------------------------
    def test_ScorersIsSorted(self,mock):
        listOfData = Feature_Sport_Data.getDataSecondFeature()
        for i in range(len(listOfData)):
            for j in range(i + 1, len(listOfData)):
                self.assertGreaterEqual(listOfData[i]['Players']['Number Of Goals'],
                                        listOfData[j]['Players']['Number Of Goals'], 'The list is not sorted')

    def test_NamePlayerNotNone(self,mock):
        listOfData = Feature_Sport_Data.getDataSecondFeature()
        for i in range(len(listOfData)):
            self.assertIsNotNone(listOfData[i]['Players']['Name Player'])

    def test_NameTeamIsUnique(self,mock):
        listOfData = Feature_Sport_Data.getDataSecondFeature()
        for i in range(len(listOfData)):
            for j in range(i + 1, len(listOfData)):
                self.assertNotEqual(listOfData[i]['Name League'], listOfData[j]['Name League'],
                                    'Cannot be 2 player in same league')
    def test_AgeOfPlayerGeatherThanSixteen(self,mock):
        mock.return_value = LocalData.firstFeatureData
        listOfData = mock()
        for i in range(len(listOfData)):
            for j in range(i+1,len(listOfData)):
                self.assertGreaterEqual(listOfData[i]['Players']['Date'])
        

if __name__ == '__main__':
    unittest.main()
