# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QPushButton, QSizePolicy,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.setEnabled(True)
        Widget.resize(300, 300)
        self.line = QFrame(Widget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(190, 0, 20, 300))
        font = QFont()
        font.setPointSize(72)
        self.line.setFont(font)
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_2 = QFrame(Widget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(90, 0, 20, 300))
        self.line_2.setFont(font)
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_3 = QFrame(Widget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(0, 190, 300, 20))
        self.line_3.setFont(font)
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_4 = QFrame(Widget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(0, 90, 300, 20))
        self.line_4.setFont(font)
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)
        self.btn_00 = QPushButton(Widget)
        self.btn_00.setObjectName(u"btn_00")
        self.btn_00.setGeometry(QRect(-1, 0, 101, 100))
        self.btn_01 = QPushButton(Widget)
        self.btn_01.setObjectName(u"btn_01")
        self.btn_01.setGeometry(QRect(100, 0, 100, 100))
        self.btn_02 = QPushButton(Widget)
        self.btn_02.setObjectName(u"btn_02")
        self.btn_02.setGeometry(QRect(200, 0, 101, 100))
        self.btn_11 = QPushButton(Widget)
        self.btn_11.setObjectName(u"btn_11")
        self.btn_11.setGeometry(QRect(100, 100, 100, 100))
        self.btn_12 = QPushButton(Widget)
        self.btn_12.setObjectName(u"btn_12")
        self.btn_12.setGeometry(QRect(200, 100, 101, 100))
        self.btn_10 = QPushButton(Widget)
        self.btn_10.setObjectName(u"btn_10")
        self.btn_10.setGeometry(QRect(-1, 100, 101, 100))
        self.btn_21 = QPushButton(Widget)
        self.btn_21.setObjectName(u"btn_21")
        self.btn_21.setGeometry(QRect(100, 200, 100, 101))
        self.btn_20 = QPushButton(Widget)
        self.btn_20.setObjectName(u"btn_20")
        self.btn_20.setGeometry(QRect(-1, 200, 101, 101))
        self.btn_22 = QPushButton(Widget)
        self.btn_22.setObjectName(u"btn_22")
        self.btn_22.setGeometry(QRect(200, 200, 101, 101))

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Tic_Tac_Toe", None))
        self.btn_00.setText("")
        self.btn_01.setText("")
        self.btn_02.setText("")
        self.btn_11.setText("")
        self.btn_12.setText("")
        self.btn_10.setText("")
        self.btn_21.setText("")
        self.btn_20.setText("")
        self.btn_22.setText("")
    # retranslateUi

