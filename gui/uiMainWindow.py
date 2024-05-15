
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.InputStockName = QLineEdit(self.centralwidget)
        self.InputStockName.setObjectName(u"InputStockName")
        self.InputStockName.setGeometry(QRect(100, 170, 121, 31))
        font = QFont()
        font.setPointSize(12)
        self.InputStockName.setFont(font)
        self.InputStockName.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(100, 139, 121, 31))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setStrikeOut(False)
        self.label.setFont(font1)
        self.label.setAutoFillBackground(False)
        self.label.setTextFormat(Qt.TextFormat.AutoText)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(500, 170, 151, 31))
        self.comboBox.setMaxVisibleItems(0)
        self.comboBox.setInsertPolicy(QComboBox.InsertPolicy.InsertAlphabetically)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(500, 140, 151, 31))
        self.label_2.setFont(font1)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setTextFormat(Qt.TextFormat.AutoText)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(640, 480, 91, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 19))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.InputStockName.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Stock name", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"SVR", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"CNN-LSTM", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Transformer", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"LSTM", None))

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Model", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Next", None))
    # retranslateUi

