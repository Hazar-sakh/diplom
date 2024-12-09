# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGraphicsView,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1126, 900)
        icon = QIcon()
        icon.addFile(u"icons8-graph-100.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(114, 0, 156, 255), stop:1 rgba(92, 255, 255, 255));\n"
"font: 12pt \"Franklin Gothic\";")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.browse_label = QLabel(self.centralwidget)
        self.browse_label.setObjectName(u"browse_label")
        self.browse_label.setGeometry(QRect(320, 49, 371, 31))
        self.browse_label.setStyleSheet(u"background: qlineargradient(spread:pad, x1:0.511, y1:0, x2:0.517, y2:1, stop:0 rgba(0, 83, 166, 102), stop:1 rgba(0, 0, 71, 150));\n"
"color: rgb(255, 255, 255);\n"
"border-radius:7")
        self.browse_label.setFrameShape(QFrame.Shape.StyledPanel)
        self.browse_label.setFrameShadow(QFrame.Shadow.Plain)
        self.browse_label.setTextFormat(Qt.TextFormat.AutoText)
        self.browse_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.browse = QPushButton(self.centralwidget)
        self.browse.setObjectName(u"browse")
        self.browse.setGeometry(QRect(700, 50, 121, 31))
        self.browse.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.browse.setStyleSheet(u"QPushButton {background: qlineargradient(spread:pad, x1:0.511, y1:0, x2:0.517, y2:1, stop:0 rgba(0, 83, 166, 102), stop:1 rgba(0, 0, 71, 255));\n"
"color: rgb(255, 255, 255);\n"
"border-radius:7\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: qlineargradient(spread:pad, x1:0.511, y1:0, x2:0.517, y2:1, stop:0 rgba(0, 83, 166, 100), stop:1 rgba(0, 0, 71, 100));\n"
"color: rgb(255, 255, 255);\n"
"border-radius:7\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background: qlineargradient(spread:pad, x1:0.511, y1:0, x2:0.517, y2:1, stop:0 rgba(0, 83, 166, 255), stop:1 rgba(0, 0, 71, 255));\n"
"color: rgb(255, 255, 255);\n"
"border-radius:7\n"
"}\n"
"\n"
"")
        self.browse.setFlat(False)
        self.select_type = QComboBox(self.centralwidget)
        self.select_type.setObjectName(u"select_type")
        self.select_type.setEnabled(True)
        self.select_type.setGeometry(QRect(320, 100, 501, 31))
        self.select_type.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.select_type.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.select_type.setToolTipDuration(-1)
        self.select_type.setStyleSheet(u"QComboBox {background: qlineargradient(spread:pad, x1:0.511, y1:0, x2:0.517, y2:1, stop:0 rgba(0, 83, 166, 102), stop:1 rgba(0, 0, 71, 255));\n"
"color: rgb(255, 255, 255);\n"
"border-radius:7\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"background: qlineargradient(spread:pad, x1:0.511, y1:0, x2:0.517, y2:1, stop:0 rgba(0, 83, 166, 100), stop:1 rgba(0, 0, 71, 100));\n"
"color: rgb(255, 255, 255);\n"
"border-radius:7\n"
"}\n"
"\n"
"QComboBox:pressed {\n"
"background: qlineargradient(spread:pad, x1:0.511, y1:0, x2:0.517, y2:1, stop:0 rgba(0, 83, 166, 255), stop:1 rgba(0, 0, 71, 255));\n"
"color: rgb(255, 255, 255);\n"
"border-radius:7\n"
"}\n"
"\n"
"")
        self.select_type.setEditable(True)
        self.select_type.setFrame(True)
        self.mpl_gra_h = QGraphicsView(self.centralwidget)
        self.mpl_gra_h.setObjectName(u"mpl_gra_h")
        self.mpl_gra_h.setGeometry(QRect(20, 580, 351, 271))
        self.mpl_gra_h.setStyleSheet(u"background:qlineargradient(spread:pad, x1:0.511, y1:0, x2:0.517, y2:1, stop:0 rgba(0, 83, 166, 102), stop:1 rgba(0, 0, 71, 255));\n"
"border-radius:7")
        self.mpl_gra_h.setFrameShape(QFrame.Shape.StyledPanel)
        self.mpl_gra_h.setFrameShadow(QFrame.Shadow.Sunken)
        self.mpl_gra_h.setLineWidth(0)
        self.mpl_gra_h.setMidLineWidth(0)
        self.mpl_gra_h.setInteractive(True)
        self.ptl_gra_h = QGraphicsView(self.centralwidget)
        self.ptl_gra_h.setObjectName(u"ptl_gra_h")
        self.ptl_gra_h.setGeometry(QRect(760, 580, 351, 271))
        self.ptl_gra_h.setStyleSheet(u"background:qlineargradient(spread:pad, x1:0.511, y1:0, x2:0.517, y2:1, stop:0 rgba(0, 83, 166, 102), stop:1 rgba(0, 0, 71, 255));\n"
"border-radius:7")
        self.sns_gra_h = QGraphicsView(self.centralwidget)
        self.sns_gra_h.setObjectName(u"sns_gra_h")
        self.sns_gra_h.setGeometry(QRect(390, 580, 351, 271))
        self.sns_gra_h.setStyleSheet(u"background:qlineargradient(spread:pad, x1:0.511, y1:0, x2:0.517, y2:1, stop:0 rgba(0, 83, 166, 102), stop:1 rgba(0, 0, 71, 255));\n"
"border-radius:7")
        self.mpl_gra_s = QGraphicsView(self.centralwidget)
        self.mpl_gra_s.setObjectName(u"mpl_gra_s")
        self.mpl_gra_s.setGeometry(QRect(20, 270, 351, 271))
        self.mpl_gra_s.setStyleSheet(u"background:qlineargradient(spread:pad, x1:0.511, y1:0, x2:0.517, y2:1, stop:0 rgba(0, 83, 166, 102), stop:1 rgba(0, 0, 71, 255));\n"
"border-radius:7")
        self.sns_gra_s = QGraphicsView(self.centralwidget)
        self.sns_gra_s.setObjectName(u"sns_gra_s")
        self.sns_gra_s.setGeometry(QRect(390, 270, 351, 271))
        self.sns_gra_s.setStyleSheet(u"background:qlineargradient(spread:pad, x1:0.511, y1:0, x2:0.517, y2:1, stop:0 rgba(0, 83, 166, 102), stop:1 rgba(0, 0, 71, 255));\n"
"border-radius:7")
        self.ptl_gra_s = QGraphicsView(self.centralwidget)
        self.ptl_gra_s.setObjectName(u"ptl_gra_s")
        self.ptl_gra_s.setGeometry(QRect(760, 270, 351, 271))
        self.ptl_gra_s.setStyleSheet(u"background:qlineargradient(spread:pad, x1:0.511, y1:0, x2:0.517, y2:1, stop:0 rgba(0, 83, 166, 102), stop:1 rgba(0, 0, 71, 255));\n"
"border-radius:7")
        self.t_mpl_s = QLabel(self.centralwidget)
        self.t_mpl_s.setObjectName(u"t_mpl_s")
        self.t_mpl_s.setGeometry(QRect(110, 550, 161, 16))
        self.t_mpl_s.setStyleSheet(u"background:qlineargradient(spread:pad, x1:0.511, y1:0, x2:0.517, y2:1, stop:0 rgba(0, 83, 166, 102), stop:1 rgba(0, 0, 71, 255));\n"
"color:rgb(255, 255, 255);\n"
"border-radius:7")
        self.t_mpl_s.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.t_mpl_h = QLabel(self.centralwidget)
        self.t_mpl_h.setObjectName(u"t_mpl_h")
        self.t_mpl_h.setGeometry(QRect(110, 860, 161, 16))
        self.t_mpl_h.setStyleSheet(u"background:qlineargradient(spread:pad, x1:0.511, y1:0, x2:0.517, y2:1, stop:0 rgba(0, 83, 166, 102), stop:1 rgba(0, 0, 71, 255));\n"
"color:rgb(255, 255, 255);\n"
"border-radius:7")
        self.t_mpl_h.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.t_sns_s = QLabel(self.centralwidget)
        self.t_sns_s.setObjectName(u"t_sns_s")
        self.t_sns_s.setGeometry(QRect(490, 550, 161, 16))
        self.t_sns_s.setStyleSheet(u"background:qlineargradient(spread:pad, x1:0.511, y1:0, x2:0.517, y2:1, stop:0 rgba(0, 83, 166, 102), stop:1 rgba(0, 0, 71, 255));\n"
"color:rgb(255, 255, 255);\n"
"border-radius:7")
        self.t_sns_s.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.t_sns_h = QLabel(self.centralwidget)
        self.t_sns_h.setObjectName(u"t_sns_h")
        self.t_sns_h.setGeometry(QRect(490, 860, 161, 16))
        self.t_sns_h.setStyleSheet(u"background:qlineargradient(spread:pad, x1:0.511, y1:0, x2:0.517, y2:1, stop:0 rgba(0, 83, 166, 102), stop:1 rgba(0, 0, 71, 255));\n"
"color:rgb(255, 255, 255);\n"
"border-radius:7")
        self.t_sns_h.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.t_ptl_s = QLabel(self.centralwidget)
        self.t_ptl_s.setObjectName(u"t_ptl_s")
        self.t_ptl_s.setGeometry(QRect(860, 550, 161, 16))
        self.t_ptl_s.setStyleSheet(u"background:qlineargradient(spread:pad, x1:0.511, y1:0, x2:0.517, y2:1, stop:0 rgba(0, 83, 166, 102), stop:1 rgba(0, 0, 71, 255));\n"
"color:rgb(255, 255, 255);\n"
"border-radius:7")
        self.t_ptl_s.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.t_ptl_h = QLabel(self.centralwidget)
        self.t_ptl_h.setObjectName(u"t_ptl_h")
        self.t_ptl_h.setGeometry(QRect(860, 860, 161, 16))
        self.t_ptl_h.setStyleSheet(u"background:qlineargradient(spread:pad, x1:0.511, y1:0, x2:0.517, y2:1, stop:0 rgba(0, 83, 166, 102), stop:1 rgba(0, 0, 71, 255));\n"
"color:rgb(255, 255, 255);\n"
"border-radius:7")
        self.t_ptl_h.setAlignment(Qt.AlignmentFlag.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.browse.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0437\u0443\u0430\u043b\u0438\u0437\u0430\u0442\u043e\u0440 \u0442\u0430\u0431\u043b\u0438\u0446", None))
        self.browse_label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0444\u0430\u0439\u043b \u0434\u043b\u044f \u0432\u0438\u0437\u0443\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u0438", None))
        self.browse.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c", None))
#if QT_CONFIG(tooltip)
        self.select_type.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.select_type.setCurrentText("")
        self.select_type.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044e \u0434\u043b\u044f \u0432\u0438\u0437\u0443\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u0438", None))
        self.t_mpl_s.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0430\u0439\u043c\u0438\u043d\u0433", None))
        self.t_mpl_h.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0430\u0439\u043c\u0438\u043d\u0433", None))
        self.t_sns_s.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0430\u0439\u043c\u0438\u043d\u0433", None))
        self.t_sns_h.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0430\u0439\u043c\u0438\u043d\u0433", None))
        self.t_ptl_s.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0430\u0439\u043c\u0438\u043d\u0433", None))
        self.t_ptl_h.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0430\u0439\u043c\u0438\u043d\u0433", None))
    # retranslateUi

