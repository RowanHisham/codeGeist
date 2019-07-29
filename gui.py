# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import resources
from DatabaseClass import Database
# from sensors import Sensors
import webbrowser
from CameraClass import Camera
import cv2
from NetHoleInspection import NetHoleDetection
from NetCleaningInspection import  NetCleaning
from notify import  emailNotifier
from sensors import Sensors

class Ui_MainWindow(object):
    db = Database()
    cam = Camera(0)
    camTimer = QtCore.QTimer()
    cam.setDaemon(True)
    holes = NetHoleDetection()
    clean = NetCleaning()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1002, 872)
        MainWindow.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setFixedSize(1002, 872)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1000, 873))
        self.stackedWidget.setObjectName("stackedWidget")
        self.loginPage = QtWidgets.QWidget()
        self.loginPage.setStyleSheet("border-image: url(:/Images/Resources/signInBG.png);")
        self.loginPage.setObjectName("loginPage")
        self.button_signIn_signIn = QtWidgets.QPushButton(self.loginPage)
        self.button_signIn_signIn.setGeometry(QtCore.QRect(320, 590, 320, 45))
        self.button_signIn_signIn.setStyleSheet("border-image: url(:/Images/Resources/signIn.png);")
        self.button_signIn_signIn.setText("")
        self.button_signIn_signIn.setObjectName("button_signIn_signIn")
        self.button_faceID_signIn = QtWidgets.QPushButton(self.loginPage)
        self.button_faceID_signIn.setGeometry(QtCore.QRect(320, 660, 320, 45))
        self.button_faceID_signIn.setStyleSheet("border-image: url(:/Images/Resources/faceID.png);\n"
"")
        self.button_faceID_signIn.setText("")
        self.button_faceID_signIn.setObjectName("button_faceID_signIn")
        self.button_signUp_signIn = QtWidgets.QPushButton(self.loginPage)
        self.button_signUp_signIn.setGeometry(QtCore.QRect(320, 730, 320, 45))
        self.button_signUp_signIn.setStyleSheet("border-image: url(:/Images/Resources/signUp.png);")
        self.button_signUp_signIn.setText("")
        self.button_signUp_signIn.setObjectName("button_signUp_signIn")
        self.lineEdit_username_signIn = QtWidgets.QLineEdit(self.loginPage)
        self.lineEdit_username_signIn.setGeometry(QtCore.QRect(300, 351, 381, 31))
        self.lineEdit_username_signIn.setStyleSheet("border-image: url(:/Images/Resources/darkBlackBG.png);\n"
"color: rgb(255, 255, 255);")
        self.lineEdit_username_signIn.setObjectName("lineEdit_username_signIn")
        self.lineEdit_password_signIn = QtWidgets.QLineEdit(self.loginPage)
        self.lineEdit_password_signIn.setGeometry(QtCore.QRect(300, 421, 381, 41))
        self.lineEdit_password_signIn.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lineEdit_password_signIn.setStyleSheet("border-image: url(:/Images/Resources/darkBlackBG.png);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.lineEdit_password_signIn.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password_signIn.setObjectName("lineEdit_password_signIn")
        self.stackedWidget.addWidget(self.loginPage)
        self.signupPage = QtWidgets.QWidget()
        self.signupPage.setStyleSheet("border-image: url(:/Images/Resources/signUpBG.png);")
        self.signupPage.setObjectName("signupPage")
        self.lineEdit_firstName_signUp = QtWidgets.QLineEdit(self.signupPage)
        self.lineEdit_firstName_signUp.setGeometry(QtCore.QRect(300, 330, 151, 29))
        self.lineEdit_firstName_signUp.setStyleSheet("border-image: url(:/Images/Resources/darkBlackBG.png);\n"
"color: rgb(255, 255, 255);")
        self.lineEdit_firstName_signUp.setObjectName("lineEdit_firstName_signUp")
        self.lineEdit_lastName_signUp = QtWidgets.QLineEdit(self.signupPage)
        self.lineEdit_lastName_signUp.setGeometry(QtCore.QRect(520, 330, 151, 29))
        self.lineEdit_lastName_signUp.setStyleSheet("border-image: url(:/Images/Resources/darkBlackBG.png);\n"
"color: rgb(255, 255, 255);")
        self.lineEdit_lastName_signUp.setObjectName("lineEdit_lastName_signUp")
        self.lineEdit_email_signUp = QtWidgets.QLineEdit(self.signupPage)
        self.lineEdit_email_signUp.setGeometry(QtCore.QRect(300, 400, 371, 21))
        self.lineEdit_email_signUp.setStyleSheet("border-image: url(:/Images/Resources/darkBlackBG.png);\n"
"color: rgb(255, 255, 255);")
        self.lineEdit_email_signUp.setObjectName("lineEdit_email_signUp")
        self.lineEdit_username_signUp = QtWidgets.QLineEdit(self.signupPage)
        self.lineEdit_username_signUp.setGeometry(QtCore.QRect(300, 480, 371, 21))
        self.lineEdit_username_signUp.setStyleSheet("border-image: url(:/Images/Resources/darkBlackBG.png);\n"
"color: rgb(255, 255, 255);")
        self.lineEdit_username_signUp.setObjectName("lineEdit_username_signUp")
        self.lineEdit_password_signUp = QtWidgets.QLineEdit(self.signupPage)
        self.lineEdit_password_signUp.setGeometry(QtCore.QRect(300, 560, 371, 21))
        self.lineEdit_password_signUp.setStyleSheet("\n"
"border-image: url(:/Images/Resources/darkBlackBG.png);\n"
"color: rgb(255, 255, 255);")
        self.lineEdit_password_signUp.setObjectName("lineEdit_password_signUp")
        self.button_signUp_signUp = QtWidgets.QPushButton(self.signupPage)
        self.button_signUp_signUp.setGeometry(QtCore.QRect(340, 640, 320, 45))
        self.button_signUp_signUp.setStyleSheet("border-image: url(:/Images/Resources/signUp.png);")
        self.button_signUp_signUp.setText("")
        self.button_signUp_signUp.setObjectName("button_signUp_signUp")
        self.button_backToSignIn = QtWidgets.QPushButton(self.signupPage)
        self.button_backToSignIn.setGeometry(QtCore.QRect(340, 720, 320, 45))
        self.button_backToSignIn.setStyleSheet("border-image: url(:/Images/Resources/backSignInPressed.png);")
        self.button_backToSignIn.setText("")
        self.button_backToSignIn.setObjectName("button_backToSignIn")
        self.stackedWidget.addWidget(self.signupPage)
        self.faceidPage = QtWidgets.QWidget()
        self.faceidPage.setStyleSheet("border-image: url(:/Images/Resources/faceIDWidget.png);")
        self.faceidPage.setObjectName("faceidPage")
        self.label_cam = QtWidgets.QLabel(self.faceidPage)
        self.label_cam.setGeometry(QtCore.QRect(90, 230, 821, 401))
        self.label_cam.setStyleSheet("border-image: url(:/Images/Resources/semiDarkBG.png);")
        self.label_cam.setText("")
        self.label_cam.setObjectName("label_cam")
        self.stackedWidget.addWidget(self.faceidPage)
        self.mainPage = QtWidgets.QWidget()
        self.mainPage.setStyleSheet("border-image: url(:/Images/Resources/mainWidgetBG.png);")
        self.mainPage.setObjectName("mainPage")
        self.button_dashboard = QtWidgets.QPushButton(self.mainPage)
        self.button_dashboard.setGeometry(QtCore.QRect(0, 200, 291, 54))
        self.button_dashboard.setStyleSheet("QPushButton{\n"
"    border-image: url(:/Images/Resources/dasboard.png);\n"
"background-repeat: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border-image: url(:/Images/Resources/dashboardPressed.png);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    border-image: url(:/Images/Resources/dashboardPressed.png);\n"
"}")
        self.button_dashboard.setText("")
        self.button_dashboard.setObjectName("button_dashboard")
        self.button_createTank = QtWidgets.QPushButton(self.mainPage)
        self.button_createTank.setGeometry(QtCore.QRect(0, 280, 291, 54))
        self.button_createTank.setStyleSheet("QPushButton{\n"
"    border-image: url(:/Images/Resources/create.png);\n"
"background-repeat: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border-image: url(:/Images/Resources/createPressed.png);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    border-image: url(:/Images/Resources/createPressed.png);\n"
"}")
        self.button_createTank.setText("")
        self.button_createTank.setObjectName("button_createTank")
        self.button_analyzeTank = QtWidgets.QPushButton(self.mainPage)
        self.button_analyzeTank.setGeometry(QtCore.QRect(0, 350, 291, 54))
        self.button_analyzeTank.setStyleSheet("QPushButton{\n"
"    border-image: url(:/Images/Resources/analyze.png);\n"
"background-repeat: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border-image: url(:/Images/Resources/analyzePressed.png);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    border-image: url(:/Images/Resources/analyzePressed.png);\n"
"}")
        self.button_analyzeTank.setText("")
        self.button_analyzeTank.setObjectName("button_analyzeTank")
        self.button_settings = QtWidgets.QPushButton(self.mainPage)
        self.button_settings.setGeometry(QtCore.QRect(0, 420, 291, 54))
        self.button_settings.setStyleSheet("QPushButton{\n"
"    border-image: url(:/Images/Resources/settings.png);\n"
"background-repeat: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border-image: url(:/Images/Resources/settingsPressed.png);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    border-image: url(:/Images/Resources/settingsPressed.png);\n"
"}")
        self.button_settings.setText("")
        self.button_settings.setObjectName("button_settings")
        self.button_logout = QtWidgets.QPushButton(self.mainPage)
        self.button_logout.setGeometry(QtCore.QRect(78, 810, 130, 42))
        self.button_logout.setStyleSheet("QPushButton{\n"
"    border-image: url(:/Images/Resources/logoutPressed.png);\n"
"background-repeat: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border-image: url(:/Images/Resources/logout.png);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    border-image: url(:/Images/Resources/logout.png);\n"
"}")
        self.button_logout.setText("")
        self.button_logout.setObjectName("button_logout")
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.mainPage)
        self.stackedWidget_2.setGeometry(QtCore.QRect(290, 0, 711, 861))
        self.stackedWidget_2.setStyleSheet("border-image: url(:/Images/Resources/CreateBG.png);")
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.dashboardPage = QtWidgets.QWidget()
        self.dashboardPage.setStyleSheet("border-image: url(:/Images/Resources/dashboardWidget.png);")
        self.dashboardPage.setObjectName("dashboardPage")
        self.label_fishType_tankData = QtWidgets.QLabel(self.dashboardPage)
        self.label_fishType_tankData.setGeometry(QtCore.QRect(190, 180, 55, 16))
        self.label_fishType_tankData.setStyleSheet("border-image: url(:/Images/Resources/whiteBG.png);")
        self.label_fishType_tankData.setObjectName("label_fishType_tankData")
        self.label_harvestDate_tankData = QtWidgets.QLabel(self.dashboardPage)
        self.label_harvestDate_tankData.setGeometry(QtCore.QRect(220, 230, 71, 16))
        self.label_harvestDate_tankData.setStyleSheet("border-image: url(:/Images/Resources/whiteBG.png);")
        self.label_harvestDate_tankData.setObjectName("label_harvestDate_tankData")
        self.label_feeding_tankData = QtWidgets.QLabel(self.dashboardPage)
        self.label_feeding_tankData.setGeometry(QtCore.QRect(250, 270, 71, 16))
        self.label_feeding_tankData.setStyleSheet("border-image: url(:/Images/Resources/whiteBG.png);")
        self.label_feeding_tankData.setObjectName("label_feeding_tankData")
        self.label_ph_tankData = QtWidgets.QLabel(self.dashboardPage)
        self.label_ph_tankData.setGeometry(QtCore.QRect(140, 330, 55, 16))
        self.label_ph_tankData.setStyleSheet("border-image: url(:/Images/Resources/whiteBG.png);")
        self.label_ph_tankData.setObjectName("label_ph_tankData")
        self.label_temperature_tankData = QtWidgets.QLabel(self.dashboardPage)
        self.label_temperature_tankData.setGeometry(QtCore.QRect(210, 370, 55, 16))
        self.label_temperature_tankData.setStyleSheet("border-image: url(:/Images/Resources/whiteBG.png);")
        self.label_temperature_tankData.setObjectName("label_temperature_tankData")
        self.label_fishNetHoles_tankData = QtWidgets.QLabel(self.dashboardPage)
        self.label_fishNetHoles_tankData.setGeometry(QtCore.QRect(220, 420, 55, 16))
        self.label_fishNetHoles_tankData.setStyleSheet("border-image: url(:/Images/Resources/whiteBG.png);")
        self.label_fishNetHoles_tankData.setObjectName("label_fishNetHoles_tankData")
        self.label_fishnetNeedsCleaning_tankData = QtWidgets.QLabel(self.dashboardPage)
        self.label_fishnetNeedsCleaning_tankData.setGeometry(QtCore.QRect(290, 470, 55, 16))
        self.label_fishnetNeedsCleaning_tankData.setStyleSheet("border-image: url(:/Images/Resources/whiteBG.png);")
        self.label_fishnetNeedsCleaning_tankData.setObjectName("label_fishnetNeedsCleaning_tankData")
        self.label_pipesNeedChanging_tankData = QtWidgets.QLabel(self.dashboardPage)
        self.label_pipesNeedChanging_tankData.setGeometry(QtCore.QRect(270, 513, 55, 16))
        self.label_pipesNeedChanging_tankData.setStyleSheet("border-image: url(:/Images/Resources/whiteBG.png);")
        self.label_pipesNeedChanging_tankData.setObjectName("label_pipesNeedChanging_tankData")
        self.comboBox = QtWidgets.QComboBox(self.dashboardPage)
        self.comboBox.setGeometry(QtCore.QRect(300, 40, 128, 33))
        self.comboBox.setStyleSheet("QComboBox {\n"
"border-image: url(:/Resources/comboBoxBG.png);\n"
"    border-image: url(:/Images/Resources/comboBoxBG.png);\n"
"    color: black;\n"
"    font: 14px;\n"
"    padding: 1px 0px 1px 3px; /* This (useless) line resolves a bug with the font color */\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    color: red;\n"
"}\n"
"\n"
"QComboBox::drop-down \n"
"{\n"
"    border: 0px; /* This seems to replace the whole arrow of the combo box */\n"
"}")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.button_email = QtWidgets.QPushButton(self.dashboardPage)
        self.button_email.setGeometry(QtCore.QRect(220, 810, 127, 33))
        self.button_email.setStyleSheet("QPushButton{\n"
"    border-image: url(:/Images/Resources/EmailButton.png);\n"
"background-repeat: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border-image: url(:/Images/Resources/EmailButtonPressed.png);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    border-image: url(:/Images/Resources/EmailButtonPressed.png);\n"
"}")
        self.button_email.setText("")
        self.button_email.setObjectName("button_email")
        self.button_report = QtWidgets.QPushButton(self.dashboardPage)
        self.button_report.setGeometry(QtCore.QRect(370, 810, 127, 33))
        self.button_report.setStyleSheet("QPushButton{\n"
"    border-image: url(:/Images/Resources/report.png);\n"
"background-repeat: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border-image: url(:/Images/Resources/reportPressed.png);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    border-image: url(:/Images/Resources/reportPressed.png);\n"
"}")
        self.button_report.setText("")
        self.button_report.setObjectName("button_report")
        self.stackedWidget_2.addWidget(self.dashboardPage)
        self.createtankPage = QtWidgets.QWidget()
        self.createtankPage.setObjectName("createtankPage")
        self.lineEdit_fishType_createTank = QtWidgets.QLineEdit(self.createtankPage)
        self.lineEdit_fishType_createTank.setGeometry(QtCore.QRect(430, 500, 171, 22))
        self.lineEdit_fishType_createTank.setStyleSheet("border-image: url(:/Images/Resources/darkBlackBG.png);")
        self.lineEdit_fishType_createTank.setObjectName("lineEdit_fishType_createTank")
        self.lineEdit_date_createTank = QtWidgets.QLineEdit(self.createtankPage)
        self.lineEdit_date_createTank.setGeometry(QtCore.QRect(430, 540, 171, 22))
        self.lineEdit_date_createTank.setStyleSheet("border-image: url(:/Images/Resources/darkBlackBG.png);")
        self.lineEdit_date_createTank.setObjectName("lineEdit_date_createTank")
        self.lineEdit_feeding_createTank = QtWidgets.QLineEdit(self.createtankPage)
        self.lineEdit_feeding_createTank.setGeometry(QtCore.QRect(430, 590, 171, 22))
        self.lineEdit_feeding_createTank.setStyleSheet("border-image: url(:/Images/Resources/darkBlackBG.png);")
        self.lineEdit_feeding_createTank.setObjectName("lineEdit_feeding_createTank")
        self.lineEdit_lowerTemperatureThreshold_createTank = QtWidgets.QLineEdit(self.createtankPage)
        self.lineEdit_lowerTemperatureThreshold_createTank.setGeometry(QtCore.QRect(430, 640, 161, 22))
        self.lineEdit_lowerTemperatureThreshold_createTank.setStyleSheet("border-image: url(:/Images/Resources/darkBlackBG.png);")
        self.lineEdit_lowerTemperatureThreshold_createTank.setObjectName("lineEdit_lowerTemperatureThreshold_createTank")
        self.lineEdit_upperTemperatureThreshold_createTank = QtWidgets.QLineEdit(self.createtankPage)
        self.lineEdit_upperTemperatureThreshold_createTank.setGeometry(QtCore.QRect(430, 690, 161, 22))
        self.lineEdit_upperTemperatureThreshold_createTank.setStyleSheet("border-image: url(:/Images/Resources/darkBlackBG.png);")
        self.lineEdit_upperTemperatureThreshold_createTank.setObjectName("lineEdit_upperTemperatureThreshold_createTank")
        self.lineEdit_waterQualityThreshold_createTank = QtWidgets.QLineEdit(self.createtankPage)
        self.lineEdit_waterQualityThreshold_createTank.setGeometry(QtCore.QRect(430, 740, 161, 22))
        self.lineEdit_waterQualityThreshold_createTank.setStyleSheet("border-image: url(:/Images/Resources/darkBlackBG.png);")
        self.lineEdit_waterQualityThreshold_createTank.setObjectName("lineEdit_waterQualityThreshold_createTank")
        self.button_create_createTank = QtWidgets.QPushButton(self.createtankPage)
        self.button_create_createTank.setGeometry(QtCore.QRect(290, 810, 127, 33))
        self.button_create_createTank.setStyleSheet("border-image: url(:/Images/Resources/createButton.png);")
        self.button_create_createTank.setText("")
        self.button_create_createTank.setObjectName("button_create_createTank")
        self.stackedWidget_2.addWidget(self.createtankPage)
        self.analyzetankPage = QtWidgets.QWidget()
        self.analyzetankPage.setStyleSheet("border-image: url(:/Images/Resources/AnalyzeBG.png);")
        self.analyzetankPage.setObjectName("analyzetankPage")
        self.button_holes_analyzeTank = QtWidgets.QPushButton(self.analyzetankPage)
        self.button_holes_analyzeTank.setGeometry(QtCore.QRect(150, 530, 127, 33))
        self.button_holes_analyzeTank.setStyleSheet("border-image: url(:/Images/Resources/Holes.png);")
        self.button_holes_analyzeTank.setText("")
        self.button_holes_analyzeTank.setObjectName("button_holes_analyzeTank")
        self.button_cleaning_analyzeTank = QtWidgets.QPushButton(self.analyzetankPage)
        self.button_cleaning_analyzeTank.setGeometry(QtCore.QRect(300, 530, 127, 33))
        self.button_cleaning_analyzeTank.setStyleSheet("border-image: url(:/Images/Resources/Cleaning.png);")
        self.button_cleaning_analyzeTank.setText("")
        self.button_cleaning_analyzeTank.setObjectName("button_cleaning_analyzeTank")
        self.button_pipes_analyzeTank = QtWidgets.QPushButton(self.analyzetankPage)
        self.button_pipes_analyzeTank.setGeometry(QtCore.QRect(450, 530, 127, 33))
        self.button_pipes_analyzeTank.setStyleSheet("border-image: url(:/Images/Resources/Pipes.png);")
        self.button_pipes_analyzeTank.setText("")
        self.button_pipes_analyzeTank.setObjectName("button_pipes_analyzeTank")
        self.button_predict_analyzeTank = QtWidgets.QPushButton(self.analyzetankPage)
        self.button_predict_analyzeTank.setGeometry(QtCore.QRect(440, 740, 222, 34))
        self.button_predict_analyzeTank.setStyleSheet("border-image: url(:/Images/Resources/predict.png);")
        self.button_predict_analyzeTank.setText("")
        self.button_predict_analyzeTank.setObjectName("button_predict_analyzeTank")
        self.label_fishnetNeedsPatching_analyzeTank = QtWidgets.QLabel(self.analyzetankPage)
        self.label_fishnetNeedsPatching_analyzeTank.setGeometry(QtCore.QRect(300, 613, 55, 16))
        self.label_fishnetNeedsPatching_analyzeTank.setStyleSheet("border-image: url(:/Images/Resources/whiteBG.png);")
        self.label_fishnetNeedsPatching_analyzeTank.setObjectName("label_fishnetNeedsPatching_analyzeTank")
        self.label_fishnetNeedsCleaning_analyzeTank = QtWidgets.QLabel(self.analyzetankPage)
        self.label_fishnetNeedsCleaning_analyzeTank.setGeometry(QtCore.QRect(300, 653, 55, 16))
        self.label_fishnetNeedsCleaning_analyzeTank.setStyleSheet("border-image: url(:/Images/Resources/whiteBG.png);")
        self.label_fishnetNeedsCleaning_analyzeTank.setObjectName("label_fishnetNeedsCleaning_analyzeTank")
        self.label_pipesNeedChanging_analyzeTank = QtWidgets.QLabel(self.analyzetankPage)
        self.label_pipesNeedChanging_analyzeTank.setGeometry(QtCore.QRect(280, 705, 55, 16))
        self.label_pipesNeedChanging_analyzeTank.setStyleSheet("border-image: url(:/Images/Resources/whiteBG.png);")
        self.label_pipesNeedChanging_analyzeTank.setObjectName("label_pipesNeedChanging_analyzeTank")
        self.lineEdit_temperature_analyzeTank = QtWidgets.QLineEdit(self.analyzetankPage)
        self.lineEdit_temperature_analyzeTank.setGeometry(QtCore.QRect(560, 610, 113, 22))
        self.lineEdit_temperature_analyzeTank.setStyleSheet("border-image: url(:/Images/Resources/whiteBG.png);")
        self.lineEdit_temperature_analyzeTank.setObjectName("lineEdit_temperature_analyzeTank")
        self.lineEdit_waterSalinity_analyzeTank = QtWidgets.QLineEdit(self.analyzetankPage)
        self.lineEdit_waterSalinity_analyzeTank.setGeometry(QtCore.QRect(570, 700, 113, 22))
        self.lineEdit_waterSalinity_analyzeTank.setStyleSheet("border-image: url(:/Images/Resources/whiteBG.png);")
        self.lineEdit_waterSalinity_analyzeTank.setObjectName("lineEdit_waterSalinity_analyzeTank")
        self.label_camFeed = QtWidgets.QLabel(self.analyzetankPage)
        self.label_camFeed.setGeometry(QtCore.QRect(80, 200, 551, 281))
        self.label_camFeed.setStyleSheet("border-image: url(:/Images/Resources/semiDarkBG.png);")
        self.label_camFeed.setText("")
        self.label_camFeed.setObjectName("label_camFeed")
        self.stackedWidget_2.addWidget(self.analyzetankPage)
        self.settingsPage = QtWidgets.QWidget()
        self.settingsPage.setStyleSheet("border-image: url(:/Images/Resources/settingsWidget.png);")
        self.settingsPage.setObjectName("settingsPage")
        self.stackedWidget_2.addWidget(self.settingsPage)
        self.label_username_mainPage = QtWidgets.QLabel(self.mainPage)
        self.label_username_mainPage.setGeometry(QtCore.QRect(120, 140, 101, 16))
        self.label_username_mainPage.setStyleSheet("border-image: url(:/Images/Resources/blueBG.png);")
        self.label_username_mainPage.setObjectName("label_username_mainPage")
        self.label_user_admin = QtWidgets.QLabel(self.mainPage)
        self.label_user_admin.setGeometry(QtCore.QRect(140, 170, 101, 16))
        self.label_user_admin.setStyleSheet("border-image: url(:/Images/Resources/blueBG.png);")
        self.label_user_admin.setObjectName("label_user_admin")
        self.label_userLetter = QtWidgets.QLabel(self.mainPage)
        self.label_userLetter.setGeometry(QtCore.QRect(50, 140, 31, 31))
        self.label_userLetter.setStyleSheet("border-image: url(:/Images/Resources/greyBG.png);\n"
"font: 26pt \"MS Shell Dlg 2\";")
        self.label_userLetter.setObjectName("label_userLetter")
        self.stackedWidget.addWidget(self.mainPage)
        MainWindow.setCentralWidget(self.centralwidget)
        self.buttonsConnections()

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit_username_signIn.setText(_translate("MainWindow", "rowan"))
        self.lineEdit_password_signIn.setText(_translate("MainWindow", "1234"))
        self.lineEdit_firstName_signUp.setText(_translate("MainWindow", "First name"))
        self.lineEdit_lastName_signUp.setText(_translate("MainWindow", "Last name"))
        self.lineEdit_email_signUp.setText(_translate("MainWindow", "Email address"))
        self.lineEdit_username_signUp.setText(_translate("MainWindow", "Username"))
        self.lineEdit_password_signUp.setText(_translate("MainWindow", "Password"))
        self.label_fishType_tankData.setText(_translate("MainWindow", "Salmon"))
        self.label_harvestDate_tankData.setText(_translate("MainWindow", "29/7/2019"))
        self.label_feeding_tankData.setText(_translate("MainWindow", "6:00:00"))
        self.label_ph_tankData.setText(_translate("MainWindow", "--"))
        self.label_temperature_tankData.setText(_translate("MainWindow", "22"))
        self.label_fishNetHoles_tankData.setText(_translate("MainWindow", "1"))
        self.label_fishnetNeedsCleaning_tankData.setText(_translate("MainWindow", "No"))
        self.label_pipesNeedChanging_tankData.setText(_translate("MainWindow", "No"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Tank 1"))
        self.label_fishnetNeedsPatching_analyzeTank.setText(_translate("MainWindow", "No"))
        self.label_fishnetNeedsCleaning_analyzeTank.setText(_translate("MainWindow", "No"))
        self.label_pipesNeedChanging_analyzeTank.setText(_translate("MainWindow", "No"))
        self.lineEdit_temperature_analyzeTank.setText(_translate("MainWindow", "--"))
        self.lineEdit_waterSalinity_analyzeTank.setText(_translate("MainWindow", "--"))
        self.label_username_mainPage.setText(_translate("MainWindow", "Abdullah Salah"))
        self.label_user_admin.setText(_translate("MainWindow", "user"))
        self.label_userLetter.setText(_translate("MainWindow", "A"))


    def signInIsClicked(self):
        username_signIn = self.lineEdit_username_signIn.text()
        password_signIn = self.lineEdit_password_signIn.text()
        self.user = self.db.authenticateLogIn(username_signIn, password_signIn)
        self.tankList = self.db.loadTankList(self.user.getUserID())
        self.numberOfTanks = len(self.tankList)
        for i in range(self.numberOfTanks-2):
            name = "Tank" + str(i+2)
            self.comboBox.addItem(name)
        self.tankIndex = self.comboBox.currentIndex()
        self.waterQualityList = self.db.loadWaterQualityList(self.tankList[self.tankIndex].getTankID())
        self.sen = Sensors("http://192.168.43.223/")
        if(self.user):
            self.displayList(self.tankIndex)
            self.stackedWidget.setCurrentIndex(3)
            self.cam.start()
            self.camTimer.timeout.connect(lambda: self.camFeedFunc())
            self.camTimer.start(100)
        else:
            print("INVALID USERNAME OR PASSWORD")

    def camFeedFunc(self):
        self.fr = self.cam.getFrame()
        frame = cv2.cvtColor(self.fr, cv2.COLOR_BGR2RGB)
        img = QtGui.QImage(frame, frame.shape[1], frame.shape[0], QtGui.QImage.Format_RGB888)
        pix = QtGui.QPixmap.fromImage(img)
        self.label_camFeed.setScaledContents(True)
        self.label_camFeed.setPixmap(pix)

    def captureImage(self):
        return self.fr.copy()

    def displayList(self, tankIndex):
        if(self.user):
            self.label_username_mainPage.setText(self.user.getFirstName() + " " + self.user.getLastName())
            self.label_user_admin.setText("")
            self.label_fishType_tankData.setText(self.tankList[tankIndex].getFishType())
            self.label_harvestDate_tankData.setText(self.tankList[tankIndex].getHarvestDate())
            self.label_feeding_tankData.setText(self.tankList[tankIndex].getFeedingSchedule())
            self.label_ph_tankData.setText(str(self.waterQualityList[0].getpH()))
            self.temp = self.sen.getTemperature()
            if(self.temp > 20):
                self.label_temperature_tankData.setText( "WARNING! Temperature is " + self.temp + " C")
                self.em = emailNotifier(self.user, self.temp)
                self.em.sendEmail()
            else:
                self.label_temperature_tankData.setText(self.sen.getTemperature())


    def updateTankData(self):
        self.tankIndex = self.comboBox.currentIndex()
        self.displayList(self.tankIndex)


    def signUpfromLoginPageIsClicked(self):
        self.stackedWidget.setCurrentIndex(1)

    def signUpfromsignUpPageIsClicked(self):
        self.stackedWidget.setCurrentIndex(0)
        username_signUp=self.lineEdit_username_signUp.text()
        password_signUp=self.lineEdit_password_signUp.text()
        firstName_signUp=self.lineEdit_firstName_signUp.text()
        lastName_signUp=self.lineEdit_lastName_signUp.text()
        email_signUp=self.lineEdit_email_signUp.text()


    def faceIdIsClicked(self):
        self.stackedWidget.setCurrentIndex(2)

    def goToLoginPage(self):
        self.stackedWidget.setCurrentIndex(0)

    def dashboardIsClicked(self):
        self.stackedWidget_2.setCurrentIndex(0)

    def createTankIsClicked(self):
        self.stackedWidget_2.setCurrentIndex(1)

    def createTankButtonClicked(self):
        fishType_createTank= self.lineEdit_fishType_createTank.text()
        date_createTank= self.lineEdit_date_createTank.text()
        feeding_createTank= self.lineEdit_feeding_createTank.text()
        lowerTemperatureThreshold_createTank= self.lineEdit_lowerTemperatureThreshold_createTank.text()
        upperTemperatureThreshold_createTank= self.lineEdit_upperTemperatureThreshold_createTank.text()
        waterQualityThreshold_createTank= self.lineEdit_waterQualityThreshold_createTank.text()

    def reportIsClicked(self):
        webbrowser.open("https://app.powerbi.com/view?r=eyJrIjoiZjhkMzViNTUtMDU3Yy00NTBhLTg1OWUtZjU1OGU1NzcyZjFiIiwidCI6ImVhZjYyNGM4LWEwYzQtNDE5NS04N2QyLTQ0M2U1ZDc1MTZjZCIsImMiOjh9&fbclid=IwAR29_qNsg6Nwu1QKUFX6OjKhhUDT77pEpZHJDb0ZE1-OwoRCjhy1En90DAc")


    def emailIsClicked(self):
        pass

    def analyzeTankIsClicked(self):
        self.stackedWidget_2.setCurrentIndex(2)

    def settingsIsClicked(self):
        self.stackedWidget_2.setCurrentIndex(3)

    def cleaningIsClicked(self):
        pred = self.clean.predict(self.captureImage())
        if(pred == "yes"):
            self.label_fishnetNeedsCleaning_analyzeTank.setText("Yes")
        elif(pred == "no"):
            self.label_fishnetNeedsCleaning_analyzeTank.setText("No")
        else:
            self.label_fishnetNeedsCleaning_analyzeTank.setText("Can't determine")

    def holesIsClicked(self):
        pred = self.holes.predict(self.captureImage())
        if(pred == "yes"):
            self.label_fishnetNeedsPatching_analyzeTank.setText("Yes")
        elif(pred == "no"):
            self.label_fishnetNeedsPatching_analyzeTank.setText("No")
        else:
            self.label_fishnetNeedsPatching_analyzeTank.setText("Can't determine")

    def pipesIsClicked(self):
        pass

    def predictIsClicked(self):
        pass

    def buttonsConnections(self):
        self.button_signIn_signIn.clicked.connect(self.signInIsClicked)
        self.button_signUp_signIn.clicked.connect(self.signUpfromLoginPageIsClicked)
        self.button_faceID_signIn.clicked.connect(self.faceIdIsClicked)
        self.button_backToSignIn.clicked.connect(self.goToLoginPage)
        self.button_signUp_signUp.clicked.connect(self.signUpfromsignUpPageIsClicked)
        self.button_logout.clicked.connect(self.goToLoginPage)
        self.button_dashboard.clicked.connect(self.dashboardIsClicked)
        self.button_createTank.clicked.connect(self.createTankIsClicked)
        self.button_analyzeTank.clicked.connect(self.analyzeTankIsClicked)
        self.button_settings.clicked.connect(self.settingsIsClicked)
        self.button_cleaning_analyzeTank.clicked.connect(self.cleaningIsClicked)
        self.button_holes_analyzeTank.clicked.connect(self.holesIsClicked)
        self.button_pipes_analyzeTank.clicked.connect(self.pipesIsClicked)
        self.button_predict_analyzeTank.clicked.connect(self.predictIsClicked)
        self.button_create_createTank.clicked.connect(self.createTankButtonClicked)
        self.button_report.clicked.connect(self.reportIsClicked)
        self.button_email.clicked.connect(self.emailIsClicked)
        self.comboBox.currentIndexChanged.connect(self.updateTankData)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
