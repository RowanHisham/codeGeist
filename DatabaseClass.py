import pyodbc
# from datetime import datetime
#
import NetHolesClass
import TankClass
import UserClass
import WaterQualityClass
# from array import *


class Database:
    def __init__(self):
        self.server = 'mia-robotics.database.windows.net'
        self.database = 'Aquaculture'
        self.username = 'miaRobotics'
        self.password = 'jungleBoogie123'
        self.driver= '{ODBC Driver 17 for SQL Server}'
        self.cnxn = pyodbc.connect('DRIVER='+self.driver+';SERVER='+self.server+';PORT=1433;DATABASE='+self.database+';UID='+self.username+';PWD='+ self.password)
        self.cursor = self.cnxn.cursor()


    #checks if user exists in database and returns user object or return None
    def authenticateLogIn(self, username, password):
        print("AUTHENTICATE LOG IN ------")
        userID = self.searchUser(username,password)
        if(userID == None):
            return None
        else:
            return self.loadUser(userID)

    # #checks if user exists in database and returns user object or return None
    # def authenticatePerson(self, faceID):


    #searches for user in database and if it exists returns its ID
    def searchUser(self, username, password):
        tsql = "SELECT * FROM [User] WHERE username = ? and password = ? ;"
        with self.cursor.execute(tsql,username,password):
            row = self.cursor.fetchone()
            while row:
                print("USER ID = " +  str(row[0]))
                return row[0]
            return None

    # #searches for user in database and if it exists returns its ID [ faceID = result_set[i][6] , userID = result_set[i][0] ]
    # def searchUserFaceID(self, faceID):
    #
    #
    # #not important
    # def validateUsername(self, username):
    #     """
    #     takes username and verifies that it doesn't exist in the database
    #     if it exists returns false and if it doesn't returns true
    #     """
    #
    #
    # "Id = ", row[0]
    # "Username = ", row[1]
    # "Password = ", row[2]
    # "FirstName  = ", row[3]
    # "Lastname = ", row[4]
    # "email = ", row[5]
    # "faceID = ", row[6]
    # "reportLink = ", row[7]
    #loads user data from database and returns user object
    def loadUser(self, userID):
        print("LOADING USER -------")
        tsql = "SELECT * FROM [User] WHERE userID = ?;"
        with self.cursor.execute(tsql, userID):
            row = self.cursor.fetchone()
            while row:
                print("Id = ", row[0])
                print("Username = ", row[1])
                print("Password = ", row[2])
                print("FirstName  = ", row[3])
                print("Lastname = ", row[4])
                print("email = ", row[5])
                print("faceID = ", row[6])
                print("reportLink = ", row[7])
                username = row[1]
                password = row[2]
                firstname = row[3]
                lastname = row[4]
                email = row[5]
                faceID = row[6]
                reportlink = row[7]
                tankList = self.loadTankList(userID)
                user = UserClass.User(firstname,lastname,username,password,email,faceID,reportlink,userID,tankList)
                return user
            return None



    # "feedingSchedule = ", row[1]
    # "userID = ", row[2]
    # "tankID  = ", row[3]
    # "waterSalinityUpperThresh = ", row[4]
    # "waterSalinityLowerThresh = ", row[5]
    # "tempLowerThresh = ", row[6]
    # "tempUpperThresh = ", row[7]
    # "pHLowerThresh = ", row[8]
    # "pHUpperThresh = ", row[9]
    # "harvestDate  = ", row[10]
    # "needsCleaning  = ", row[11]
    # "needsFixing  = ", row[12]
    # load tanks list and returns it
    def loadTankList(self, userID):
        print("LOADING TankList -------")
        tsql = "SELECT * FROM Tanks WHERE userID = ?;"
        with self.cursor.execute(tsql, userID):
            result = self.cursor.fetchall()
            tankList = []
            for row in result:
                print("LOADING TANK --")
                print("fishttype = ", row[0])
                print("feedingSchedule = ", row[1])
                print("userID = ", row[2])
                print("tankID  = ", row[3])
                print("waterSalinityUpperThresh = ", row[4])
                print("waterSalinityLowerThresh = ", row[5])
                print("tempLowerThresh = ", row[6])
                print("tempUpperThresh = ", row[7])
                print("pHLowerThresh = ", row[8])
                print("harvestDate  = ", row[10])
                print("needsCleaning  = ", row[11])
                print("needsFixing  = ", row[12])
                fishtype = row[0]
                feedingSchedule = row[1]
                tankID  = row[3]
                waterSalinityUpperThresh = row[4]
                waterSalinityLowerThresh =  row[5]
                tempLowerThresh =  row[6]
                tempUpperThresh =  row[7]
                pHLowerThresh =  row[8]
                pHUpperThresh =  row[9]
                harvestDate  =  row[10]
                needsCleaning  =  row[11]
                needsFixing  =  row[12]
                wqList = self.loadWaterQualityList(tankID)
                # hList = self.loadNetHolesList(tankID)
                tank = TankClass.Tank(tankID,fishtype,feedingSchedule,waterSalinityUpperThresh,waterSalinityLowerThresh,tempUpperThresh,
                                      tempLowerThresh,pHUpperThresh,pHLowerThresh,harvestDate,needsCleaning,needsFixing,wqList,None)
                tankList.append(tank)

            return tankList

    # "tankID = ", row[0]
    # "time = ", row[1]
    # "date = ", row[2]
    # "pH  = ", row[3]
    # "temp  = ", row[4]
    # "waterQualityLevel = ", row[5]
    # load water quality list and returns it
    def loadWaterQualityList(self, tankID):
        print("LOADING waterQuality -------")
        tsql = "SELECT * FROM Water_Quality WHERE tankID = ?;"
        with self.cursor.execute(tsql, tankID):
            result = self.cursor.fetchall()
            waterQualityList = []

            for row in result:
                print("LOADING WQ --")
                print("tankID = ", row[0])
                print("time = ", row[1])
                print("date = ", row[2])
                print("pH  = ", row[3])
                print("temp  = ", row[4])
                print("waterQualityLevel = ", row[5])
                time =  row[1]
                date = row[2]
                pH  = row[3]
                temp  =  row[4]
                waterQualityLevel = row[5]

                wq = WaterQualityClass.waterQuality(date,time,pH,temp,waterQualityLevel)
                waterQualityList.append(wq)

            return waterQualityList

    # "tankID = ", row[0]
    # "holesCoord = ", row[1]
    # "date = ", row[2]
    # "time  = ", row[3]
    # load net holes list
    def loadNetHolesList(self, tankID):
        print("LOADING netHoles -------")
        tsql = "SELECT * FROM Holes WHERE tankID = ?;"
        with self.cursor.execute(tsql, tankID):
            result = self.cursor.fetchall()
            holesList = []

            for row in result:
                print("tankID = ", row[0])
                print("holesCoord = ", row[1])
                print("date = ", row[2])
                print("time  = ", row[3])
                tankID = row[0]
                holesCoord = row[1]
                date = row[2]
                time  = row[3]

                h = NetHolesClass.netHoles(holesCoord,date,time)
                holesList.append(h)

            return holesList



    # def addFaceID(self, user):
    #     """
    #     takes user object and sets its face ID
    #     """
    #
    # # (userID, fishType, feedingSchedule, waterSalinityUpperThresh,waterSalinityLowerThresh, tempLowerThresh, tempUpperThresh, pHLowerThresh, pHUpperThresh, harvest_date, needsCleaning, needsFixing)
    # #take objects as parameter and adds new entry in database
    # def addNewTank(self, tank, user):
    #
    #
    # #(tankID, time, date, pH, temperature, water_salinity)
    # #take objects as parameter and adds new entry in database
    # def addNewWaterQuality(self, waterQuality, tank):
    #
    #
    # #(tankID,holeCoordinates, date, time)
    # # take objects as parameter and adds new entry in database
    # def addNewNetHoleEntry(self, netHoles,tank):
    #
    #
    #
    # # take objects as parameter and delete entry in database
    # def deleteUser(self, user):
    #
    #
    # # take objects as parameter and delete entry in database
    # def deleteTank(self, tank):
    #
    #
    # def deleteWaterQuality(self, tankID):
    #
    #
    # def deleteNetHole(self, tankID):
    #
    #
    # def deleteAllUserData(self, userID):
    #
    #
    # def printUsers(self):
    #
    #
    # #return 2D array [tanksList,WaterQualityList]
    # def getData(self,username,password):
