from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import Main as main_function
import config.Config as con #语言包，但是还没有被启用

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(373, 162)

        self.args=[]

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 161, 31))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(120, 110, 131, 41))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(20, 50, 341, 41))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(self.Button1Listern)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "快捷启动"))
        self.label.setText(_translate("Dialog", "输入您希望附加的参数"))
        self.pushButton.setText(_translate("Dialog", "确定"))

    def Button1Listern(self):
        inputer = self.lineEdit.text()
        args_out = self.args[1]
        main_function.run_it(args_out,inputer)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Dialog()
    ui.setupUi(MainWindow)
    ui.args= sys.argv
    MainWindow.show()
    sys.exit(app.exec_())
