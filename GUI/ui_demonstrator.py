# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_demonstrator.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, QSize)
from PySide6.QtGui import (QIcon)
from PySide6.QtWidgets import (QComboBox, QLabel)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(720, 600)
        Dialog.setMinimumSize(QSize(720, 600))
        Dialog.setMaximumSize(QSize(720, 600))
        icon = QIcon()
        icon.addFile(u"Icons/icons8-graph-100.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(114, 0, 156, 255), stop:1 rgba(92, 255, 255, 255));\n"
"font: 12pt \"Franklin Gothic\";")
        self.choose_lib = QComboBox(Dialog)
        self.choose_lib.addItem("")
        self.choose_lib.addItem("")
        self.choose_lib.addItem("")
        self.choose_lib.setObjectName(u"choose_lib")
        self.choose_lib.setGeometry(QRect(10, 10, 341, 31))
        self.choose_lib.setStyleSheet(u"QComboBox {\n"
"background: qlineargradient(spread:pad, x1:0.511, y1:0, x2:0.517, y2:1, stop:0 rgba(0, 83, 166, 102), stop:1 rgba(0, 0, 71, 150));\n"
"color: rgb(255, 255, 255);\n"
"border-radius:7\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"background: qlineargradient(spread:pad, x1:0.511, y1:0, x2:0.517, y2:1, stop:0 rgba(0, 83, 166, 10), stop:1 rgba(0, 0, 71, 10));\n"
"selection-background-color: qlineargradient(spread:pad, x1:0.511, y1:0, x2:0.517, y2:1, stop:0 rgba(0, 83, 166, 10), stop:1 rgba(0, 0, 71, 10));\n"
"color: rgb(255, 255, 255);\n"
"border-radius:7\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"background: qlineargradient(spread:pad, x1:0.511, y1:0, x2:0.517, y2:1, stop:0 rgba(0, 83, 166, 102), stop:1 rgba(0, 0, 71, 255));\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"")
        self.choose_lib.setEditable(False)
        self.choose_lib.setDuplicatesEnabled(False)
        self.view = QLabel(Dialog)
        self.view.setObjectName(u"view")
        self.view.setEnabled(True)
        self.view.setGeometry(QRect(10, 50, 701, 541))
        self.view.setStyleSheet(u"background:qlineargradient(spread:pad, x1:0.511, y1:0, x2:0.517, y2:1, stop:0 rgba(0, 83, 166, 60), stop:1 rgba(0, 0, 71, 60));\n"
"border-radius:7")
        self.comboBox_2 = QComboBox(Dialog)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(370, 10, 341, 31))
        self.comboBox_2.setStyleSheet(u"QComboBox {\n"
"background: qlineargradient(spread:pad, x1:0.511, y1:0, x2:0.517, y2:1, stop:0 rgba(0, 83, 166, 102), stop:1 rgba(0, 0, 71, 150));\n"
"color: rgb(255, 255, 255);\n"
"border-radius:7\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"background: qlineargradient(spread:pad, x1:0.511, y1:0, x2:0.517, y2:1, stop:0 rgba(0, 83, 166, 10), stop:1 rgba(0, 0, 71, 10));\n"
"selection-background-color: qlineargradient(spread:pad, x1:0.511, y1:0, x2:0.517, y2:1, stop:0 rgba(0, 83, 166, 10), stop:1 rgba(0, 0, 71, 10));\n"
"color: rgb(255, 255, 255);\n"
"border-radius:7\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"background: qlineargradient(spread:pad, x1:0.511, y1:0, x2:0.517, y2:1, stop:0 rgba(0, 83, 166, 102), stop:1 rgba(0, 0, 71, 255));\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"")
        self.comboBox_2.setEditable(False)
        self.comboBox_2.setDuplicatesEnabled(False)

        self.retranslateUi(Dialog)

        self.choose_lib.setCurrentIndex(-1)
        self.comboBox_2.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u0414\u0435\u043c\u043e\u043d\u0441\u0442\u0440\u0430\u0442\u043e\u0440 \u0433\u0440\u0430\u0444\u0438\u043a\u043e\u0432", None))
        self.choose_lib.setItemText(0, QCoreApplication.translate("Dialog", u"Matplotlib", None))
        self.choose_lib.setItemText(1, QCoreApplication.translate("Dialog", u"Seaborn", None))
        self.choose_lib.setItemText(2, QCoreApplication.translate("Dialog", u"Plotly", None))

        self.choose_lib.setCurrentText("")
        self.choose_lib.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0431\u0438\u0431\u043b\u0438\u043e\u0442\u0435\u043a\u0443 \u0434\u043b\u044f \u0432\u0438\u0437\u0443\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u0438", None))
        self.view.setText("")
        self.comboBox_2.setCurrentText("")
        self.comboBox_2.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0432\u0438\u0434 \u0433\u0440\u0430\u0444\u0438\u043a\u0430", None))
    # retranslateUi

