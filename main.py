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
    QTimeEdit, QWidget, QSlider, QDoubleSpinBox, QHBoxLayout)

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
        self.gridLayout.setContentsMargins(4, 4, 4, 4)
        self.gridLayout.setSpacing(4)
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
        self.gridLayout_2.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_2.setSpacing(2)
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
        self.gridLayout_3.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_3.setSpacing(2)
        self.stackedWidget = QStackedWidget(self.tab_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_4 = QGridLayout(self.page)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_4.setSpacing(2)
        self.pushButton = QPushButton(self.page)
        self.pushButton.setObjectName(u"pushButton")

        self.quick10Button = QPushButton(self.page)
        self.quick10Button.setObjectName(u"quick10Button")
        self.quick10Button.setMaximumSize(QSize(30, 16777215))

        self.quick30Button = QPushButton(self.page)
        self.quick30Button.setObjectName(u"quick30Button")
        self.quick30Button.setMaximumSize(QSize(30, 16777215))

        self.quick60Button = QPushButton(self.page)
        self.quick60Button.setObjectName(u"quick60Button")
        self.quick60Button.setMaximumSize(QSize(30, 16777215))

        self.gridLayout_4.addWidget(self.quick10Button, 2, 0, 1, 1)
        self.gridLayout_4.addWidget(self.quick30Button, 2, 1, 1, 1)
        self.gridLayout_4.addWidget(self.quick60Button, 2, 2, 1, 1)
        self.gridLayout_4.addWidget(self.pushButton, 2, 3, 1, 1)

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

        self.gridLayout_4.addWidget(self.timeEdit, 1, 0, 1, 4)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_5 = QGridLayout(self.page_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_5.setSpacing(2)
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
        self.gridLayout_6.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_6.setSpacing(4)
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
        self.normalSpinBox.setValue(72)

        self.gridLayout_6.addWidget(self.normalSpinBox, 4, 1, 1, 1)

        self.normalSlider = QSlider(self.tab_4)
        self.normalSlider.setObjectName(u"normalSlider")
        self.normalSlider.setOrientation(Qt.Horizontal)
        self.normalSlider.setMinimum(8)
        self.normalSlider.setMaximum(256)
        self.normalSlider.setSingleStep(2)
        self.normalSlider.setPageStep(2)
        self.normalSlider.setValue(72)

        self.gridLayout_6.addWidget(self.normalSlider, 4, 2, 1, 1)

        self.smallSpinBox = QSpinBox(self.tab_4)
        self.smallSpinBox.setObjectName(u"smallSpinBox")
        self.smallSpinBox.setMaximum(495)
        self.smallSpinBox.setSingleStep(2)
        self.smallSpinBox.setStepType(QAbstractSpinBox.DefaultStepType)
        self.smallSpinBox.setValue(54)

        self.gridLayout_6.addWidget(self.smallSpinBox, 5, 1, 1, 1)

        self.smallSlider = QSlider(self.tab_4)
        self.smallSlider.setObjectName(u"smallSlider")
        self.smallSlider.setOrientation(Qt.Horizontal)
        self.smallSlider.setMinimum(8)
        self.smallSlider.setMaximum(256)
        self.smallSlider.setSingleStep(2)
        self.smallSlider.setPageStep(2)
        self.smallSlider.setValue(54)

        self.gridLayout_6.addWidget(self.smallSlider, 5, 2, 1, 1)

        self.label_4 = QLabel(self.tab_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_4, 2, 0, 1, 1)

        self.offsetLayout = QHBoxLayout()
        self.offsetLayout.setObjectName(u"offsetLayout")
        self.offsetLayout.setContentsMargins(0, 0, 0, 0)
        self.offsetLayout.setSpacing(4)

        self.offsetLabel = QLabel(self.tab_4)
        self.offsetLabel.setObjectName(u"offsetLabel")
        self.offsetLabel.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.offsetLayout.addWidget(self.offsetLabel)

        self.verticalOffsetSpin = QSpinBox(self.tab_4)
        self.verticalOffsetSpin.setObjectName(u"verticalOffsetSpin")
        self.verticalOffsetSpin.setMinimum(-100)
        self.verticalOffsetSpin.setMaximum(100)
        self.verticalOffsetSpin.setSingleStep(1)
        self.verticalOffsetSpin.setValue(0)
        self.verticalOffsetSpin.setMaximumWidth(80)
        self.offsetLayout.addWidget(self.verticalOffsetSpin)

        self.gridLayout_6.addLayout(self.offsetLayout, 6, 0, 1, 3)

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
        self.offsetLabel.setText(QCoreApplication.translate("MainWindow", u"\u5782\u76f4\u504f\u79fb", None))
        self.quick10Button.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.quick30Button.setText(QCoreApplication.translate("MainWindow", u"30", None))
        self.quick60Button.setText(QCoreApplication.translate("MainWindow", u"60", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"S", None))
    # retranslateUi


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.is_topmost = False
        self.ctrl_pressed = False
        
        # Setting to control window buttons (minimize/maximize)
        self.show_window_buttons = False
        self.timer = QTimer()
        self.timer.timeout.connect(self.showTime)
        self.timer.start(1000)

        self.normal_size = 72
        self.small_size = 54
        self.vertical_offset = 0

        self.countdownTime = QTime(0, 0)
        self.countdownTimer = QTimer()
        self.countdownTimer.timeout.connect(self.updateCountdown)
        
        self.ui.pushButton.clicked.connect(self.setCountdown)
        self.ui.stopCountdownButton.clicked.connect(self.stopCountdown)
        self.ui.quick10Button.clicked.connect(lambda: self.quickCountdown(10))
        self.ui.quick30Button.clicked.connect(lambda: self.quickCountdown(30))
        self.ui.quick60Button.clicked.connect(lambda: self.quickCountdown(60))
        
        self.ui.fontComboBox.currentFontChanged.connect(self.setFont)
        self.ui.normalSpinBox.valueChanged.connect(self._onNormalSpinChanged)
        self.ui.smallSpinBox.valueChanged.connect(self._onSmallSpinChanged)
        self.ui.normalSlider.valueChanged.connect(self._onNormalSliderChanged)
        self.ui.smallSlider.valueChanged.connect(self._onSmallSliderChanged)
        self.ui.verticalOffsetSpin.valueChanged.connect(self._onVerticalOffsetChanged)
        
        self._updateTitle()
    
    def setFont(self):
        self.ui.timeLable.setFont(self.ui.fontComboBox.currentFont())
        self.ui.countdownTimeLable.setFont(self.ui.fontComboBox.currentFont())
        self.normal_size = self.ui.normalSpinBox.value()
        self.small_size = self.ui.smallSpinBox.value()
        self._renderNow()
        self._passiveResize()

    def _onNormalSpinChanged(self, value):
        if self.ui.normalSlider.value() != value:
            self.ui.normalSlider.setValue(value)
        self.normal_size = value
        self._renderNow()
        self._passiveResize()

    def _onSmallSpinChanged(self, value):
        if self.ui.smallSlider.value() != value:
            self.ui.smallSlider.setValue(value)
        self.small_size = value
        self._renderNow()
        self._passiveResize()

    def _onNormalSliderChanged(self, value):
        if self.ui.normalSpinBox.value() != value:
            self.ui.normalSpinBox.setValue(value)

    def _onSmallSliderChanged(self, value):
        if self.ui.smallSpinBox.value() != value:
            self.ui.smallSpinBox.setValue(value)

    def _onVerticalOffsetChanged(self, value):
        self.vertical_offset = int(value)
        self._applyVerticalOffset()
        self._renderNow()

    def _passiveResize(self):
        # Passive resize: let Qt handle the sizing naturally, but enforce screen limits
        self.adjustSize()  # Let Qt calculate optimal size based on content
        
        # Enforce screen size limits after Qt's natural sizing
        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        max_width = screen_geometry.width() - 50  # 50px margin
        max_height = screen_geometry.height() - 50  # 50px margin
        
        current_size = self.size()
        if current_size.width() > max_width or current_size.height() > max_height:
            new_width = min(current_size.width(), max_width)
            new_height = min(current_size.height(), max_height)
            self.resize(new_width, new_height)

    def _applyVerticalOffset(self):
        top_margin = max(0, self.vertical_offset)
        bottom_margin = max(0, -self.vertical_offset)
        # Compact side margins while applying vertical offset
        self.ui.timeLable.setContentsMargins(0, top_margin, 0, bottom_margin)
        self.ui.countdownTimeLable.setContentsMargins(0, top_margin, 0, bottom_margin)

    def _getFontSizes(self):
        # Return actual font sizes without scaling
        return self.normal_size, self.small_size

    def _renderNow(self):
        # update both labels using current time/countdown values
        self.showTime()
        if self.ui.stackedWidget.currentIndex() == 1:
            # force countdown label refresh with current stored time
            self._renderCountdown()

    def showTime(self):
        currentTime = QDateTime.currentDateTime()
        displayTimeHM, displayTimeS = currentTime.toString('hh:mm'), currentTime.toString('ss')
        normal_pt, small_pt = self._getFontSizes()
        self.ui.timeLable.setText(f"<html><head/><body><p><span style=\" font-size:{normal_pt}pt;\">{displayTimeHM}</span><span style=\" font-size:{small_pt}pt;\">:{displayTimeS}</span></p></body></html>")
    
    def setCountdown(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.countdownTime = self.ui.timeEdit.time()
        self.countdownTimer.start(1000)
        self._renderCountdown()

    def updateCountdown(self):
        self.countdownTime = self.countdownTime.addSecs(-1)
        self._renderCountdown()
        if self.countdownTime == QTime(0, 0):
            self.countdownTimer.stop()
            normal_pt, small_pt = self._getFontSizes()
            self.ui.countdownTimeLable.setText(f"<html><head/><body><p><span style=\" font-size:{normal_pt}pt; color:#ff587f;\">0:00</span><span style=\" font-size:{small_pt}pt; color:#ff587f;\">:00</span></p></body></html>")
    
    def stopCountdown(self):
        self.countdownTimer.stop()
        self.ui.stackedWidget.setCurrentIndex(0)
        
    def aboutQt(self):
        QApplication.aboutQt()

    def _renderCountdown(self):
        # Fix display for times >= 60 minutes
        total_seconds = self.countdownTime.hour() * 3600 + self.countdownTime.minute() * 60 + self.countdownTime.second()
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        
        if hours > 0:
            cdTimeHM = f"{hours}:{minutes:02d}"
            cdTimeS = f"{seconds:02d}"
        else:
            cdTimeHM = f"{minutes:02d}"
            cdTimeS = f"{seconds:02d}"
        
        normal_pt, small_pt = self._getFontSizes()
        self.ui.countdownTimeLable.setText(f"<html><head/><body><p><span style=\" font-size:{normal_pt}pt;\">{cdTimeHM}</span><span style=\" font-size:{small_pt}pt;\">:{cdTimeS}</span></p></body></html>")

    def _updateTitle(self):
        base_title = "CHAONX" if self.is_topmost else "Chaonx"
        if self.ctrl_pressed:
            base_title += " [MOD]"
        self.setWindowTitle(base_title)

    def _updateWindowFlags(self):
        flags = Qt.Window | Qt.WindowCloseButtonHint
        if self.is_topmost:
            flags |= Qt.WindowStaysOnTopHint
        if self.show_window_buttons:
            flags |= Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint
        self.setWindowFlags(flags)

    def _adjustWindowSize(self):
        # Get screen size to limit window growth
        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        max_width = screen_geometry.width()
        max_height = screen_geometry.height()
        
        # Calculate required size based on font sizes
        normal_pt, small_pt = self._scaledSizes()
        
        # Estimate required width and height based on font sizes
        # Add some padding for UI elements
        estimated_width = max(300, normal_pt * 8)  # Minimum 300px, scale with font
        estimated_height = max(200, normal_pt * 3)  # Minimum 200px, scale with font
        
        # Limit to screen size
        new_width = min(estimated_width, max_width - 50)  # Leave 50px margin
        new_height = min(estimated_height, max_height - 50)  # Leave 50px margin
        
        # Only resize if the new size is significantly different
        current_size = self.size()
        if abs(current_size.width() - new_width) > 20 or abs(current_size.height() - new_height) > 20:
            self.resize(new_width, new_height)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_T:
            self.is_topmost = not self.is_topmost
            self._updateWindowFlags()
            self.show()
            self._updateTitle()
        elif event.key() == Qt.Key_Control:
            self.ctrl_pressed = True
            self._updateTitle()
        else:
            super().keyPressEvent(event)

    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key_Control:
            self.ctrl_pressed = False
            self._updateTitle()
        else:
            super().keyReleaseEvent(event)

    def wheelEvent(self, event):
        if self.ctrl_pressed:
            delta = event.angleDelta().y()
            if delta > 0:
                # Scroll up - increase font sizes
                self.ui.normalSpinBox.setValue(self.ui.normalSpinBox.value() + 4)
                self.ui.smallSpinBox.setValue(self.ui.smallSpinBox.value() + 4)
            else:
                # Scroll down - decrease font sizes
                self.ui.normalSpinBox.setValue(self.ui.normalSpinBox.value() - 4)
                self.ui.smallSpinBox.setValue(self.ui.smallSpinBox.value() - 4)
        else:
            super().wheelEvent(event)

    def quickCountdown(self, minutes):
        self.ui.stackedWidget.setCurrentIndex(1)
        # Fix: Create time properly for minutes >= 60
        hours = minutes // 60
        mins = minutes % 60
        self.countdownTime = QTime(hours, mins, 0)
        self.countdownTimer.start(1000)
        self._renderCountdown()

    def resizeEvent(self, event):
        self._applyVerticalOffset()
        self._renderNow()
        return super().resizeEvent(event)
        
if __name__ == "__main__":
    import sys
    from PySide6.QtCore import QTimer
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())