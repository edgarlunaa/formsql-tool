# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\edgar\Documents\Python programs\formsql-tool\Window.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(776, 592)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(776, 592))
        MainWindow.setMaximumSize(QtCore.QSize(776, 592))
        MainWindow.setStyleSheet("/* From uiverse.io by @adamgiebl */\n"
"QMainWindow {\n"
"    background: rgb(211, 211, 211);\n"
"}\n"
"\n"
"/* From uiverse.io by @alexruix */\n"
".QComboBox {\n"
"    line-height: 28px;\n"
"    border: 2px solid transparent;\n"
"    border-bottom-color: #777;\n"
"    padding: .2rem 0;\n"
"    outline: none;\n"
"    background-color: transparent;\n"
"    color: #0d0c22;\n"
"}\n"
"\n"
".QComboBox:focus, QComboBox:hover {\n"
"    outline: none;\n"
"    padding: .2rem 1rem;\n"
"    border-radius: 1rem;\n"
"    border-color: #7a9cc6;\n"
"}\n"
"\n"
".QLineEdit {\n"
"    line-height: 28px;\n"
"    border: 2px solid transparent;\n"
"    border-bottom-color: #777;\n"
"    padding: .2rem 0;\n"
"    outline: none;\n"
"    background-color: transparent;\n"
"    color: #0d0c22;\n"
"}\n"
"\n"
".QLineEdit:focus, QLineEdit:hover {\n"
"    outline: none;\n"
"    padding: .2rem 1rem;\n"
"    border-radius: 1rem;\n"
"    border-color: #7a9cc6;\n"
"}\n"
"\n"
".QLineEdit::placeholder {\n"
"    color: #777;\n"
"}\n"
"\n"
".QLineEdit:focus::placeholder {\n"
"    opacity: 0;\n"
"}\n"
"\n"
"QPushButton {\n"
"    color: #090909;\n"
"    border-radius: 0.1em;\n"
"    background: #e8e8e8;\n"
"   }\n"
"   \n"
"   QPushButton:hover {\n"
"    border: 1px solid white;\n"
"   }\n"
"   \n"
" QPushButton:pressed {\n"
"    background: rgb(218, 218, 218);\n"
" }")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(16, 12, 80, 16))
        self.label.setObjectName("label")
        self.cb_TOF = QtWidgets.QComboBox(self.centralwidget)
        self.cb_TOF.setGeometry(QtCore.QRect(110, 10, 140, 22))
        self.cb_TOF.setObjectName("cb_TOF")
        self.cb_TOF.addItem("")
        self.cb_TOF.addItem("")
        self.cb_TOF.addItem("")
        self.txt_Variable = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_Variable.setGeometry(QtCore.QRect(110, 34, 211, 22))
        self.txt_Variable.setObjectName("txt_Variable")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(17, 37, 100, 16))
        self.label_2.setObjectName("label_2")
        self.btn_Generate = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Generate.setGeometry(QtCore.QRect(628, 10, 138, 40))
        self.btn_Generate.setObjectName("btn_Generate")
        self.lst_Elements = QtWidgets.QListWidget(self.centralwidget)
        self.lst_Elements.setGeometry(QtCore.QRect(16, 106, 256, 431))
        self.lst_Elements.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.lst_Elements.setDragEnabled(False)
        self.lst_Elements.setObjectName("lst_Elements")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(16, 62, 150, 16))
        self.label_3.setObjectName("label_3")
        self.txt_Code = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txt_Code.setGeometry(QtCore.QRect(476, 82, 291, 479))
        self.txt_Code.setObjectName("txt_Code")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(476, 62, 55, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(276, 62, 110, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(336, 12, 71, 16))
        self.label_6.setObjectName("label_6")
        self.cb_TODD = QtWidgets.QComboBox(self.centralwidget)
        self.cb_TODD.setGeometry(QtCore.QRect(406, 10, 151, 22))
        self.cb_TODD.setObjectName("cb_TODD")
        self.cb_TODD.addItem("")
        self.cb_TODD.addItem("")
        self.cb_TODD.addItem("")
        self.txt_FEO = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txt_FEO.setGeometry(QtCore.QRect(276, 82, 195, 480))
        self.txt_FEO.setObjectName("txt_FEO")
        self.btn_Copy1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Copy1.setGeometry(QtCore.QRect(378, 52, 93, 28))
        self.btn_Copy1.setObjectName("btn_Copy1")
        self.btn_Copy2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Copy2.setGeometry(QtCore.QRect(673, 52, 93, 28))
        self.btn_Copy2.setObjectName("btn_Copy2")
        self.txt_Element = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_Element.setGeometry(QtCore.QRect(16, 82, 256, 22))
        self.txt_Element.setObjectName("txt_Element")
        self.btn_Empty = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Empty.setGeometry(QtCore.QRect(190, 540, 81, 20))
        self.btn_Empty.setObjectName("btn_Empty")
        self.btn_Eliminate = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Eliminate.setGeometry(QtCore.QRect(90, 540, 97, 20))
        self.btn_Eliminate.setObjectName("btn_Eliminate")
        self.btn_Edit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Edit.setGeometry(QtCore.QRect(17, 540, 69, 20))
        self.btn_Edit.setObjectName("btn_Edit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.btn_Copy2.clicked.connect(self.txt_Code.selectAll)
        self.btn_Copy2.clicked.connect(self.txt_Code.copy)
        self.btn_Copy2.clicked.connect(self.txt_Code.paste)
        self.btn_Copy1.clicked.connect(self.txt_FEO.selectAll)
        self.btn_Copy1.clicked.connect(self.txt_FEO.copy)
        self.btn_Copy1.clicked.connect(self.txt_FEO.paste)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.cb_TOF, self.cb_TODD)
        MainWindow.setTabOrder(self.cb_TODD, self.txt_Variable)
        MainWindow.setTabOrder(self.txt_Variable, self.txt_Element)
        MainWindow.setTabOrder(self.txt_Element, self.btn_Generate)
        MainWindow.setTabOrder(self.btn_Generate, self.txt_FEO)
        MainWindow.setTabOrder(self.txt_FEO, self.btn_Copy1)
        MainWindow.setTabOrder(self.btn_Copy1, self.btn_Copy2)
        MainWindow.setTabOrder(self.btn_Copy2, self.txt_Code)
        MainWindow.setTabOrder(self.txt_Code, self.lst_Elements)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FormSQL-Tool"))
        self.label.setText(_translate("MainWindow", "Type of field:"))
        self.cb_TOF.setItemText(0, _translate("MainWindow", "Dropdown"))
        self.cb_TOF.setItemText(1, _translate("MainWindow", "Checkbox"))
        self.cb_TOF.setItemText(2, _translate("MainWindow", "Date"))
        self.label_2.setText(_translate("MainWindow", "Variable Name:"))
        self.btn_Generate.setText(_translate("MainWindow", "Generate"))
        self.label_3.setText(_translate("MainWindow", "Add element to the list:"))
        self.label_4.setText(_translate("MainWindow", "Code"))
        self.label_5.setText(_translate("MainWindow", "Form edit options"))
        self.label_6.setText(_translate("MainWindow", "Type of DD:"))
        self.cb_TODD.setItemText(0, _translate("MainWindow", "Yes/No"))
        self.cb_TODD.setItemText(1, _translate("MainWindow", "Element to Checkbox"))
        self.cb_TODD.setItemText(2, _translate("MainWindow", "Element to Text"))
        self.btn_Copy1.setText(_translate("MainWindow", "Copy"))
        self.btn_Copy2.setText(_translate("MainWindow", "Copy"))
        self.btn_Empty.setText(_translate("MainWindow", "Empty"))
        self.btn_Eliminate.setText(_translate("MainWindow", "Eliminate"))
        self.btn_Edit.setText(_translate("MainWindow", "Edit"))
