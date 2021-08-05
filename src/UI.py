#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File : UI.py
@Note : 界面UI部分,Qt Designer懒人生成,自己再修修补补
'''

from PyQt5 import QtCore, QtGui, QtWidgets
from Plan import Plan

class UI_Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, Window):
        Window.setObjectName("Window")
        Window.resize(400, 300)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Window)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(Window)
        self.tabWidget.setObjectName("tabWidget")
        # -------------------Tab1-------------------#
        self.tab = QtWidgets.QWidget()
        # self.tab.setStyleSheet('background-color:#37474F')
        self.tab.setObjectName("tab")
        self.layoutVP1 = QtWidgets.QVBoxLayout(self.tab)
        self.layoutVP1.setObjectName("layoutVP1")
        self.textBrowser_feedback = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser_feedback.setEnabled(True)
        self.textBrowser_feedback.setMinimumSize(QtCore.QSize(0, 205))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser_feedback.setFont(font)
        self.textBrowser_feedback.setObjectName("textBrowser_feedback")
        self.layoutVP1.addWidget(self.textBrowser_feedback)
        self.layoutHP1 = QtWidgets.QHBoxLayout()
        self.layoutHP1.setObjectName("layoutHP1")
        self.comboBox_plan = QtWidgets.QComboBox(self.tab)
        self.comboBox_plan.setMaximumSize(QtCore.QSize(100, 30))
        self.comboBox_plan.setObjectName("comboBox_plan")

        self.layoutHP1.addWidget(self.comboBox_plan)
        self.textEdit_time = QtWidgets.QTextEdit(self.tab)
        self.textEdit_time.setMaximumSize(QtCore.QSize(40, 30))
        self.textEdit_time.setObjectName("textEdit_time")
        self.textEdit_time.setAlignment(QtCore.Qt.AlignHCenter)

        self.layoutHP1.addWidget(self.textEdit_time)
        self.label_unit = QtWidgets.QLabel(self.tab)
        self.label_unit.setMaximumSize(QtCore.QSize(20, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_unit.setFont(font)
        self.label_unit.setObjectName("label_unit")
        self.layoutHP1.addWidget(self.label_unit)
        self.startBtn = QtWidgets.QPushButton(self.tab)
        self.startBtn.setMinimumSize(QtCore.QSize(0, 30))
        self.startBtn.setObjectName("startBtn")
        self.layoutHP1.addWidget(self.startBtn)
        self.stopBtn = QtWidgets.QPushButton(self.tab)
        self.stopBtn.setMinimumSize(QtCore.QSize(0, 30))
        self.stopBtn.setObjectName("stopBtn")
        self.layoutHP1.addWidget(self.stopBtn)
        self.layoutVP1.addLayout(self.layoutHP1)
        self.tabWidget.addTab(self.tab, "")
        # -------------------Tab2-------------------#
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_headP2 = QtWidgets.QWidget(self.tab_2)
        self.widget_headP2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.widget_headP2.setObjectName("widget_headP2")
        self.layoutHP2 = QtWidgets.QHBoxLayout(self.widget_headP2)
        self.layoutHP2.setContentsMargins(0, 0, 0, 0)
        self.layoutHP2.setObjectName("layoutHP2")
        self.label_P2 = QtWidgets.QLabel(self.widget_headP2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_P2.sizePolicy().hasHeightForWidth())
        self.label_P2.setSizePolicy(sizePolicy)
        self.label_P2.setMinimumSize(QtCore.QSize(0, 30))
        self.label_P2.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_P2.setFont(font)
        self.label_P2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_P2.setObjectName("label_P2")
        self.layoutHP2.addWidget(self.label_P2)
        self.addBtn = QtWidgets.QPushButton(self.widget_headP2)
        self.addBtn.setMinimumSize(QtCore.QSize(99, 30))
        self.addBtn.setMaximumSize(QtCore.QSize(99, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.addBtn.setFont(font)
        self.addBtn.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.addBtn.setObjectName("addBtn")
        self.layoutHP2.addWidget(self.addBtn)
        self.verticalLayout_2.addWidget(self.widget_headP2, 0, QtCore.Qt.AlignTop)
        self.layoutVP2 = QtWidgets.QVBoxLayout()
        self.layoutVP2.setObjectName("layoutVP2")
        # self.layoutVP2.setAlignment(QtCore.Qt.AlignBottom)
        self.layoutVP2.addStretch(1)
        self.verticalLayout_2.addLayout(self.layoutVP2)
        self.tabWidget.addTab(self.tab_2, "")
        #-------------------Tab3-------------------#
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_headP3 = QtWidgets.QWidget(self.tab_3)
        self.widget_headP3.setMaximumSize(QtCore.QSize(16777215, 30))
        self.widget_headP3.setObjectName("widget_headP3")
        self.layoutHP3_1 = QtWidgets.QHBoxLayout(self.widget_headP3)
        self.layoutHP3_1.setContentsMargins(0, 0, 0, 0)
        self.layoutHP3_1.setObjectName("layoutHP3_1")
        self.lineEdit_path = QtWidgets.QLineEdit(self.widget_headP3)
        self.lineEdit_path.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_path.setObjectName("lineEdit_path")
        self.layoutHP3_1.addWidget(self.lineEdit_path)
        self.savePathBtn = QtWidgets.QPushButton(self.widget_headP3)
        self.savePathBtn.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.savePathBtn.setFont(font)
        self.savePathBtn.setObjectName("savePathBtn")
        self.layoutHP3_1.addWidget(self.savePathBtn)
        self.verticalLayout_3.addWidget(self.widget_headP3)
        self.label_image = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_image.setFont(font)
        self.label_image.setAlignment(QtCore.Qt.AlignCenter)
        self.label_image.setObjectName("label_image")
        self.verticalLayout_3.addWidget(self.label_image)
        self.widget_footP3 = QtWidgets.QWidget(self.tab_3)
        self.widget_footP3.setMaximumSize(QtCore.QSize(16777215, 30))
        self.widget_footP3.setObjectName("widget_footP3")
        self.layoutHP3_2 = QtWidgets.QHBoxLayout(self.widget_footP3)
        self.layoutHP3_2.setContentsMargins(0, 0, 0, 0)
        self.layoutHP3_2.setObjectName("layoutHP3_2")
        self.screenshotBtn = QtWidgets.QPushButton(self.widget_footP3)
        self.screenshotBtn.setMaximumSize(QtCore.QSize(99, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.screenshotBtn.setFont(font)
        self.screenshotBtn.setObjectName("screenshotBtn")
        self.layoutHP3_2.addWidget(self.screenshotBtn)
        self.deleteBtn = QtWidgets.QPushButton(self.widget_footP3)
        self.deleteBtn.setMaximumSize(QtCore.QSize(99, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.deleteBtn.setFont(font)
        self.deleteBtn.setObjectName("deleteBtn")
        self.layoutHP3_2.addWidget(self.deleteBtn)
        self.verticalLayout_3.addWidget(self.widget_footP3)
        self.tabWidget.addTab(self.tab_3, "")
        # -------------------Tab4-------------------#
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_instruction = QtWidgets.QLabel(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_instruction.setFont(font)
        self.label_instruction.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_instruction.setObjectName("label_instruction")
        self.label_instruction.setWordWrap(True)
        self.verticalLayout_4.addWidget(self.label_instruction)
        self.tabWidget.addTab(self.tab_4, "")
        self.horizontalLayout.addWidget(self.tabWidget)

        self.retranslateUi(Window)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Window)
        Window.show()

    def retranslateUi(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "On-Hook"))
        self.label_unit.setText(_translate("Window", "次"))
        self.startBtn.setText(_translate("Window", "开始挂机"))
        self.stopBtn.setText(_translate("Window", "停止"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Window", "挂机"))
        self.label_P2.setText(_translate("Window", "已保存挂机方案："))
        self.addBtn.setText(_translate("Window", "添加新方案"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Window", "定制挂机方案"))
        self.savePathBtn.setText(_translate("Window", "截图保存路径"))
        self.label_image.setText(_translate("Window", "显示截取的图片"))
        self.screenshotBtn.setText(_translate("Window", "截图"))
        self.deleteBtn.setText(_translate("Window", "删除该截图"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Window", "截图小工具"))
        self.label_instruction.setText(_translate("Window", '''使用说明：\n只完成了tab1和tab2的功能\nemmmm太臃肿了决定换个dev
        '''))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Window", "说明书"))






