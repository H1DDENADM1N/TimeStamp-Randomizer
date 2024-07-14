# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'timestamp_randomizer.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QCheckBox, QGroupBox,
    QHBoxLayout, QPushButton, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(532, 482)
        icon = QIcon()
        icon.addFile(u"icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_select_folder = QPushButton(Form)
        self.pushButton_select_folder.setObjectName(u"pushButton_select_folder")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_select_folder.sizePolicy().hasHeightForWidth())
        self.pushButton_select_folder.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.pushButton_select_folder)

        self.pushButton_run = QPushButton(Form)
        self.pushButton_run.setObjectName(u"pushButton_run")
        sizePolicy.setHeightForWidth(self.pushButton_run.sizePolicy().hasHeightForWidth())
        self.pushButton_run.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.pushButton_run)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout = QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.checkBox_same_caw = QCheckBox(self.groupBox_2)
        self.checkBox_same_caw.setObjectName(u"checkBox_same_caw")

        self.verticalLayout.addWidget(self.checkBox_same_caw)

        self.checkBox_more_realistic = QCheckBox(self.groupBox_2)
        self.checkBox_more_realistic.setObjectName(u"checkBox_more_realistic")
        self.checkBox_more_realistic.setChecked(True)

        self.verticalLayout.addWidget(self.checkBox_more_realistic)


        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.textEdit_info = QTextEdit(self.groupBox)
        self.textEdit_info.setObjectName(u"textEdit_info")

        self.verticalLayout_3.addWidget(self.textEdit_info)


        self.verticalLayout_2.addWidget(self.groupBox)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"TimeStamp Randomizer", None))
        self.pushButton_select_folder.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u6587\u4ef6\u5939", None))
        self.pushButton_run.setText(QCoreApplication.translate("Form", u"\u968f\u673a\u5316\u65f6\u95f4\u6233", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"\u8bbe\u7f6e\uff1a", None))
        self.checkBox_same_caw.setText(QCoreApplication.translate("Form", u"\u521b\u5efa\u65f6\u95f4 == \u6700\u540e\u8bbf\u95ee\u65f6\u95f4 == \u6700\u540e\u4fee\u6539\u65f6\u95f4", None))
        self.checkBox_more_realistic.setText(QCoreApplication.translate("Form", u"\u521b\u5efa\u65f6\u95f4 <= \u6700\u540e\u4fee\u6539\u65f6\u95f4 <= \u6700\u540e\u8bbf\u95ee\u65f6\u95f4 <= \u5f53\u524d\u65f6\u95f4", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u4fe1\u606f\uff1a", None))
    # retranslateUi

