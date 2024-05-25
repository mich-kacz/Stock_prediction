import pandas as pd


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'guijSNBgS.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(978, 682)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setStrikeOut(False)
        self.label_2.setFont(font)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setTextFormat(Qt.TextFormat.AutoText)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.comboBox = QComboBox(self.frame)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMaxVisibleItems(0)
        self.comboBox.setInsertPolicy(QComboBox.InsertPolicy.InsertAlphabetically)

        self.verticalLayout_2.addWidget(self.comboBox)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_2.addItem(self.horizontalSpacer)

        self.NextButton = QPushButton(self.frame)
        self.NextButton.setObjectName(u"NextButton")

        self.verticalLayout_2.addWidget(self.NextButton)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)

        self.marketName = QLineEdit(self.frame)
        self.marketName.setObjectName(u"marketName")
        font2 = QFont()
        font2.setPointSize(12)
        self.marketName.setFont(font2)
        self.marketName.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.marketName)

        self.tableWidget_2 = QTableWidget(self.frame)
        self.tableWidget_2.setObjectName(u"tableWidget_2")

        self.verticalLayout.addWidget(self.tableWidget_2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setTextFormat(Qt.TextFormat.AutoText)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.InputStockName = QLineEdit(self.frame)
        self.InputStockName.setObjectName(u"InputStockName")
        self.InputStockName.setFont(font2)
        self.InputStockName.setText(u"")
        self.InputStockName.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.InputStockName)

        self.tableWidget = QTableWidget(self.frame)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout.addWidget(self.tableWidget)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 978, 19))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tableWidget_2.itemClicked.connect(self.item_clicked_table_2)
        self.tableWidget.itemClicked.connect(self.item_clicked_table)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Model", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"SVR", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"CNN-LSTM", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Transformer", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"LSTM", None))

        self.comboBox.setCurrentText(QCoreApplication.translate("MainWindow", u"SVR", None))
        self.NextButton.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Market name", None))
        self.marketName.setText("")
        self.marketName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type market name here", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Stock name", None))
        self.InputStockName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type stock ticker here", None))
    # retranslateUi

    def registerCallbacks(self, marketCallback, buttonCallback):
        self.marketCallback = marketCallback
        self.buttonCallback = buttonCallback


    def item_clicked_table_2(self, item):
        # Get the text of the clicked item
        text = item.text()
        self.marketName.setText(text)
        self.marketCallback(self.marketName.text())
    def item_clicked_table(self, item):
        # Get the text of the clicked item
        self.InputStockName.setText(item.text())


    def setMarketNames(self, df : pd.DataFrame):
        num_rows, num_cols = df.shape
        self.tableWidget_2.setRowCount(num_rows)
        self.tableWidget_2.setColumnCount(num_cols)
        self.tableWidget_2.setHorizontalHeaderLabels(df.columns.values)
        for i in range(num_rows):
            for j in range(num_cols):
                item = QTableWidgetItem(str(df.iloc[i, j]))  # Convert each DataFrame cell to a QTableWidgetItem
                self.tableWidget_2.setItem(i, j, item)

    def setCompounds(self, df : pd.DataFrame):
        num_rows, num_cols = df.shape
        self.tableWidget.setRowCount(num_rows)
        self.tableWidget.setColumnCount(num_cols)
        self.tableWidget.setHorizontalHeaderLabels(df.columns.values)
        for i in range(num_rows):
            for j in range(num_cols):
                item = QTableWidgetItem(str(df.iloc[i, j]))  # Convert each DataFrame cell to a QTableWidgetItem
                self.tableWidget.setItem(i, j, item)
