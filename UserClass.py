import TankClass


class User:
    # userTankList: TankClass

    def __init__(self, firstName, lastName ,username, password, email, faceID,reportLink, userID, userTankList):
        self.firstName = firstName
        self.lastName = lastName
        self.username = username
        self.password = password
        self.userID = userID
        self.userTankList = userTankList
        self.email = email
        self.faceID = faceID
        self.reportLink = reportLink

    def getUsername(self):

    def getPassword(self):

    def getFirstName(self):
        '''a function that returns user's first name'''

    def getLastName(self):
        '''a function that returns user's last name'''

    def getUserID(self):
        '''a function that returns user ID'''

    def getEmail(self):

    def setFaceID(self, faceID):
        '''a function that sets face ID'''

    def setReportLink(self, reportLink):
        '''a function that sets report link'''

    def getFaceID(self):
        '''a function that returns face ID'''

    def getReportLink(self):


    def creatTank(self, tankID, typeOfFish,feedingSchedule, waterSalinityUpperThresh,waterSalinityLowerThresh, tempUpperThresh, tempLowerThresh,
                 pHUpperThresh,pHLowerThresh,harvestDate,needsCleaning,needsFixing, waterQualityHistory):
        '''a function that appends a tank object to the user's tanks list
        and returns this newly created object'''


    def getTankList(self):
        '''a function that returns a list of the user's tanks'''

    def removeTank(self, tankID):
        '''a function that checks if the tank id exists and removes it
        returns 0 when the tank removal is successfull
        returns 1 when the tank doesn't exist'''


    def getWaterQualityHistory(self):
        '''a function that returns a full list of
        all the user's tanks' water quality entries'''

