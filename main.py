# -*- coding: utf-8 -*-

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QDateTimeEdit, QFontComboBox,
    QGridLayout, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QSpinBox, QStackedWidget, QTabWidget,
    QTimeEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(381, 165)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
#if QT_CONFIG(statustip)
        MainWindow.setStatusTip(u"\u65f6\u949f")
#endif // QT_CONFIG(statustip)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy1)
        self.tabWidget.setLayoutDirection(Qt.LeftToRight)
        self.tabWidget.setTabPosition(QTabWidget.East)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_2 = QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.timeLable = QLabel(self.tab)
        self.timeLable.setObjectName(u"timeLable")
        font = QFont()
        font.setFamilies([u"Aldrich"])
        font.setPointSize(48)
        font.setBold(False)
        font.setStyleStrategy(QFont.PreferDefault)
        self.timeLable.setFont(font)
        self.timeLable.setTextFormat(Qt.RichText)
        self.timeLable.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.timeLable, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_3 = QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.stackedWidget = QStackedWidget(self.tab_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_4 = QGridLayout(self.page)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.pushButton = QPushButton(self.page)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_4.addWidget(self.pushButton, 2, 0, 1, 1)

        self.timeEdit = QTimeEdit(self.page)
        self.timeEdit.setObjectName(u"timeEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.timeEdit.sizePolicy().hasHeightForWidth())
        self.timeEdit.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setPointSize(22)
        font1.setBold(False)
        self.timeEdit.setFont(font1)
        self.timeEdit.setWrapping(False)
        self.timeEdit.setFrame(True)
        self.timeEdit.setAlignment(Qt.AlignCenter)
        self.timeEdit.setAccelerated(False)
        self.timeEdit.setCorrectionMode(QAbstractSpinBox.CorrectToPreviousValue)
        self.timeEdit.setKeyboardTracking(True)
        self.timeEdit.setProperty("showGroupSeparator", False)
        self.timeEdit.setCurrentSection(QDateTimeEdit.HourSection)
        self.timeEdit.setCalendarPopup(True)

        self.gridLayout_4.addWidget(self.timeEdit, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_5 = QGridLayout(self.page_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.countdownTimeLable = QLabel(self.page_2)
        self.countdownTimeLable.setObjectName(u"countdownTimeLable")
        self.countdownTimeLable.setFont(font)
        self.countdownTimeLable.setTextFormat(Qt.RichText)
        self.countdownTimeLable.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.countdownTimeLable, 0, 0, 1, 1)

        self.stopCountdownButton = QPushButton(self.page_2)
        self.stopCountdownButton.setObjectName(u"stopCountdownButton")

        self.gridLayout_5.addWidget(self.stopCountdownButton, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_2)

        self.gridLayout_3.addWidget(self.stackedWidget, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_6 = QGridLayout(self.tab_4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_2 = QLabel(self.tab_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_2, 4, 0, 1, 1)

        self.fontComboBox = QFontComboBox(self.tab_4)
        self.fontComboBox.setObjectName(u"fontComboBox")
        font2 = QFont()
        font2.setFamilies([u"Aldrich"])
        self.fontComboBox.setCurrentFont(font2)

        self.gridLayout_6.addWidget(self.fontComboBox, 2, 1, 1, 2)

        self.label_3 = QLabel(self.tab_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_3, 5, 0, 1, 1)

        self.normalSpinBox = QSpinBox(self.tab_4)
        self.normalSpinBox.setObjectName(u"normalSpinBox")
        self.normalSpinBox.setAutoFillBackground(False)
        self.normalSpinBox.setMaximum(500)
        self.normalSpinBox.setSingleStep(2)
        self.normalSpinBox.setValue(48)

        self.gridLayout_6.addWidget(self.normalSpinBox, 4, 1, 1, 2)

        self.smallSpinBox = QSpinBox(self.tab_4)
        self.smallSpinBox.setObjectName(u"smallSpinBox")
        self.smallSpinBox.setMaximum(495)
        self.smallSpinBox.setSingleStep(2)
        self.smallSpinBox.setStepType(QAbstractSpinBox.DefaultStepType)
        self.smallSpinBox.setValue(36)

        self.gridLayout_6.addWidget(self.smallSpinBox, 5, 1, 1, 2)

        self.label_4 = QLabel(self.tab_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_4, 2, 0, 1, 1)

        self.label = QLabel(self.tab_4)
        self.label.setObjectName(u"label")
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setTextFormat(Qt.RichText)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label, 0, 0, 2, 2)

        self.aboutQtButton = QPushButton(self.tab_4)
        self.aboutQtButton.setObjectName(u"aboutQtButton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.aboutQtButton.sizePolicy().hasHeightForWidth())
        self.aboutQtButton.setSizePolicy(sizePolicy3)

        self.gridLayout_6.addWidget(self.aboutQtButton, 0, 2, 2, 1)

        self.tabWidget.addTab(self.tab_4, "")

        self.gridLayout.addWidget(self.tabWidget, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(2)
        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Chaonx", None))
#if QT_CONFIG(tooltip)
        MainWindow.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.timeLable.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:48pt;\">00:00</span><span style=\" font-size:36pt;\">:00</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"T", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.timeEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"H:mm:ss", None))
        self.countdownTimeLable.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:48pt;\">00:00</span><span style=\" font-size:36pt;\">:00</span></p></body></html>", None))
        self.stopCountdownButton.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"C", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u65f6/\u5206 \u5b57\u53f7", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u79d2 \u5b57\u53f7", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u5b57\u4f53", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Chaonx </span><span style=\" font-size:16pt; vertical-align:sub;\">v1.0</span></p></body></html>", None))
        self.aboutQtButton.setText(QCoreApplication.translate("MainWindow", u"About Qt", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"S", None))
    # retranslateUi


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.timer = QTimer()
        self.timer.timeout.connect(self.showTime)
        self.timer.start(1000)

        self.normal_size = 48
        self.small_size = 36

        self.countdownTime = QTime(0, 0)
        self.countdownTimer = QTimer()
        self.countdownTimer.timeout.connect(self.updateCountdown)
        
        self.ui.pushButton.clicked.connect(self.setCountdown)
        self.ui.stopCountdownButton.clicked.connect(self.stopCountdown)
        
        self.ui.fontComboBox.currentFontChanged.connect(self.setFont)
        self.ui.normalSpinBox.valueChanged.connect(self.setFont)
        self.ui.smallSpinBox.valueChanged.connect(self.setFont)
        
        self.ui.aboutQtButton.clicked.connect(self.aboutQt)
    
    def setFont(self):
        self.ui.timeLable.setFont(self.ui.fontComboBox.currentFont())
        self.ui.countdownTimeLable.setFont(self.ui.fontComboBox.currentFont())
        self.normal_size = self.ui.normalSpinBox.value()
        self.small_size = self.ui.smallSpinBox.value()

    def showTime(self):
        currentTime = QDateTime.currentDateTime()
        displayTimeHM, displayTimeS = currentTime.toString('hh:mm'), currentTime.toString('ss')
        self.ui.timeLable.setText(f"<html><head/><body><p><span style=\" font-size:{self.normal_size}pt;\">{displayTimeHM}</span><span style=\" font-size:{self.small_size}pt;\">:{displayTimeS}</span></p></body></html>")
    
    def setCountdown(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.countdownTime = self.ui.timeEdit.time()
        self.countdownTimer.start(1000)
        cdTimeHM, cdTimeS = self.countdownTime.toString('H:mm'), self.countdownTime.toString('ss')
        self.ui.countdownTimeLable.setText(f"<html><head/><body><p><span style=\" font-size:{self.normal_size}pt;\">{cdTimeHM}</span><span style=\" font-size:{self.small_size}pt;\">:{cdTimeS}</span></p></body></html>")

    def updateCountdown(self):
        self.countdownTime = self.countdownTime.addSecs(-1)
        cdTimeHM, cdTimeS = self.countdownTime.toString('H:mm'), self.countdownTime.toString('ss')
        self.ui.countdownTimeLable.setText(f"<html><head/><body><p><span style=\" font-size:{self.normal_size}pt;\">{cdTimeHM}</span><span style=\" font-size:{self.small_size}pt;\">:{cdTimeS}</span></p></body></html>")
        if self.countdownTime == QTime(0, 0):
            self.countdownTimer.stop()
            self.ui.countdownTimeLable.setText(f"<html><head/><body><p><span style=\" font-size:{self.normal_size}pt; color:#ff587f;\">0:00</span><span style=\" font-size:{self.small_size}pt; color:#ff587f;\">:00</span></p></body></html>")
    
    def stopCountdown(self):
        self.countdownTimer.stop()
        self.ui.stackedWidget.setCurrentIndex(0)
        
    def aboutQt(self):
        QApplication.aboutQt()
        
if __name__ == "__main__":
    import sys
    from PySide6.QtCore import QTimer
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())