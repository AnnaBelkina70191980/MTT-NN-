
from PyQt5.QtWidgets import QWidget,QVBoxLayout,QListWidget,QLabel
import sqlite3
class AdminWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Администрирование")
        l=QVBoxLayout()
        self.users=QListWidget()
        self.products=QListWidget()
        c=sqlite3.connect("database/mettransterminal.db")
        for u,r in c.execute("SELECT username,role FROM users"):
            self.users.addItem(f"{u} ({r})")
        for n,p in c.execute("SELECT name,price FROM products"):
            self.products.addItem(f"{n} — {p}")
        c.close()
        l.addWidget(QLabel("Пользователи"))
        l.addWidget(self.users)
        l.addWidget(QLabel("Товары"))
        l.addWidget(self.products)
        self.setLayout(l)
