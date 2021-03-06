# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/artem/Projects/School project/mainWindowDesign.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(19, 460, 761, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.previous_question_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.previous_question_button.setEnabled(False)
        self.previous_question_button.setObjectName("previous_question_button")
        self.horizontalLayout.addWidget(self.previous_question_button)
        self.next_question_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.next_question_button.setEnabled(False)
        self.next_question_button.setObjectName("next_question_button")
        self.horizontalLayout.addWidget(self.next_question_button)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(19, 9, 761, 441))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.question_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.question_label.setEnabled(False)
        self.question_label.setText("")
        self.question_label.setObjectName("question_label")
        self.verticalLayout.addWidget(self.question_label)
        self.answer_line_edit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.answer_line_edit.setEnabled(False)
        self.answer_line_edit.setObjectName("answer_line_edit")
        self.verticalLayout.addWidget(self.answer_line_edit)
        self.finish_test_button = QtWidgets.QPushButton(self.centralwidget)
        self.finish_test_button.setEnabled(False)
        self.finish_test_button.setGeometry(QtCore.QRect(679, 0, 111, 23))
        self.finish_test_button.setObjectName("finish_test_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.open_test_action = QtWidgets.QAction(MainWindow)
        self.open_test_action.setObjectName("open_test_action")
        self.menuFile.addAction(self.open_test_action)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "????????????????????????"))
        self.previous_question_button.setText(_translate("MainWindow", "???????????????????? ????????????"))
        self.next_question_button.setText(_translate("MainWindow", "?????????????????? ????????????"))
        self.finish_test_button.setText(_translate("MainWindow", "?????????????????? ????????"))
        self.menuFile.setTitle(_translate("MainWindow", "????????"))
        self.open_test_action.setText(_translate("MainWindow", "?????????????? ????????"))
        self.open_test_action.setShortcut(_translate("MainWindow", "Ctrl+O"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
