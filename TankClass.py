import WaterQualityClass
from WaterQualityClass import waterQuality
import datetime
class Tank:
    def __init__(self, tankID, typeOfFish,feedingSchedule, waterSalinityUpperThresh,waterSalinityLowerThresh, tempUpperThresh, tempLowerThresh,
                 pHUpperThresh,pHLowerThresh,harvestDate,needsCleaning,needsFixing, waterQualityHistory, holesList):
        self.tankID = tankID
        self.typeOfFish = typeOfFish
        self.feedingSchedule = feedingSchedule
        self.waterSalinityUpperThresh = waterSalinityUpperThresh
        self.waterSalinityLowerThresh = waterSalinityLowerThresh
        self.tempUpperThresh = tempUpperThresh
        self.tempLowerThresh = tempLowerThresh
        self.pHUpperThresh = pHUpperThresh
        self.pHLowerThresh = pHLowerThresh
        self.harvestDate = harvestDate
        self.needsCleaning = needsCleaning
        self.needsFixing = needsFixing
        self.waterQualityHistory = waterQualityHistory
        self.holesList = holesList

    def getTankID(self):
        '''a function that returns tank ID'''
        return self.tankID


    def getFishType(self):

    def getHarvestDate(self):

    def getFeedingSchedule(self):

    def getPipeState(self):

    def getFishnetState(self):

    def getWaterQualityHistory(self):

    def getNetHolesList(self):

    def checkWaterSalinity(self, waterSalinity):
        '''a function that returns true if the water salinity level is within the specified thresholds'''


    def checkTemp(self, temp):
        '''a function that returns true if the temperature is within the specified threshold'''


    def checkpH(self, pH):
        '''a function that returns true if the pH is within the specified threshold'''


    def addWaterQualityEntry(self, date, pH, temperature,waterSalinity):
        '''a function that add an entry to getting water quality and appends it to the history list'''


    def getWaterQualityHistory(self):
        '''a function that returns the water quality entries history list'''
