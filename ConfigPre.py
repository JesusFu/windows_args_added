# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ConfigPre.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import Main as main_function

class treeNode():
    NodeType = ''
    Nodes = QtWidgets.QTreeWidgetItem()
    Name = ""
    ListNum = ""
    Icon = ""
    Command = ""


    def setup(self,type,name,nodes,icon,command,listnum):
        self.NodeType = type
        self.Name = name
        self.Nodes = nodes
        self.Command = command
        self.Icon = icon
        self.ListNum = listnum

    def setupRoot(self,type,name,listnum,nodes,icon):
        self.NodeType = type
        self.Name = name
        self.ListNum=listnum
        self.Nodes = nodes
        self.Icon = icon

class Ui_MainWindow(QtWidgets.QWidget):
    FROM, SUBJECT, DATE = range(3)
    treeNode = []
    CurrentType = 0
    treeSelect = ''
    listCount = 0
    treeSelect_2 = ''

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(880, 562)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(360, 60, 491, 331))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(370, 10, 181, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.setGeometry(QtCore.QRect(510, 420, 181, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")

        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(110, 55, 361, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setEnabled(False)
        self.label.setGeometry(QtCore.QRect(10, 50, 131, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 110, 361, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setEnabled(False)
        self.label_3.setGeometry(QtCore.QRect(10, 105, 131, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setEnabled(False)
        self.label_4.setGeometry(QtCore.QRect(10, 160, 131, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_3.setGeometry(QtCore.QRect(110, 165, 361, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setEnabled(False)
        self.pushButton.setGeometry(QtCore.QRect(150, 205, 181, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(20, 60, 331, 451))
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.setColumnCount(2)
        self.treeWidget.setHeaderLabels(['名称','类型'])
        self.treeWidget.setColumnWidth(0,200)
        self.treeWidget.setColumnWidth(1, 100)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 200, 181, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_5.setEnabled(True)
        self.lineEdit_5.setGeometry(QtCore.QRect(110, 90, 361, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_6.setEnabled(True)
        self.lineEdit_6.setGeometry(QtCore.QRect(110, 145, 361, 31))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setEnabled(True)
        self.label_6.setGeometry(QtCore.QRect(10, 85, 131, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setEnabled(True)
        self.label_7.setGeometry(QtCore.QRect(10, 140, 131, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.tabWidget.addTab(self.tab_2, "")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.treeWidget.clicked['QModelIndex'].connect(self.treeClick)
        self.pushButton.clicked.connect(self.Button1Listern)
        self.pushButton_2.clicked.connect(self.Button1Listern_2)
        self.pushButton_3.clicked.connect(self.Button1Listern_3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.treeInit()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "快捷启动配置器"))
        self.label_2.setText(_translate("MainWindow", "编辑配置菜单"))
        self.label.setText(_translate("MainWindow", "配置名称"))
        self.label_3.setText(_translate("MainWindow", "配置参数"))
        self.label_4.setText(_translate("MainWindow", "图标参数"))
        self.pushButton.setText(_translate("MainWindow", "没有选择"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "启动项编辑"))
        self.pushButton_2.setText(_translate("MainWindow", "新建目录"))
        self.label_6.setText(_translate("MainWindow", "目录名称"))
        self.label_7.setText(_translate("MainWindow", "图标参数"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "菜单编辑"))
        self.pushButton_3.setText(_translate("MainWindow", "删除启动项"))

    def createMailModel(self,parent):
        model =  QtGui.QStandardItemModel(0, 3, parent)
        model.setHeaderData(self.FROM,QtCore.Qt.Horizontal, "图标")
        model.setHeaderData(self.SUBJECT,QtCore. Qt.Horizontal, "标题")
        model.setHeaderData(self.DATE,QtCore. Qt.Horizontal, "参数")
        return model

    def addMail(self,model, mailFrom, subject, date):
        model.insertRow(0)
        model.setData(model.index(0, self.FROM), mailFrom)
        model.setData(model.index(0, self.SUBJECT), subject)
        model.setData(model.index(0, self.DATE), date)

    def Button1Listern_3(self):
        if self.CurrentType == 1 :
            if main_function.delete_key(self.treeSelect) == 0:
                reply = QtWidgets.QMessageBox.information( self,'删除成功', '目录已经被删除',
                                                       QtWidgets.QMessageBox.Yes, )
                self.treeWidget.clear()
                self.treeInit()
                self.listCount -= 1
            else:
                reply = QtWidgets.QMessageBox.warning( self,'未知错误', '未知错误导致删除失败，可能是缺乏权限导致的',
                                                       QtWidgets.QMessageBox.Yes, )
        elif self.CurrentType == 2 :
            if self.treeSelect != 'BASIC':
                if main_function.delete_key(self.treeSelect+"\\Shell\\"+self.treeSelect_2) == 0:
                    reply = QtWidgets.QMessageBox.information( self,'删除成功', '预设已经被删除',
                                                       QtWidgets.QMessageBox.Yes, )
                    self.treeWidget.clear()
                    self.treeInit()

                else:
                    reply = QtWidgets.QMessageBox.warning( self,'未知错误', '未知错误导致删除失败，可能是缺乏权限导致的',
                                                       QtWidgets.QMessageBox.Yes, )
            else:
                if main_function.delete_key(self.treeSelect_2) == 0:
                    reply = QtWidgets.QMessageBox.information( self,'删除成功', '预设已经被删除',
                                                       QtWidgets.QMessageBox.Yes, )
                    self.treeWidget.clear()
                    self.treeInit()

                else:
                    reply = QtWidgets.QMessageBox.warning( self,'未知错误', '未知错误导致删除失败，可能是缺乏权限导致的',
                                                       QtWidgets.QMessageBox.Yes, )

    def Button1Listern_2(self):
        Names = self.lineEdit_5.text()
        Icons = self.lineEdit_6.text()
        if self.lineEdit_5.text()!="":
            if main_function.submains_register_in_shell(self.listCount+1,Names,Icons) == 0:
                reply = QtWidgets.QMessageBox.information( self,'创建成功', '新的目录已经得到定义',
                                                       QtWidgets.QMessageBox.Yes, )
                self.treeWidget.clear()
                self.treeInit()
                self.listCount+=1

            else:
                reply = QtWidgets.QMessageBox.warning( self,'未知错误', '未知错误导致创建失败，可能是缺乏权限导致的',
                                                       QtWidgets.QMessageBox.Yes, )
        else:
                reply = QtWidgets.QMessageBox.warning( self,'参数错误！', '参数输入不能为空',
                                                       QtWidgets.QMessageBox.Yes, )

    def Button1Listern(self):
        if self.CurrentType == 1 :
            if self.lineEdit.text()!="" and self.lineEdit_2.text()!="":
                posG = self.treeSelect
                namesG = self.lineEdit.text()
                commandG = self.lineEdit_2.text()
                iconG = self.lineEdit_3.text()
                print(posG,namesG,commandG,iconG)
                if main_function.Key_register_in_shell(posG,namesG,commandG,iconG) == 0:
                    reply = QtWidgets.QMessageBox.information( self,'创建成功', '新的项目已经得到定义',
                                                       QtWidgets.QMessageBox.Yes, )
                    self.treeWidget.clear()
                    self.treeInit()

                else:
                    reply = QtWidgets.QMessageBox.warning( self,'未知错误', '未知错误导致创建失败，可能是缺乏权限导致的',
                                                       QtWidgets.QMessageBox.Yes, )

            else:
                try:
                    reply = QtWidgets.QMessageBox.warning( self,'参数错误！', '参数输入不能为空',
                                                       QtWidgets.QMessageBox.Yes, )
                except Exception as e:
                    print(str(e))
        elif self.CurrentType == 2 :
            if self.lineEdit.text()!="" and self.lineEdit_2.text()!="":
                posG = self.treeSelect
                namesG = self.lineEdit.text()
                commandG = self.lineEdit_2.text()
                iconG = self.lineEdit_3.text()
                if main_function.Key_register_in_shell(posG,namesG,commandG,iconG) == 0:
                    reply = QtWidgets.QMessageBox.information( self,'保存成功', '预设的修改已经保存',
                                                       QtWidgets.QMessageBox.Yes, )
                    self.treeWidget.clear()
                    self.treeNode = []
                    self.treeInit()

                else:
                    reply = QtWidgets.QMessageBox.warning( self,'未知错误', '未知错误导致修改失败，可能是缺乏权限导致的',
                                                       QtWidgets.QMessageBox.Yes, )

            else:
                try:
                    reply = QtWidgets.QMessageBox.warning( self,'参数错误！', '参数输入不能为空',
                                                       QtWidgets.QMessageBox.Yes, )
                except Exception as e:
                    print(str(e))

    def treeInit(self):
        self.addTreeRoot()

    def treeClick(self,qmodelindex):
        item = self.treeWidget.currentItem()
        if item.text(1) == "菜单" :
            self.CurrentType = 1
            self.lineEdit.setEnabled(True)
            self.lineEdit_2.setEnabled(True)
            self.lineEdit_3.setEnabled(True)
            self.label.setEnabled(True)
            self.label_3.setEnabled(True)
            self.label_4.setEnabled(True)
            self.pushButton.setEnabled(True)
            self.pushButton_3.setEnabled(True)
            self.lineEdit.setText("")
            self.lineEdit_2.setText("")
            self.lineEdit_3.setText("")
            self.pushButton.setText("确认新建")
            self.pushButton_3.setText("删除目录")
            try:
                if item.text(0) == '(根目录)':
                    self.treeSelect = 'BASIC'
                else:
                    self.treeSelect = self.check_root_in_Lists(item.text(0))
            except Exception as e:
                print(str(e))
            print(self.treeSelect)
        else:
            self.CurrentType = 2
            self.lineEdit.setEnabled(True)
            self.lineEdit_2.setEnabled(True)
            self.lineEdit_3.setEnabled(True)
            self.label.setEnabled(True)
            self.label_3.setEnabled(True)
            self.label_4.setEnabled(True)
            self.pushButton.setEnabled(True)
            self.pushButton_3.setEnabled(True)
            self.pushButton.setText("确认保存")
            self.pushButton_3.setText("删除预设")
            Names,Icon,Command ,ListNum = self.check_node_in_Lists(item.text(0))
            self.lineEdit.setText(Names)
            self.lineEdit_2.setText(Command)
            self.lineEdit_3.setText(Icon)
            self.treeSelect = ListNum
            self.treeSelect_2 = item.text(0)

    def check_root_in_Lists(self,args_name):
        for i in range(len(self.treeNode)):
            if self.treeNode[i].NodeType == 'root' and  self.treeNode[i].Name == args_name :
                    return self.treeNode[i].ListNum
        return 'ERROR'

    def check_node_in_Lists(self,args_name):
        for i in range(len(self.treeNode)):
            if self.treeNode[i].NodeType == 'noder' and  self.treeNode[i].Name == args_name :
                    return self.treeNode[i].Name,self.treeNode[i].Icon,self.treeNode[i].Command,self.treeNode[i].ListNum
        return 'ERROR','ERROR','ERROR','ERROR'

    def echo(self, value):
        QtWidgets.QMessageBox.information(self, "返回值",  "得到：{}\n\ntype: {}".format(value, type(value)), QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

    def addTreeRoot(self):
        lists , icons , listLs ,childs ,childicon, commands = main_function.fetch_lists()
        self.listCount = len(lists)
        basicroot = QtWidgets.QTreeWidgetItem(self.treeWidget)
        basicroot.setText(0, '(根目录)')
        basicroot.setText(1, "菜单")
        node = treeNode()
        node.setupRoot('root','(根目录)','BASIC',basicroot,'')
        #self.treeNode.append(basicroot)
        basicpatchlist, basiciconlist, basiccommandlist = main_function.BasicNodeRead()

        for t in range(len(basicpatchlist)):
            nodes = QtWidgets.QTreeWidgetItem(basicroot)
            nodes.setText(0, basicpatchlist[t])
            nodes.setText(1, "启动项")
            node = treeNode()
            node.setup('noder',basicpatchlist[t], nodes, basiciconlist[t], basiccommandlist[t], 'BASIC')
            self.treeNode.append(node)

        self.treeNode.append(node)
        for i in range(len(lists)):
            root = QtWidgets.QTreeWidgetItem(basicroot)
            root.setText(0, lists[i])
            root.setText(1, "菜单")
            node = treeNode()
            node.setupRoot('root',lists[i],listLs[i],root,icons[i])
            self.treeNode.append(node)
            for k in range(len(childs[i])):
                nodes = QtWidgets.QTreeWidgetItem(root)
                nodes.setText(0, childs[i][k])
                nodes.setText(1, "启动项")
                node = treeNode()
                node.setup('noder',childs[i][k], nodes,childicon[i][k],commands[i][k],listLs[i])
                self.treeNode.append(node)

if __name__ == "__main__":
    main_function.admin_get()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.args= sys.argv
    MainWindow.show()
    sys.exit(app.exec_())