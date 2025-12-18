
from PyQt5.QtWidgets import QWidget,QVBoxLayout,QLabel,QComboBox,QPushButton
import sqlite3
from ui.main_window import MainWindow
class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Авторизация")
        l=QVBoxLayout()
        self.box=QComboBox()
        c=sqlite3.connect("database/mettransterminal.db")
        for u in c.execute("SELECT id,username FROM users"):
            self.box.addItem(u[1],u[0])
        c.close()
        btn=QPushButton("Войти")
        btn.clicked.connect(self.login)
        l.addWidget(QLabel("Пользователь"))
        l.addWidget(self.box)
        l.addWidget(btn)
        self.setLayout(l)
    def login(self):
        self.m=MainWindow(self.box.currentData(),self.box.currentText())
        self.m.show()
        self.close()
