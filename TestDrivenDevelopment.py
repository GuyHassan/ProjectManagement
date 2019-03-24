import unittest
import Feature_Sport_Data


class TDD(unittest.TestCase):
    # --------------------------Tests First Feature------------------------------------------
    def test_WinnerNameNotNone(self):
        listOfData = Feature_Sport_Data.getDataFirstFeature()
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
