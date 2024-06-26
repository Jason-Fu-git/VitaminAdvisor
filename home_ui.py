# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from dialog_ui import Ui_Dialog
import json


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(2013, 1214)
        MainWindow.setStyleSheet("background-color : white ;\n"
                                 "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 489, 1101))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setStyleSheet("background-color:transparent;border:none;")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(50)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.title_lbl = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("KaiTi")
        font.setPointSize(30) #标题
        self.title_lbl.setFont(font)
        self.title_lbl.setStyleSheet("color:#707070")
        self.title_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.title_lbl.setObjectName("title_lbl")
        self.verticalLayout_2.addWidget(self.title_lbl)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.textArea_frm = QtWidgets.QFrame(self.centralwidget)
        self.textArea_frm.setStyleSheet("border-radius: 100px;")
        self.textArea_frm.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.textArea_frm.setFrameShadow(QtWidgets.QFrame.Raised)
        self.textArea_frm.setObjectName("textArea_frm")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.textArea_frm)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.textEdit = QtWidgets.QTextEdit(self.textArea_frm)
        font = QtGui.QFont()
        font.setFamily("KaiTi")#症状输入栏
        font.setPointSize(14)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("QTextEdit {\n"
                                    "                border-radius: 30px;\n"
                                    "                background-clip: border;\n"
                                    "                background-color: white;\n"
                                    "                border: 3px solid;\n"
                                    "                border-color: #707070;\n"
                                    "                padding-right:20px;\n"
                                    "                padding-left:20px;\n"
                                    "                padding-top:10px;\n"
                                    "            }"
                                    "QTextEdit:focus {\n"
                                    "border-color: #909090;\n"
                                    "border: 5px solid;\n"
                                    "}\n")
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_3.addWidget(self.textEdit)
        self.horizontalLayout_2.addWidget(self.textArea_frm)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 10)
        self.horizontalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.submit_btn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("KaiTi")
        font.setPointSize(23)#提交按钮
        self.submit_btn.setFont(font)
        self.submit_btn.setStyleSheet("QPushButton{\n"
                                      "background-color : #007000;\n"
                                      "border-radius : 15px;\n"
                                      "height : 60px;\n"
                                      "color : white ;\n"
                                      "}\n"
                                      "QPushButton:pressed{\n"
                                      "background-color : #009000;\n"
                                      "}")
        self.submit_btn.setObjectName("submit_btn")
        self.horizontalLayout_3.addWidget(self.submit_btn)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 2)
        self.horizontalLayout_3.setStretch(2, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem5)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 2013, 38))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # ====== CUSTOMIZED WIDGETS ARE DEFINED HERE =======
        # add scroll bar to the scroll area
        self.verticalScrollBar = QtWidgets.QScrollBar(self.scrollArea)
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.verticalScrollBar.setStyleSheet(open("styles/vscrollbar_style.qss", "r").read())
        self.scrollArea.setVerticalScrollBar(self.verticalScrollBar)
        self.horizontalScrollBar = QtWidgets.QScrollBar(self.scrollArea)
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.horizontalScrollBar.setStyleSheet(open("styles/hscrollbar_style.qss", "r").read())
        self.scrollArea.setHorizontalScrollBar(self.horizontalScrollBar)
        # add scroll bar to the text edit
        self.verticalScrollBar2 = QtWidgets.QScrollBar(self.textEdit)
        self.verticalScrollBar2.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar2.setObjectName("verticalScrollBar2")
        self.verticalScrollBar2.setStyleSheet(open("styles/vscrollbar_style.qss", "r").read())
        self.textEdit.setVerticalScrollBar(self.verticalScrollBar2)
        # add category labels to the scroll area
        self.addCategoryWidgets()
        # link pushbutton to dialog
        self.submit_btn.clicked.connect(self.submit)
        # ======= CUSTOMIZED WIDGETS ARE DEFINED HERE ========

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def addCategoryWidgets(self):
        """
        add category labels and checkboxes to the scroll area
        """
        self.cbox_ls = []
        category_dic = json.load(open("json/symptom_class.json", "r", encoding="utf-8", errors='ignore'))
        for category, symptoms in category_dic.items():
            # add a corresponding label for each category
            category_lbl = QtWidgets.QLabel(self.scrollAreaWidgetContents)
            category_lbl.setMinimumSize(QtCore.QSize(0, 80))
            category_lbl.setMaximumSize(QtCore.QSize(16777215, 80))
            font = QtGui.QFont()
            font.setFamily("KaiTi")
            font.setPointSize(20)#选项标题的大小
            category_lbl.setFont(font)
            category_lbl.setStyleSheet("background-color : #007000;\n"
                                       "height : 70 px;\n"
                                       "color : white;\n"
                                       "padding-left : 20px;")
            category_lbl.setText(category)
            self.verticalLayout.addWidget(category_lbl)
            # initialize a frame
            category_frm = QtWidgets.QFrame(self.scrollAreaWidgetContents)
            category_frm.setFrameShape(QtWidgets.QFrame.StyledPanel)
            # initialize gridLayout
            gridLayout = QtWidgets.QGridLayout(category_frm)
            # add corresponding checkboxes
            for index, symptom in enumerate(symptoms):
                symptom_cbox = QtWidgets.QCheckBox(category_frm)
                symptom_cbox.setText(symptom)
                symptom_cbox.setStyleSheet("")
                font.setFamily("KaiTi")
                font.setPointSize(13)  # 选项的大小
                symptom_cbox.setFont(font)
                symptom_cbox.clicked.connect(self.checkboxChecked)
                gridLayout.addWidget(symptom_cbox, index // 2, index % 2, 1, 1)
                self.cbox_ls.append(symptom_cbox)
            self.verticalLayout.addWidget(category_frm)

    def checkboxChecked(self):
        symptom_text = ""
        for symptom_cbox in self.cbox_ls:
            if symptom_cbox.isChecked():
                symptom_text += f"{symptom_cbox.text()}；"
        self.textEdit.setText(symptom_text)

    def submit(self):
        # split the textEdit content by "；"
        submit_txt = self.textEdit.toPlainText()
        # pop up a dialog
        dialog = QtWidgets.QDialog(self.centralwidget)
        dialog_ui = Ui_Dialog(submit_txt)
        dialog_ui.setupUi(dialog)
        dialog.exec_()
        dialog.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "维生素缺乏症状自测系统"))
        MainWindow.setWindowIcon(QtGui.QIcon("icons/icon.png"))
        self.title_lbl.setText(_translate("MainWindow", "维生素缺乏症状自测"))
        self.textEdit.setPlaceholderText(_translate("MainWindow",
                                                    "请输入您的症状，或从左侧列表选择，症状之间用分号分隔。例：夜盲症；失眠。"))
        self.submit_btn.setText(_translate("MainWindow", "提      交"))
