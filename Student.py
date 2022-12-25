
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
import sqlite3


class InsertDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(InsertDialog, self).__init__(*args, **kwargs)
        self.QBtn = QPushButton()
        self.QBtn.setText('Register')
        self.QBtn.setStyleSheet("QPushButton{\n"
                                "color: rgb(51, 51, 51);\n"
                                "background-color: rgb(241, 196, 15);\n"
                                "font: 11pt \"B Nazanin\";\n"
                                "border-radius: 5px;\n"
                                "}\n"
                                "QPushButton:Hover{\n"
                                "color: rgb(51, 51, 51);\n"
                                "background-color: rgb(255, 255, 255);\n"
                                "}")
        self.setWindowTitle('Add Student')
        self.setWindowIcon(QIcon("icons8-add-user-group-woman-man-100.png"))
        self.setFixedWidth(300)
        self.setFixedHeight(250)
        self.QBtn.clicked.connect(self.addstudent)
        layout = QVBoxLayout()
        self.nameinput = QLineEdit()
        self.nameinput.setPlaceholderText('Name')
        layout.addWidget(self.nameinput)
        self.branchinput = QComboBox()
        self.branchinput.addItem('Mechanical')
        self.branchinput.addItem('Civil')
        self.branchinput.addItem('Electrical')
        self.branchinput.addItem('Electronics and Communication')
        self.branchinput.addItem('Computer Science')
        self.branchinput.addItem('Information Technology')
        layout.addWidget(self.branchinput)
        self.seminput = QComboBox()
        self.seminput.addItem('1')
        self.seminput.addItem('2')
        self.seminput.addItem('3')
        self.seminput.addItem('4')
        self.seminput.addItem('5')
        self.seminput.addItem('6')
        self.seminput.addItem('7')
        self.seminput.addItem('8')
        layout.addWidget(self.seminput)
        self.mobileinput = QLineEdit()
        self.mobileinput.setPlaceholderText('Mobile')
        self.mobileinput.setInputMask('9999 999 9999')
        layout.addWidget(self.mobileinput)
        self.addressinput = QLineEdit()
        self.addressinput.setPlaceholderText('Adrress')
        layout.addWidget(self.addressinput)
        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def addstudent(self):
        name = ""
        branch = ""
        sem = 0
        mobile = 0
        address = ""
        name = self.nameinput.text()
        branch = self.branchinput.itemText(self.branchinput.currentIndex())
        sem = self.seminput.itemText(self.seminput.currentIndex())
        mobile = self.mobileinput.text()
        address = self.addressinput.text()
        try:
            self.conn = sqlite3.connect("database.db")
            self.c = self.conn.cursor()
            self.c.execute('INSERT INTO students (name,branch,sem,Mobile,address) VALUES (?,?,?,?,?)',
                           (name, branch, sem, mobile, address))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            QMessageBox.information(
                QMessageBox(), 'Successful', 'Student is added successfully to the database.')
            self.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error',
                                'Could not add student to the database.')


class SearchDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(SearchDialog, self).__init__(*args, **kwargs)
        self.QBtn = QPushButton()
        self.QBtn.setText('Search')
        self.QBtn.setStyleSheet("QPushButton{\n"
                                "color: rgb(51, 51, 51);\n"
                                "background-color: rgb(241, 196, 15);\n"
                                "font: 11pt \"B Nazanin\";\n"
                                "border-radius: 5px;\n"
                                "}\n"
                                "QPushButton:Hover{\n"
                                "color: rgb(51, 51, 51);\n"
                                "background-color: rgb(255, 255, 255);\n"
                                "}")
        self.setWindowTitle('Search User')
        self.setWindowIcon(QIcon("icons8-search-100.png"))
        self.setFixedHeight(100)
        self.setFixedWidth(300)
        self.QBtn.clicked.connect(self.searchstudent)
        layout = QVBoxLayout()
        self.searchinput = QLineEdit()
        self.onlyInt = QIntValidator()
        self.searchinput.setValidator(self.onlyInt)
        self.searchinput.setPlaceholderText('Roll No...')
        layout.addWidget(self.searchinput)
        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def searchstudent(self):
        searchrol = ''
        searchrol = self.searchinput.text()
        try:
            self.conn = sqlite3.connect("database.db")
            self.c = self.conn.cursor()
            result = self.c.execute(
                'SELECT * from students WHERE roll='+str(searchrol))
            row = result.fetchone()
            searchresult = "Roll no : "+str(row[0])+'\n'+"Name : "+str(row[1])+'\n'+"Branch : "+str(
                row[2])+'\n'+"Sem : "+str(row[3])+'\n'+"Address : "+str(row[5])
            QMessageBox.information(QMessageBox(), 'Successful', searchresult)
            self.conn.commit()
            self.c.close()
            self.conn.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), "Error",
                                'Could not find student from the database.')


class DeleteDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(DeleteDialog, self).__init__(*args, **kwargs)
        self.QBtn = QPushButton()
        self.QBtn.setText("Delete")
        self.QBtn.setStyleSheet("QPushButton{\n"
                                "color: rgb(51, 51, 51);\n"
                                "background-color: rgb(241, 196, 15);\n"
                                "font: 11pt \"B Nazanin\";\n"
                                "border-radius: 5px;\n"
                                "}\n"
                                "QPushButton:Hover{\n"
                                "color: rgb(51, 51, 51);\n"
                                "background-color: rgb(255, 255, 255);\n"
                                "}")
        self.setWindowTitle('Delete Student')
        self.setWindowIcon(QIcon("icons8-delete-100.png"))
        self.setFixedWidth(300)
        self.setFixedHeight(100)
        self.QBtn.clicked.connect(self.deletestudent)
        layout = QVBoxLayout()
        self.deleteinput = QLineEdit()
        self.onlyInt = QIntValidator()
        self.deleteinput.setValidator(self.onlyInt)
        self.deleteinput.setPlaceholderText('Roll No...')
        layout.addWidget(self.deleteinput)
        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def deletestudent(self):
        delrol = ""
        delrol = self.deleteinput.text()
        try:
            self.conn = sqlite3.connect('database.db')
            self.c = self.conn.cursor()
            self.c.execute("DELETE from students WHERE roll="+str(delrol))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            QMessageBox.information(
                QMessageBox(), 'Successful', "Deleted From Table Successful")
            self.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error',
                                'Could not Delete student from the database.')


class LoginDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(LoginDialog, self).__init__(*args, **kwargs)
        self.setFixedWidth(300)
        self.setFixedHeight(120)
        layout = QVBoxLayout()
        self.passinput = QLineEdit()
        self.passinput.setEchoMode(QLineEdit.Password)
        self.passinput.setPlaceholderText('Enter Password...')
        self.QBtn = QPushButton()
        self.QBtn.setText('Login')
        self.QBtn.setStyleSheet("QPushButton{\n"
                                "color: rgb(51, 51, 51);\n"
                                "background-color: rgb(241, 196, 15);\n"
                                "font: 11pt \"B Nazanin\";\n"
                                "border-radius: 5px;\n"
                                "}\n"
                                "QPushButton:Hover{\n"
                                "color: rgb(51, 51, 51);\n"
                                "background-color: rgb(255, 255, 255);\n"
                                "}")
        self.setWindowTitle('Login')
        self.setWindowIcon(QIcon("icons8-login-100.png"))
        self.QBtn.clicked.connect(self.login)

        self.title = QLabel('Login')
        self.font = self.title.font()
        self.font.setPointSize(18)
        self.title.setFont(self.font)
        layout.addWidget(self.title)
        layout.addWidget(self.passinput)
        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def login(self):
        if(self.passinput.text() == "123"):
            self.accept()
        else:
            QMessageBox.warning(self, 'Error', 'Wrong Password')


class AboutDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(AboutDialog, self).__init__(*args, **kwargs)
        self.setFixedWidth(300)
        self.setFixedHeight(150)
        self.setWindowTitle("About")
        self.setWindowIcon(QIcon("icons8-college-100.png"))
        QBtn = QDialogButtonBox.Ok
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        layout = QVBoxLayout()

        self.title = QLabel("STDMGMT")
        self.font = self.title.font()
        self.font.setPixelSize(20)
        self.title.setFont(self.font)
        layout.addWidget(self.title)
        layout.addWidget(QLabel('Version 5.3.3'))
        layout.addWidget(QLabel('Copyright 2022 College.'))
        layout.addWidget(self.buttonBox)
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.conn = sqlite3.connect('database.db')
        self.c = self.conn.cursor()
        self.c.execute(
            'CREATE TABLE IF NOT EXISTS students(roll INTEGER PRIMARY KEY AUTOINCREMENT ,name TEXT, branch TEXT,sem INTEGER,mobile INTEGER,address TEXT)')
        self.c.close()
        file_menu = self.menuBar().addMenu('&File')
        help_menu = self.menuBar().addMenu("&About")
        self.setWindowTitle('Student Mangement')
        self.setWindowIcon(QIcon("icons8-management-100.png"))
        self.setMinimumSize(800, 600)
        self.tableWidget = QTableWidget()
        self.setCentralWidget(self.tableWidget)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.tableWidget.setHorizontalHeaderLabels(
            ("Roll No.", "Name", "Branch", "Sem", "Mobile", "Address"))
        self.tableWidget.setStyleSheet(
            "background-color: rgb(255, 255, 255)")

        toolbar = QToolBar()
        toolbar.setMovable(False)
        self.addToolBar(toolbar)
        toolbar.setStyleSheet("background-color: rgb(241, 196, 15)")
        statusbar = QStatusBar()
        self.setStatusBar(statusbar)
        statusbar.setStyleSheet("background-color: rgb(255, 255, 255)")
        btn_ac_adduser = QAction(
            QIcon('icons8-add-user-group-woman-man-100.png'), "Add Student", self)
        btn_ac_adduser.triggered.connect(self.insert)
        btn_ac_adduser.setStatusTip('Add Student')
        toolbar.addAction(btn_ac_adduser)
        btn_ac_refresh = QAction(
            QIcon('icons8-refresh-100.png'), 'Refresh', self)
        btn_ac_refresh.triggered.connect(self.loaddata)
        btn_ac_refresh.setStatusTip('Refrsh Table')
        toolbar.addAction(btn_ac_refresh)
        btn_ac_search = QAction(QIcon("icons8-search-100.png"), "Search", self)
        btn_ac_search.triggered.connect(self.search)
        btn_ac_search.setStatusTip("Search User")
        toolbar.addAction(btn_ac_search)
        btn_ac_delete = QAction(QIcon("icons8-delete-100.png"), "Delete", self)
        btn_ac_delete.triggered.connect(self.delete)
        btn_ac_delete.setStatusTip("Delete User")
        toolbar.addAction(btn_ac_delete)
        adduser_action = QAction(QIcon(
            'icons8-add-user-group-woman-man-100.png'), "Insert Student", self)
        adduser_action.triggered.connect(self.insert)
        file_menu.addAction(adduser_action)
        searchuser_action = QAction(QIcon(
            "icons8-search-100.png"), "Search Student", self)
        searchuser_action.triggered.connect(self.search)
        file_menu.addAction(searchuser_action)
        deluser_action = QAction(
            QIcon("icons8-delete-100.png"), "Delete", self)
        deluser_action.triggered.connect(self.delete)
        file_menu.addAction(deluser_action)
        about_action = QAction(QIcon("icons8-info-100.png"), "Developer", self)
        about_action.triggered.connect(self.about)
        help_menu.addAction(about_action)

    def loaddata(self):
        self.connection = sqlite3.connect('database.db')
        query = 'SELECT * FROM students'
        result = self.connection.execute(query)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(
                    row_number, column_number, QTableWidgetItem(str(data)))
        self.connection.close()

    def handlePaintRequest(self, printer):
        document = QTextDocument()
        cursor = QTextCursor(document)
        model = self.table.model()
        table = cursor.insertTable(model.rowCount(), model.columnCount())
        for row in range(table.rows()):
            for column in range(table.columns()):
                cursor.insertText(model.item(row, column).text())
                cursor.movePosition(QTextCursor.NextCell)
        document.print_(printer)

    def insert(self):
        dlg = InsertDialog()
        dlg.exec_()

    def delete(self):
        dlg = DeleteDialog()
        dlg.exec_()

    def search(self):
        dlg = SearchDialog()
        dlg.exec_()

    def about(self):
        dlg = AboutDialog()
        dlg.exec_()


app = QApplication(sys.argv)
passdlg = LoginDialog()
if(passdlg.exec_() == QDialog.Accepted):
    window = MainWindow()
    window.show()
    window.loaddata()
sys.exit(app.exec_())
